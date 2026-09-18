[简体中文](README.md) · **English** · [日本語](README.ja.md)

# QBS · Build a Skill in an unfamiliar field, starting with a question

> *“Bring your question. Let AI find books, read the relevant chapters, and turn their methods into a Skill of your own.”*

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-QBS-blueviolet)](skills/qbs/SKILL.md)
[![Package checks](https://github.com/LearnPrompt/qbs/actions/workflows/check.yml/badge.svg)](https://github.com/LearnPrompt/qbs/actions/workflows/check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**QBS = Question → Book → Skill.** You bring a problem you want to solve. QBS guides AI to find relevant books, read the relevant main-text chapters in full, extract methods, build a Skill you can invoke independently, and test it on an actual task.

[How to build a Skill](#workflow) · [Install QBS](#install) · [First use](#first-use) · [What you get](#deliverables) · [Examples and progress](#examples)

---

<a id="why-qbs"></a>

## You want to make a Skill. What experience should go into it?

When you use Codex every day and keep running into the same problem, saving a way to handle it as a Skill feels natural.

But what happens when the field is unfamiliar? You haven't read the books or built up much experience. Which steps should you include? How can you check the judgments AI makes?

Turning a few conversations into a file gives you a file. It still leaves the basis for the method unresolved.

That's why we made QBS. Describe the problem in front of you, then let AI find books, obtain the main text, read it, and extract methods. Read the chapters relevant to this one problem, then turn the author's methods, conditions, and exceptions into steps you can follow and check.

**Start with a real problem and make a Skill with sources, something you can try and keep improving. You don't need to study the entire field first.**

<a id="workflow"></a>

## From a question to your own Skill

```mermaid
flowchart TD
    A["You bring a problem<br/>What you want to achieve · Where you are stuck"] --> B["QBS finds books and selects chapters<br/>Check why the book fits this problem"]
    B --> C{"Are the relevant<br/>main-text chapters available in full?"}
    C -- "No" --> D["Keep looking for accessible main text<br/>If gaps remain, name the missing chapters and materials needed"]
    D -- "Obtain the missing material" --> C
    C -- "Yes" --> E["AI reads the relevant chapters in full<br/>Record methods, conditions, exceptions, and sources"]
    E --> F["Build your Skill<br/>Inputs → Decision steps → Deliverables → Acceptance checks"]
    F --> G["Try it on a new task<br/>Check whether the method is applied correctly and the result is useful"]
    G -- "Checks fail: revise or read more" --> E
    G -- "Checks pass" --> H["Deliver the Skill, trial output, and reading entry points<br/>Invoke it directly when a similar problem comes up"]
```

The full process is in the [QBS Skill](skills/qbs/SKILL.md). If the main text isn't available, it reports the specific gaps. Finding a title or reading a foreword does not count as reading the relevant chapters.

### How fast can it be?

You can start directly with your problem, without first choosing books yourself or studying the entire field. QBS connects finding books, reading, building, and trying the Skill in one workflow. The time needed depends on access to the main text, how much needs reading, and how many revisions the trial calls for. We don't yet have complete timing data, so we aren't promising “done in minutes.”

<a id="install"></a>

## Install QBS with one command

On a computer with Node.js, npm (including `npx`), and Git installed, run:

```bash
npx skills@latest add LearnPrompt/qbs --skill qbs
```

Select the Agent you use. Installation defaults to the current project; add `-g` to the end of the command to use it across all projects. After installation, open a new session and ask QBS to help you make your own Skill.

<details>
<summary>Choose an Agent</summary>

Install for Codex and Claude Code in the current project:

```bash
npx skills@latest add LearnPrompt/qbs --skill qbs -a codex claude-code -y
```

</details>

[Installer and options](https://github.com/vercel-labs/skills#install-a-skill) · [Installation checks](docs/npx-install-check.md) · [Manual installation](docs/manual-install.md). If you already have a Skill with the same name and have edited it, back it up before updating.

<a id="first-use"></a>

## After installation, give QBS your problem

Replace the brackets below with your own situation, then send this to your Agent:

```text
Use $qbs. I'm unfamiliar with [field], and I want to solve [specific problem]. The result I want is [something I can check]. Find relevant books, obtain and read the relevant main-text chapters in full, turn the methods into a Skill I can invoke independently, and try it on a new task. Deliver the Skill, the trial results, and a record of the chapters actually read and the sources for the methods. If the full main text isn't available, explain the specific gaps.
```

For example: “Use $qbs. When I build small features in Codex, the requirements keep growing with every conversation. Find books and read the relevant chapters in full, make a Skill that helps me define this round's scope, then try it on my current feature request.”

You don't need to know a book title in advance. If you've already chosen a book or have an electronic file or chapter materials, you can provide them too.

<a id="deliverables"></a>

## What should you get at the end?

| Deliverable | What you can check |
|---|---|
| A Skill you can invoke independently | When to use it, what input it needs, which steps to follow, and what it delivers |
| Sources and a reading record | Which chapters of which books were actually read, which rules came from the books, and which were added for the scenario |
| Output from a trial on a new task | What the input was, how the method was used, and which acceptance checks passed or failed |
| A place to keep reading | Where the method used appears in the book and where to start if you want to explore further |

When a similar problem comes up, invoke the Skill you've made. For a new field, start with QBS again. A book list or an untested file alone doesn't complete the process.

---

<a id="examples"></a>
<a id="everyday-problems"></a>
<a id="reading-status"></a>

## What we're making through this process

Scheduling was our first case while exploring QBS. We later chose books for two more problems that often come up in Codex. These examples show outputs at different stages, including where the process still has gaps to close.

| Problem | Book | Current progress |
|---|---|---|
| How do you delegate, schedule, and assess work handed to colleagues? | [High Output Management](books/high-output-management.md) | An installable draft exists. Only the publicly available foreword to the newer edition has been read in full; relevant main-text chapters are still missing. It does not yet meet the current QBS chapter-reading requirement. |
| How do you keep a small feature from growing endlessly? | [Shape Up](books/shape-up.md) | Chapters 3 and 14 read in full; not yet packaged as a child Skill. |
| After several attempted bug fixes, how do you stop guessing? | [The Debugging Book](books/the-debugging-book.md) | Introduction to Debugging read in full, including exercise solutions; not yet packaged as a child Skill. |

<a id="scheduling-flow"></a>

<details>
<summary>Expand the first output example: a scheduling Skill draft</summary>

Two videos each need 3 hours of editing, but the only editor has just 5 hours available. The draft's simulated output identified that the work wouldn't fit and required checking review, revision, and publication time again. The two scheduling and acceptance flowcharts are in the [case details](docs/scheduling-example.en.md); they describe this child Skill's business workflow.

[Simulation inputs and actual outputs](evals/RESULTS.md) · [Draft entry point](skills/high-output-management/SKILL.md)

If you happen to want to try this draft, install it separately:

```bash
npx skills@latest add LearnPrompt/qbs --skill high-output-management
```

```text
Use $high-output-management. Both video drafts arrive at 13:00, and each needs 3 hours of editing. The only editor is available from 13:00 to 18:00, and both videos are intended for publication at 18:00. First determine whether the work fits, then tell me what decisions I need to make. Don't assume anyone will work overtime.
```

These are scenario designs and simulations. In the earlier [three-way comparison](evals/comparison-2026-09-18/REPORT.md), ordinary conversation also reached the correct core conclusions. It did not establish that this draft performs better than direct conversation.

</details>

<details>
<summary>Validation commands for maintainers</summary>

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These check Skill packages, references, the book index, multilingual documentation links, installed-file readback, and failure handling. [GitHub Actions](https://github.com/LearnPrompt/qbs/actions/workflows/check.yml) runs the checks automatically, and the badge at the top shows their actual status. Whether the methods from the books help in practice still depends on trial records from the corresponding tasks.

</details>

<a id="next-book"></a>

## Try a method, and perhaps you'll want to open the book

It's been a while since we really read a book. So I also want this process to leave one small next step: whenever a Skill delivers its result, tell me which chapter that decision came from.

Let a method take part in today's work first. If it helps, curiosity may follow: why does the author think this way, and what else is worth reading?

**Make a Skill with a question in mind. Then return to the book with the curiosity that using it creates.**

[Child Skill contract](skills/qbs/references/child-contract.md) · [MIT](LICENSE) (applies to this project's original code and documentation; book texts and covers remain the copyright of their respective rights holders)
