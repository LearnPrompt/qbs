# The Debugging Book

**Andreas Zeller** · *Tools and Techniques for Automated Software Debugging* · CISPA Helmholtz Center for Information Security 发布的持续更新在线教材。[官方书页](https://www.debuggingbook.org/)。下图使用官网 `og:image` 指定的展示图（在线教材），不是纸本封面。

![The Debugging Book 官网展示图](https://www.debuggingbook.org/html/PICS/wordcloud.png)

图片来源：[官方书页](https://www.debuggingbook.org/)，版权归原权利人。

## 从什么麻烦找到它

在 Codex 里遇到 bug，反复试改，却说不清是哪一个猜测被证实了。我们想先把观察、假设和修复之间的关系弄清楚。

这次选读 [Introduction to Debugging](https://www.debuggingbook.org/html/Intro_Debugging.html)。它用一个小程序，把发现异常、提出解释、设计实验和检查修复串起来，可以边读边运行。

## 这次完整读了哪里

2026-09-18，完整读取[官方章节 Notebook](https://www.debuggingbook.org/notebooks/Intro_Debugging.ipynb)的 0–216 号 cell，从章首一直到 Exercise 2 的末尾答案。正文、代码、练习答案均已覆盖；关键图的关系通过渲染图、完整 SVG 或生成代码核对。页面 Last change 标记为 2024-10-15。

实跑了原始失败、诊断断言、正文修复的回归，以及练习中的混合引号案例。未运行完整 Jupyter 环境，未播放讲课视频，未读后续自动缩减或统计调试章节。

## 哪些地方可以先用起来

| 原书位置 | 方法 | 放进 Codex 的尝试 |
|---|---|---|
| [Testing a Hypothesis](https://www.debuggingbook.org/html/Intro_Debugging.html#Testing-a-Hypothesis) | 先给出预测，再用实验检验 | 每次试改前，说清本次观测能排除哪个解释 |
| [Checking Diagnoses](https://www.debuggingbook.org/html/Intro_Debugging.html#Checking-Diagnoses) | 解释失败的因果关系与被违反的规则 | 多个症状不一定同源，解释不通的部分单独保留 |
| [Keep a Log](https://www.debuggingbook.org/html/Intro_Debugging.html#Keep-a-Log) 与 [Homework after the Fix](https://www.debuggingbook.org/html/Intro_Debugging.html#Homework-after-the-Fix) | 留下实验记录，修复后防止复发 | 记录预期与实际结果，再检查原失败与原成功案例 |

右列是本项目的场景适配，已打包为可独立安装的 [the-debugging-book Skill](../skills/the-debugging-book/SKILL.md)。完整来源与方法映射随安装包提供，见[来源说明](../skills/the-debugging-book/references/source-notes.md)。不据此声称能减少真实项目的调试时间。

## 带着这个问题接着读

**为什么两个看起来不同的错误，可能来自同一个条件判断？为什么一个通过了测试的补丁，还可能没修完？**

先从 [A Simple Function](https://www.debuggingbook.org/html/Intro_Debugging.html#A-Simple-Function) 的程序看起。观察书中每一步怎么把一个猜测变成可检查的实验。

## 安装后直接用

```bash
npx skills@latest add LearnPrompt/qbs --skill the-debugging-book
```

> 使用 $the-debugging-book，处理我这个反复出现的错误：[复现步骤、代码位置、预期和实际结果]。先用实验区分原因，再完成有证据的修复和回归。最后指给我看，这次最关键的判断在章节哪里。

你会拿到：可复现的基线、实验预测与实际结果、解释因果和错误性的诊断、已授权范围内的修复及回归记录。缺乏运行条件时明确交付证据缺口，不冒充修好。此 Skill 可单独使用，不要求安装父 Skill；新领域仍从 QBS 的找书、读章路线开始。

已完成一次独立模拟试跑：实际修复分页故障并跑通 8 项回归；无证据场景保留未知。见[原始产物与判定](../evals/book-skills-2026-09-18/REPORT.md)。状态为 simulated，不代表真实项目效果。

## 为什么这次选它

也核对了同作者 [Why Programs Fail 第二版](https://www.whyprogramsfail.com/book.php)的[目录](https://www.whyprogramsfail.com/toc.php)，其中 Scientific Debugging 很相关。本次优先选择已经取得完整正文和可运行案例的 The Debugging Book；另一本只核对了书目与目录，未读完整章。

这是选书、阅读范围与对应 Skill 的说明。书籍正文、代码许可按[原书说明](https://www.debuggingbook.org/)执行，不随本项目 MIT 许可重新授权。
