# Scheduling Skill draft: workflow example

This is the business workflow of the `high-output-management` draft, not the full QBS process for creating a Skill. Only the publicly available foreword has been read in full; the relevant main-text chapters are still missing. The draft does not yet meet the current QBS chapter-reading requirement.

[Back to QBS examples](../README.en.md#examples)


**The lead defines deliverables and approves changes; the coordinator schedules milestones and reports conflicts; contributors deliver the work.**

### First, schedule the work: if it won't fit, bring options to the lead

```mermaid
flowchart TD
    A["Lead defines the goal<br/>Deliverables · Deadline · Acceptance criteria"] --> B["Coordinator schedules the full workflow<br/>Draft → Editing → Review → Revisions → Publication<br/>Check staffing, work hours, and availability at each step"]
    B --> C{"Can every step<br/>finish on time?"}
    C -- "No / Not enough information" --> D["Coordinator reports the specific bottleneck<br/>Missing people, time, or information?"]
    D --> E["Lead decides how to adjust<br/>Reduce scope · Reschedule · Add help · Get information"]
    E -- "Reschedule with the new conditions" --> B
    C -- "Yes" --> F["Lead confirms; coordinator sends task cards<br/>Who delivers what · By when · Who accepts it<br/>Checkpoints and risk reporting requirements"]
    F --> G["Contributors deliver; coordinator follows up<br/>New risks go back through bottleneck resolution"]
    G --> H["Lead assesses each area separately<br/>Reminders, records, and content delivery"]
    classDef lead fill:#e8efff,stroke:#4169a1,color:#182b49;
    classDef decision fill:#fff3d6,stroke:#b37b17,color:#503a13;
    classDef done fill:#e6f4eb,stroke:#43845b,color:#21422d;
    class A,E,F lead;
    class C,D decision;
    class H done;
```

For example: both video drafts arrive at 13:00, each needs 3 hours of editing, and both are intended for publication at 18:00. The only editor is available from 13:00 to 18:00. **There are 6 hours of work and only 5 hours available**, so the editing stage already makes the schedule impossible. **19:00 is outside the editor's working hours and cannot be treated as available time. Even with another editor, review, revisions, and publication must all be checked again.**

### Then, assess the work: sending reminders doesn't mean everything passed

```mermaid
flowchart TD
    A["Lead checks the agreement and records from the time<br/>Assess three areas separately"] --> B["Reminders and risk reporting<br/>Completed as agreed?"]
    A --> C["Schedule records<br/>Accurate, with history preserved?"]
    A --> D["Content delivery<br/>On time and up to standard?"]
    B --> E["Assess the coordinator's reminder work<br/>A writer's late delivery does not mean the coordinator failed"]
    C --> F["Check four dates or times<br/>Original commitment · Forecast · Approved · Actual<br/>Responsibility for changes requires a record of who made them"]
    D --> G["Assess the content owner's delivery<br/>A forecast delay is not an approved deadline change<br/>Check timing and quality separately"]
    E --> H["Give a result for each area<br/>Pass / Fail / Needs verification<br/>What evidence is missing, who provides it, and when to recheck"]
    F --> H
    G --> H
    classDef check fill:#fff3d6,stroke:#b37b17,color:#503a13;
    classDef done fill:#e6f4eb,stroke:#43845b,color:#21422d;
    class B,C,D check;
    class H done;
```

For example: the coordinator sent reminders and reported risks as agreed, but the writer still delivered late. The reminder work can pass while on-time content delivery still fails. If the spreadsheet lost the original deadline, record keeping needs a separate check. **Do not erase a delay by changing the deadline, or introduce new criteria after the fact to penalize past actions.**

[See the inputs and actual outputs from this simulation](../evals/RESULTS.md).

