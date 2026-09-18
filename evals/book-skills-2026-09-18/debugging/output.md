**D1：已修复，8 项回归测试全部通过。**

根因是 `_cache` 只按业务 key 保存首次切片。同 key 再次调用时，代码跳过切片计算，忽略新的 offset、limit 和 rows；`list(_cache[key])` 只是复制旧结果。它违反了你给出的“每次返回当前 rows 对应切片”的约定。

所有复制、修改和运行均在 `./` 中完成，源文件没有改动。环境为 Python 3.9.6、macOS 27.0 arm64。

实验预测已在运行前写入 [experiment-plan.md](./experiment-plan.md)。关键命令：

```sh
cd <trial-directory>
python3 experiments.py > experiments.log
python3 -m unittest -v test_listing > before-tests.log 2>&1
# 应用 fix.diff 对应的修复后：
python3 -m unittest -v test_listing > after-tests.log 2>&1
diff -u original_listing.py listing.py
```

实验以 `rows=[0,1,2,3,4,5]` 开始；首次调用返回 `[0,1]`，是成功对照。

| 实验 | 运行前预测（若缓存解释成立） | 实际观察 | 按约定应返回 |
|---|---|---|---|
| 同 key，offset=2、limit=2 | 仍返回首次结果 | `[0,1]` | `[2,3]` |
| 新 key，同样 offset=2、limit=2 | 返回当前切片 | `[2,3]` | `[2,3]` |
| 直接执行 rows[2:4] | 切片正确 | `[2,3]` | `[2,3]` |
| 同 key，limit=3 | 仍返回首次结果 | `[0,1]` | `[0,1,2]` |
| 同 key，rows 替换为 [10,11,12] | 仍返回首次结果 | `[0,1]` | `[10,11]` |
| 同 key，原 rows[0] 改成 99 | 仍返回首次结果 | `[0,1]` | `[99,1]` |
| 清空本地缓存后，offset=2 | 恢复当前切片 | `[2,3]` | `[2,3]` |

失败的换页完全在有效范围内，同一切片用新 key 又正常，因此“切片越界”不能解释本次失败。清空本地状态后的恢复支持缓存解释；它也解释了新进程空缓存时首个请求恢复正常的机制，未执行或验证线上重启。

最小修复位于 [listing.py](./listing.py)：移除缓存，每次用当前输入切片，保留 key 参数兼容现有调用。

```python
def page(key, rows, offset=0, limit=2):
    return list(rows[offset:offset + limit])
```

仅把 offset、limit 加进缓存 key 仍不能处理 rows 更新，因此本次直接取消缓存。不引入数据库或第三方依赖。

[test_listing.py](./test_listing.py) 修复前实跑 8 项，5 项失败、3 项通过；修复后相同测试全部通过。覆盖换页、改变 limit、替换和原地修改数据、空列表、offset 超出长度、尾页不足 limit、返回 list 和返回容器隔离。原始输出分别保存在 [before-tests.log](./before-tests.log)、[after-tests.log](./after-tests.log)，实验原始输出在 [experiments.log](./experiments.log)。已检查最终差异 [fix.diff](./fix.diff)，仅涉及移除这层缓存。已给出的本地症状均得到解释和验证，没有开展线上验证。

本次实际用了“先预测，再用对照实验检验假设”：[Testing a Hypothesis](https://www.debuggingbook.org/html/Intro_Debugging.html#Testing-a-Hypothesis)。可以继续想一个问题：同样的切片参数只换 key 就恢复正常，为什么比“重启后好了”更能定位原因？

**D2：目前只能确认收到“线上偶尔保存失败”的报告，无法复现，根因未定。**

没有日志、失败输入、环境或代码，也没有线上访问权限；现在不能判断失败发生在前端、传输还是服务端，更不能宣布修复。未运行任何线上动作，也未重启服务。

下一步最有价值的是收集一个失败样本和一个相近的成功样本。请提供失败发生时间（含时区）、操作步骤、界面原始报错、脱敏后的保存内容，以及同内容重试是否成功；已有请求 ID、状态码、客户端/服务版本也一并保留。敏感字段、令牌和个人信息需要去掉。若这些信息要从线上取，由有权限的同事提取相关请求的最小脱敏片段即可。

材料到位后，先明确“保存成功”的判据，再按同一请求 ID 对齐客户端结果和服务端记录，检查是否实际持久化。待执行的判断是：若客户端报错但服务端已落库，说明“显示失败”不等于“未保存”；若请求已到达却被拒绝，再用错误码和失败/成功输入差异检验原因；若找不到服务端记录，先确认日志覆盖和关联方式，不能直接判定请求没到达。取得代码和可重放的脱敏样本后，才在获准的本地或测试环境复现。

上述是尚未执行的取证与实验计划，不是已经观察到的现象；偶发问题需要记录发生频率和条件，一次重试成功不足以说明已经修好。

本次实际使用的是把已知事实与待验证解释分开，并确定下一项可区分原因的证据：[The Scientific Method](https://www.debuggingbook.org/html/Intro_Debugging.html#The-Scientific-Method)。下一步要回答的问题是：用户看到保存失败时，对应数据究竟有没有写入？
