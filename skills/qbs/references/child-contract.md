# 子 Skill 合约

父子关系是工作流与索引关系，不依赖模型运行时支持继承。每个子 Skill 自带所需规则和来源，可以单独复制安装。

## 仓库布局

```text
skills/qbs/                         父 Skill
skills/<book-skill>/SKILL.md          独立可发现的子 Skill
skills/<book-skill>/references/      方法出处和按需模板
skills/<book-skill>/agents/openai.yaml
books/<book-id>.md                   面向读者的书籍说明，含封面
evals/                              新案例、评分标准与实际结果
```

只有 `skills/` 下的文件会随安装复制；子 Skill 运行必需的内容必须放在自身目录，不能引用仓库外的书籍页或兄弟 Skill 才能工作。书籍页用于浏览，来源说明属于安装包。

## 先形成一条完整方法

对每条会改变判断的方法记录：

| 项目 | 要回答的问题 |
|---|---|
| 任务 | 具体解决哪类问题？ |
| 来源 | 哪个版本的哪部分？已读正文还是转述？ |
| 条件 | 哪些事实成立时适用？什么情况下不适用？ |
| 操作 | 需要哪些输入，如何选择下一步？ |
| 交付 | 用户能检查的产物是什么？ |
| 失败 | 什么结果说明方法或使用条件有问题？ |
| 归属 | 来源概括、推断、场景设计，分别是哪部分？ |

不要为了填表扩写原文没有的理论。公开序言最多支撑其实际涉及的方法；源于自拟实践的流程要保留场景设计身份。

## 最小交付

- `SKILL.md` 有 name、description、任务入口、判断步骤与可观察验收。目录名与 name 一致。
- `references/source-notes.md` 有书目/作者、来源链接、阅读日期、已读/未读边界、规则映射；不复制大段原文。
- 按任务需要添加模板或脚本；不默认每本书必须有脚本。
- `agents/openai.yaml` 的 default_prompt 显式提到 `$<skill-name>`。
- `books/<book-id>.md` 显示官方封面、封面来源、作者、版本、阅读范围、用途和可复制调用语。封面与书的版权不随项目 MIT 授权。
- `evals/` 保留测试输入、产物和判定依据。结构校验不能替代行为试跑。

## 登记

`skills/qbs/references/library.json` 为唯一书籍索引，字段包含 `id`、`title`、`author`、`isbn`、`skill`、`skill_path`、`book_path`、`scope`、`reading_scope`、`source_url`、`cover_url`、`book_url`、`status`。

`status` 只用 `draft`、`simulated`、`field-tested`。完整书籍卡和一次通过的行为试跑可标 simulated；field-tested 需要真实使用记录以及能核验的适用范围。模板完整、文件格式通过不提升状态。故障修复应保留变更和复测证据。
