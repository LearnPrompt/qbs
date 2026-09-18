# High Output Management

[![High Output Management 封面](https://images4.penguinrandomhouse.com/cover/9780679762881)](https://penguinrandomhousehighereducation.com/book/?isbn=9780679762881)

书作者：**Andrew S. Grove** · ISBN：9780679762881。封面来自 Penguin Random House 图片服务，点击封面可到出版社书目页；封面及原书版权归各自权利人，不属于本项目开源许可。

## 这本书对应什么问题

把内容排期和交稿提醒交出去后，仍需要自己盯进度；文案、审核和剪辑接不上；任务延期时，分不清是交付问题、容量问题还是排期维护遗漏。

本项目把上述问题整理为 [high-output-management 子 Skill](../skills/high-output-management/SKILL.md)：定义可验收的委派、检查依赖和共享资源、区分原承诺与获批改期、生成提醒草稿，并按证据分别验收排期服务和内容交付。

## 如何调用

安装后可独立调用，不要求先运行 QBS。提供现有任务、团队分工、日期时区和可用工时；没有工具接入也可先做草稿。

> 使用 $high-output-management。我想把项目的排期维护和交稿提醒交给运营。请根据以下团队与任务，给我一张任务卡，并指出会影响交付的缺失信息：……

也可直接检查已有安排：

> 使用 $high-output-management。以下几条任务共用一位剪辑和一位审核，请检查依赖与容量，保留原承诺，提出需要负责人决定的调整：……

> 使用 $high-output-management。根据以下职责约定、提醒记录和交付记录，分别验收运营的排期服务与内容交付；证据不足的地方请标出来：……

这些是输入示例，不是已通过的测试报告。此 Skill 不会仅因被调用就发送消息或修改外部任务。

## 阅读边界

**状态：draft，待补完整相关正文章节。** 现有规则仍可用于场景演练，但不能作为已完成的书籍方法提炼。至少完整读一个相关正文章节后，才能逐条补来源、改规则并重测。

**当前版本只依据出版社公开的 Ben Horowitz 2015 新版序言，未阅读全文。** 序言介绍了团队产出、提前规划、按任务经验调整管理方式及培训的价值；本项目将这些启发转成具体内容团队规则，规则并非 Grove 原书的逐章提炼。

详见 [来源映射](../skills/high-output-management/references/source-notes.md) 与 [出版社公开试读](https://penguinrandomhousehighereducation.com/book/?isbn=9780679762881#excerpt)。扩展到新章节前，需要补充可使用的原文和阅读记录；不以模型记忆代替原文核对，也不把场景测试当成真实团队效果证明。
