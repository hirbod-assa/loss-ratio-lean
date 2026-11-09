# Agents for AI-assisted proofs

These are the agent roles designed for the case study in H. Assa, *Reporting AI-Assisted Proofs in Mathematical
Risk Management: A Proposed Standard, with an Axiomatic Characterization of the Loss Ratio as a Case Study*
(2026), written in a form that other researchers can reuse. The protocol around them, and the records to keep, are
in the skill `skill/ai-assisted-proof-case-study/SKILL.md`.

## Format

Each agent is one Markdown file with a short YAML header and a body:

```markdown
---
name: proof-adversarial-checker          # identifier used to call the agent
description: When to use this agent ...  # the assistant uses this to decide when to call it
tools: Read, Grep, Glob, Bash, Write     # optional: tools the agent may use (omit to allow all)
---

Instructions to the agent (its system prompt): role, inputs, checks, output format, rules.
```

This is the format of Claude Code subagents. The body is plain text, so with any other assistant it can be pasted
as the role prompt of a separate session.

## The agents

| File | Role | Stage |
|---|---|---|
| `proof-literature-strand.md` | exact statements of the literature, with confidence labels | knowledge base |
| `proof-proposer.md` | statement and proofs from one assigned angle | proposal panel |
| `proof-adversarial-checker.md` | tries to refute one proposal; structured verdict | adversarial check |
| `proof-judge.md` | ranks, synthesizes, collects impossibility results, independent exact check | judge |
| `proof-chair.md` | neutral note to the author with the decisions to take | end of a panel |
| `proof-prover.md` | full statement and complete proof of an accepted formulation | drafting |
| `proof-checking-run.md` | review against one brief; repeated until two rounds find nothing new | repair loop |
| `lean-formalizer.md` | Lean 4 formalization with the build-and-repair loop and checks | formal verification |
| `second-provider-review.md` | prompt for an independent review by a model of another provider | second provider |

`context-template.md` is the shared problem context that every agent reads first: setting, target, established
facts, traps, the author's constraints, notation, files and deliverable. Filling it in well matters more than any
other step.

`workflow/proof-panel.js` runs a whole panel in Claude Code: the proposers in parallel, each followed by its own
checker, then the judge and the chair. Its arguments are the context file, a scratch folder, the list of angles
(include one angle on the limits of what can be achieved) and, optionally, `agentsDir`, the path of this folder.

## Use

**Claude Code.**
1. Copy `context-template.md` to your project and fill it in.
2. Either install the agent files in `.claude/agents/` (or `~/.claude/agents/`) and **start a new session**, since
   Claude Code reads agent definitions at start-up; or skip installation and pass `agentsDir`, so that each agent
   reads its role file directly.
3. Ask the assistant to use a given agent for a task, or run the workflow with your angles, for example:

```
args = { context: "notes/context.md", scratch: "ai_process/panels/run1", agentsDir: "agents",
         angles: [ { key: "direct", text: "..." }, { key: "limits", text: "Limits and minimality: ..." } ] }
```

**Other assistants.** Open one session per role. Give it the filled context file and the body of the agent file as
its instructions, and save each output as a file. Pass the proposals and verdicts to the judge session.

**Records.** Keep the context file, the prompts, the outputs and the judge's report in `ai_process/`. They are
item 9 of the reporting standard.

## Worked example

`examples/two-point-choquet/` is a test run of the whole panel on a problem with a known answer: the functionals on a
two-point space that are cash additive, comonotonic additive, monotone and law invariant are exactly
`a max + (1 - a) min` with `a` in [0, 1]. It contains:
- the context file;
- the proposals and the adversarial verdicts;
- the judge's report and the chair's note;
- the check scripts, which run with `python3 -I`.

Six agents took about eight minutes. The panel found the answer and an independence witness for each axiom. A
checker found three presentation errors, and the chair flagged the one step that needs the axiom of choice as a
`GAP`. The test also showed that agent files installed during a session are not picked up, which is why `agentsDir`
exists.

## Limits

- The roles were designed for one case study, a characterization theorem in actuarial mathematics. Adapt the
  checks to your field.
- An agent's verdict is evidence, not proof. The author decides, and the report says which checks were made.
- Tool names and the workflow syntax are those of Claude Code in November 2026 and may change.
