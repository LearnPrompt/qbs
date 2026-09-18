# 手动安装与本地维护

推荐先用 [README 的 npx 一行安装](../README.md#安装)。需要自行控制复制路径、离线安装或维护仓库时，再用下面的方式。

## 手动安装

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

也可以直接复制 `skills/qbs/` 和 `skills/high-output-management/` 到支持 Agent Skills 的宿主目录。宿主发现技能的方式可能不同；安装脚本验证文件一致性，**不代表每种宿主都已实机验收**。刷新技能列表或新开会话后，用 [README 的调用示例](../README.md#安装)试用。

预检查发现目标目录已存在时，脚本会在复制任何包前停止。每个包先暂存并校验再放入目标；安装中遇到异常会保留已经完整安装的包及并发出现的用户文件，并报告失败，不用删除整目录来回滚。更新前自行备份并比较本地改动，不覆盖已有私人规则。

