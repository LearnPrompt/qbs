# QBS · 把书里的方法，变成能用的 Skill

从《High Output Management》开始，先解决一件事：**把内容团队的排期交出去，并且知道怎么验收。**

[![High Output Management 封面](https://images4.penguinrandomhouse.com/cover/9780679762881)](books/high-output-management.md)

Andrew S. Grove 著 · [书籍说明与阅读范围](books/high-output-management.md) · 封面由 Penguin Random House 提供，版权归原权利人。

你还没系统读过这个领域的书，也可以从一个真实问题开始：找可靠资料，把方法写成可重复执行的步骤，再拿新问题检验。**QBS 不要求你先成为专家，但要求方法有来源、结论有边界、结果能检查。**

`具体问题 → 核对书与原文 → 提取判断和操作 → 生成子 Skill → 新案例验证 → 真实使用反馈`

[马上使用](#马上使用) · [书籍与技能](#书籍与技能) · [安装](#安装) · [验证](#验证) · [添加一本书](#添加一本书)

## 马上使用

已经想把排期交给运营，直接用书籍子 Skill：

> 使用 $high-output-management。我想把内容排期维护和交稿提醒交给运营。下面是团队分工、任务和现有约定，请给我一张能转发的任务卡与验收标准：……

想把另一本书的方法做成自己的 Skill，用父 Skill：

> 使用 $qbs。我没系统学过这个领域，眼前的问题是……请先核对合适的资料，读到哪里就标到哪里，把适用条件、操作步骤、失败情形和验收标准做成一个书籍子 Skill，用新案例测试。

仅有书名时先找材料；已有指定书时直接围绕该书。不会把推荐一本书等同于已经读过，也不把一次聊天中的猜测变成通用规则。

## 书籍与技能

| 入口 | 负责什么 | 当前证据 |
|---|---|---|
| [`qbs`](skills/qbs/SKILL.md) · 父 Skill | 选资料、核对阅读范围、提取方法、创建和验证子 Skill | 见[行为试跑](evals/RESULTS.md) |
| [`high-output-management`](skills/high-output-management/SKILL.md) · 书籍子 Skill | 内容团队的委派、共享资源排期、提醒草稿和证据验收 | 模拟案例；未证明真实团队节省时间 |

**第一本书只读了出版社公开的 Ben Horowitz 2015 新版序言，未阅读全文。** 团队产出、提前规划、按任务经验安排指导是来源启发；具体时间字段、冲突检查和验收流程是本项目的场景设计。[查看来源映射](skills/high-output-management/references/source-notes.md)。

父子表示职责与索引关系：两个 Skill 各自有入口，分别安装。日常处理排期时直接调用子 Skill，不需要每次重新找书。书籍文件放在各自包里，离开本仓库仍能使用；未安装的子 Skill 不会因为索引里列出来就自动可用。

## 一次实际模拟，能检查什么

两条视频同日 13:00 交稿，唯一剪辑员 13:00–18:00 可用，每条需要 3 小时，两条都希望 18:00 发布。

试跑产物识别出：**5 小时可用容量装不下 6 小时剪辑**；即便另加剪辑员，审核完成后是否还留有发布和返工时间也要核对。没有把下班后的 19:00 当作可以承诺的完成时间。

另一个模拟中，运营按约定提醒并反馈风险，编辑仍然迟交。产物把「提醒与反馈」「任务维护记录」「内容按时交付」分开验收，没有用改截止时间消除延期记录。

这是模拟行为证据，不是线上团队业绩。完整输入与回答保留在 [evals](evals/RESULTS.md)。

## 安装

安装脚本面向 macOS / Linux，需要 Python 3.9+ 和 Git；只复制本地文件，不请求网络、不执行 Skill 内指令。先克隆本项目：

```bash
git clone https://github.com/LearnPrompt/qbs.git
cd qbs
```

Codex，安装父 Skill 与当前全部书籍子 Skill：

```bash
python3 scripts/install.py --dest ~/.codex/skills --dry-run
python3 scripts/install.py --dest ~/.codex/skills
```

Claude Code，指定对应目录：

```bash
python3 scripts/install.py --dest ~/.claude/skills
```

仅安装第一本书：

```bash
python3 scripts/install.py --dest ~/.codex/skills --skill high-output-management
```

也可以直接复制 `skills/qbs/` 和 `skills/high-output-management/` 到支持 Agent Skills 的宿主目录。宿主发现技能的方式可能不同；安装脚本验证文件一致性，**不代表每种宿主都已实机验收**。刷新技能列表或新开会话后，用上面的 `$qbs` / `$high-output-management` 话术试用。

预检查发现目标目录已存在时，脚本会在复制任何包前停止。每个包先暂存并校验再放入目标；安装中遇到异常会保留已经完整安装的包及并发出现的用户文件，并报告失败，不用删除整目录来回滚。更新前自行备份并比较本地改动，不覆盖已有私人规则。

## 验证

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

第一条检查技能包、独立引用、书籍索引和封面链接；第二条验证安装读回、单独安装、拒绝覆盖、异常时保留用户文件以及包校验的失败路径。这些都是静态或文件操作检查。

决策行为另由独立子代理处理未见过的模拟输入，再逐项核对结果。完整记录、局限和状态见 [验证记录](evals/RESULTS.md)。没有做同条件三组对照时，不声称它优于直接问模型；真实效果需要使用记录。

## 添加一本书

让 QBS 按 [子 Skill 合约](skills/qbs/references/child-contract.md) 制作即可。一个子 Skill 应包含：

- 能解决的具体问题与可观察交付。
- 实际读过的来源、范围与方法边界。
- 自身目录内的必要引用和模板。
- 带出版社封面及归属说明的书籍页。
- 新案例的输入、实际输出和判定。

在 `skills/qbs/references/library.json` 登记。只有目录、二手摘要或模型记忆时，不应发布「全书专家」；暂缺封面时可以继续做方法试验，书籍卡保持待补状态。

公开部分不要包含原书正文、私人团队资料或账户信息。MIT 许可只覆盖本项目原创代码、指令和说明，原书与封面不因此变成开源素材。

## 设计取舍

QBS 是本项目对「问题 → 书 → Skill」的工作流命名，不宣称行业标准或保证解决所有问题。书龄不是质量门槛，生成文件也不等于拥有专业能力。

本次用 [laoyeye](https://github.com/LearnPrompt/laoyeye) 的点子王路径审视父子结构，保留了来源范围、独立安装和反例验证，删掉了不必要的平台与批量抓书设想。[阅读审视记录](docs/laoyeye-review.md)。

本项目不自带任务系统连接器或常驻提醒。起草任务卡不等于授权修改外部系统或给同事发送消息。
