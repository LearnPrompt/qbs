# npx 安装实测

日期：2026-09-18。安装器：`skills 1.7.0`。来源：公网 `LearnPrompt/qbs`，技能文件版本为 `840b35b`；本次仅修改安装文档与 README 展示，技能包内容未变。

采用 [LearnPrompt 的一行安装规范](https://github.com/LearnPrompt/luban-skill/blob/main/references/house-style.md)；命令形式也与 [laoyeye](https://github.com/LearnPrompt/laoyeye#安装) 一致。参数以 [skills 官方说明](https://github.com/vercel-labs/skills#install-a-skill) 为准。

## 实际执行

在各自全新的临时项目中执行以下命令。调用 `npx` 时添加了 `--yes`，只用于确认下载 CLI；其余选项如下。

```bash
npx skills@latest add LearnPrompt/qbs --list
npx skills@latest add LearnPrompt/qbs
npx skills@latest add LearnPrompt/qbs --skill qbs high-output-management -a codex claude-code -y
npx skills@latest add LearnPrompt/qbs --skill qbs -a codex -y
npx skills@latest add LearnPrompt/qbs --skill high-output-management -a claude-code -y
```

## 读回结果

| 场景 | 结果 |
|---|---|
| 公网发现 | 列出 `qbs` 和 `high-output-management` 两个 Skill |
| README 默认入口 | 当前 Codex 环境自动安装两个 Skill；共 10 个文件与仓库逐字节一致 |
| 同时指定 Codex、Claude Code | 两个 Skill 均可读取；正文、界面配置与 references 完整 |
| 只装父 Skill | 只有 `qbs`，5 个文件与仓库一致，`skills list` 可见 |
| 只装子 Skill | 只有 `high-output-management`，5 个文件与仓库一致，`skills list` 可见 |

Codex 使用项目内 `.agents/skills/`；本次同时指定两种 Agent 时 Claude Code 使用链接，单独指定 Claude Code 时实际复制到 `.claude/skills/`。验收按真实落盘位置读回，没有把“命令返回成功”当成文件完整的证明。

本次验证的是公开仓库的发现、下载、安装和文件完整性，不代表所有宿主都已逐一实机调用，也不补足书籍正文阅读或方法有效性的证据。未改动用户现有全局 Skill。
