# 来源、阅读范围与方法归属

## 为什么选这本书

任务是“Codex 反复改 bug，却说不清哪个猜测被证实”。**Andreas Zeller，The Debugging Book: Tools and Techniques for Automated Software Debugging** 的入门章提供连续的可运行案例，从失败走到实验、诊断和回归，直接对应这个问题。

[官方书页](https://www.debuggingbook.org/)由 CISPA Helmholtz Center for Information Security 发布，是持续更新的在线教材。本次章节页面 Last change 为 2024-10-15，不把它当作固定纸书版次。同作者 Why Programs Fail 第二版也匹配科学调试主题，但本次只核对其书目和目录，未用未读正文生成规则。

## 实际读到哪里

- 阅读日期：2026-09-18。
- [Introduction to Debugging 全章](https://www.debuggingbook.org/html/Intro_Debugging.html)。
- [官方 Notebook](https://www.debuggingbook.org/notebooks/Intro_Debugging.ipynb)：**217 个 cell，0–216**，从章首到 Exercise 2 Part 3 最后回归断言，正文、代码与练习答案完整覆盖。创建本 Skill 时再次逐段读取本地保存的官方 Notebook 全部 cell。
- 关键状态图/传播图已通过图像、完整 SVG 或生成代码核对。未播放嵌入视频，未细看装饰照片；未运行完整 Jupyter 环境。
- 本次前序阅读记录中，原始失败、诊断断言、正文修复后的 6 条回归和练习混合引号案例已实跑。本 Skill 创建时又独立运行章节函数与对应断言，验证原缺陷、正文修复和练习改进之间的区别。
- 未读后续自动缩减、统计调试、跟踪器实现章节；本 Skill 不包含那些工具的实现，也不声称能够自动定位任何根因。

## 方法到出处

| 方法 | 原文位置 | 在 Skill 中的用途与边界 |
|---|---|---|
| 明确正确结果并保留失败测试 | Testing a Function、Oops! A Bug!；cell 17–28 | 记录预期及来源，把失败变为能重跑的基线。环境/版本字段是项目适配。 |
| 观察与预测分开，用实验支持或推翻解释 | [The Scientific Method](https://www.debuggingbook.org/html/Intro_Debugging.html#The-Scientific-Method)、Testing a Hypothesis、Refining/Refuting a Hypothesis；cell 96–140 | 先写预测再实跑，有竞争解释时选能区分它们的实验。不强制两个假设或固定轮数。 |
| 从失败追溯到错误状态与缺陷 | [From Failure to Defect](https://www.debuggingbook.org/html/Intro_Debugging.html#From-Failure-to-Defect)；cell 78–95 | 说明故障传播链。并非所有状态都有规格，证据不足时继续观测。 |
| 同时证明因果与错误性 | [Checking Diagnoses](https://www.debuggingbook.org/html/Intro_Debugging.html#Checking-Diagnoses)；cell 148–150；Alternate Paths，cell 157 | 修复既要解释当前失败，又要纠正违反的规则。多症状可能同源，不强行统一。 |
| 复测原失败与原成功，继续检查相关边界 | Fixing the Code；cell 151–156；[Exercise 2: More Bugs!](https://www.debuggingbook.org/html/Intro_Debugging.html#Exercise-2:-More-Bugs!)，cell 198–216 | 正文补丁通过已有测试，混合引号仍会暴露另一问题。边界测试按修改逻辑选择，不从一次通过推断全局正确。 |
| 留日志、防复发 | [Keep a Log](https://www.debuggingbook.org/html/Intro_Debugging.html#Keep-a-Log)，cell 174–176；[Homework after the Fix](https://www.debuggingbook.org/html/Intro_Debugging.html#Homework-after-the-Fix)，cell 158–172 | 对照旧观察判断新假设，补回归并检查相似缺陷。外部收尾行动仍由用户任务授权决定。 |

这里的“实验表、简短交付格式、无法复现时的材料需求、按风险压缩步骤、用后阅读入口”是本项目适配，不是作者规定的 Skill 标准。上述内容为方法概括，没有复制整章或打包原书代码。

## 适用与证据边界

适合能取得代码与失败材料的程序调试，尤其是猜测式试改、多处症状或需要交接的诊断。异步竞态、分布式故障和偶发性能问题可能需要额外观测或统计方法；没有足够证据就报告限制。

阅读案例复跑与 Skill 包结构校验均不证明此 Skill 在新任务中有效，也不证明它优于普通 AI 对话。发布状态与独立行为试跑证据由仓库验证记录单独维护。

原书文字、图与代码许可见[官方许可说明](https://www.debuggingbook.org/html/Intro_Debugging.html)。它们不随本项目 MIT 许可重新授权。
