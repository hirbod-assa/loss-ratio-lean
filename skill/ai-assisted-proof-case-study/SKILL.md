---
name: ai-assisted-proof-case-study
description: Run and report a mathematical research project in which proofs are developed with a panel of AI agents (proposers, adversarial checkers, judge) under a human author's direction, with an error log, numerical checks, optional Lean verification and a report following the nine-item standard of Assa (2026). Use when starting a research question to be attacked with AI agents, when revising a result after a referee's or reader's comment, or when writing the AI-use report of such a paper. Written for mathematical risk management and actuarial science, usable in other areas of mathematics.
---

# AI-assisted proof case study: protocol and reporting

This skill packages the method used in H. Assa, *Reporting AI-Assisted Proofs in Mathematical Risk Management: A
Proposed Standard, with an Axiomatic Characterization of the Loss Ratio as a Case Study* (2026), repository
<https://github.com/hirbod-assa/loss-ratio-lean>. It tells an AI assistant how to organize the work and what to record,
and it tells the human author what decisions remain theirs. It does not make a result correct. Only checking does
that, and the report must say which checks were made.

## 0. Roles and ground rules

- **The author** poses the question, chooses formulations, rejects or accepts AI output, and decides on content.
  Every decision of this kind is recorded (Section 4).
- **The main assistant** organizes the work, runs the panels, drafts text and proofs, writes scripts and Lean code,
  and keeps the records. It never commits, publishes or sends anything without the author's explicit request.
- **Agents** are instances given one role, one task and the shared context. Their output is a *proposal* until it has
  passed the checks in Section 2.
- **Rules for the assistant:**
  - Mark every step not fully proved as `GAP`. Never smooth over a gap in prose.
  - Treat agreement between AI reviews as evidence, not proof.
  - Prefer primary sources. When a fact rests only on a secondary source or on another AI's report, say so in the
    text.
  - When a reader, referee or editor comments, record the comment and how it changed the work.

## 1. Before starting: tier and repository

Decide the tier (Section 5): **(i)** incidental use, **(ii)** assisted proofs, **(iii)** agent-developed proofs. A
project run with this skill is normally tier (iii).

Create a version-controlled repository at the start, and commit at each milestone the author approves:

```
manuscript/         paper source (and supplement)
lean/               formal proofs, if any (lakefile, lean-toolchain pinned)
ai_process/
  panels/           one folder per panel: prompts (the workflow script or the role prompts), outputs, judge report
  scripts/          numerical checks (exact arithmetic where possible), runnable with `python3 -I`
  errors.md         error log (template in Section 4)
  discussions.md    author-assistant discussions that changed the work (template in Section 4)
  status.md         verification status table (template in Section 5)
README.md           what is formalized, how to rebuild, where the records are
```

Remove machine-specific paths and personal data from records before publishing them.

## 2. The work, stage by stage

### 2.1 Frame the question (author)
State the question as a target theorem type, for example "characterize X by necessary and sufficient conditions".
List the known traps: degenerate cases, boundary values, conventions such as 0/0.

### 2.2 Knowledge base
Run one agent per strand of literature. Each returns the exact statements of the results it relies on, with their
hypotheses, a confidence label (high, medium or low) and a note on the source. Merge the returns into one digest that
later agents read in full. Check the statements that carry the weight of the proof against the original papers, or
reprove them. Record which ones were checked.

### 2.3 Proposal panel
Use 3 to 5 proposal agents, each with a distinct **angle**: a different strategy, formulation or level of
generality. One angle should always be *limits and minimality*: what cannot work, and the weakest statement that
does. Every proposal must contain:
- (a) the statement, ready to typeset;
- (b) a proof of necessity;
- (c) a proof of sufficiency;
- (d) a justification in the language of the field;
- (e) a numerical sanity check by script;
- (f) open gaps.

### 2.4 Adversarial check
Give each proposal its own checker agent, instructed to **refute** it and to default to "refuted" when uncertain.
The checker:
- re-derives the necessity and sufficiency proofs;
- recomputes every number;
- tests the degenerate cases named in 2.1;
- looks for circular citations;
- returns: errors found, repairs, and an overall verdict ("survives", "survives with repairs" or "refuted").

### 2.5 Judge
One judge agent ranks the surviving proposals by correctness, scope and elegance. It synthesizes from the winner,
grafts the best parts of the runners-up onto it, collects the impossibility results, and runs its own exact check of
the combined system. Record the judge's report verbatim in `ai_process/panels/`.

### 2.6 Drafting, checking runs and repair
The assistant drafts the full statement and proof. Separate checking runs, each with a specific brief (circularity,
degenerate cases, conventions, scope of claims), report errors. Send the errors back for repair, and repeat until a
round finds no new error. Log every error found (Section 4).

### 2.7 Second provider
Have the proofs reviewed by a model from a different provider. In the case study this found three errors that all
earlier checks had missed. Use the same idea for descriptions of the literature: when two independent AI reports
disagree, go to the primary source.

### 2.8 Numerical checks
Every example and counterexample is recomputed by script, in exact rational arithmetic where possible. Pitfalls seen
in practice:
- Random tests can be vacuous. A test of "the pool of unpriced books is unpriced" never hit the pole with random
  shifts (0 failures out of 2000) and failed at once with the targeted shift. Test at the points where the claim can
  fail.
- Sampling cannot check a "for all c" statement. Replace it with an equivalent finite statement.

### 2.9 Formal verification (encouraged, not required)
Formalize the steps specific to the problem. Take classical results that the library does not cover as explicit
hypotheses. Run the build-and-repair loop: the assistant writes the file, the author builds, and the assistant reads
the log and corrects only proof steps. Before reporting:
- the final file contains no `sorry`, `admit` or added `axiom`;
- `#print axioms` lists only `propext`, `Classical.choice` and `Quot.sound`;
- a clean rebuild from an empty build directory succeeds;
- the compiled file is identical to the published one;
- **fidelity**: a human compares the formal definitions and statements with the paper. The kernel checks the encoded
  proposition, not its meaning. See the Lean community's checklist "Did you prove it?".

If the mathematics is revised after the formal check, say exactly which formulation the check covers.

## 3. Human objections are the most valuable input

In the case study, the decisive steps came from the author:
- the central idea arose from objecting to an AI-drafted formulation that assumed what should have been proved;
- the final axioms came from insisting, after a reader's remark, that no derived quantity appear in an axiom.

The assistant should therefore:
- surface its assumptions, so that the author can object to them;
- when the author proposes an idea, check it carefully, and say plainly if it fails and why (for example, an explicit
  formula that is 0/0 on a degenerate set);
- correct the author's slips, such as an inverted identity, and record the correction;
- record every such exchange as a Discussion (Section 4).

## 3a. Practical advice for proofs with agents

- **Fix the statement before proving.** State all quantifiers, the domain and the conventions. Ask each agent to
  restate the theorem; differences between the restatements expose ambiguities.
- **Give every agent the list of degenerate cases and established facts.** Most errors occur at degenerate cases,
  and the list of facts prevents agents from rediscovering them.
- **Keep one notation file.** Agents drift between sign and shift conventions.
- **Freeze the statement while a proof is checked.** The typical failure is a correct proof of a slightly weaker
  statement. Checkers compare what was proved with what was claimed.
- **Search for counterexamples before proofs.** Ask agents to "try to break it" first.
- **Ask for the dependency structure of a proof**, with the hypotheses of each lemma. Treat "clearly" or "it is easy
  to see" as a gap: expand it, or mark it `GAP`.
- **Give checkers the statement and the proof, not the prover's reasoning**, so that they are not anchored on it.
- **Require concrete objections:** a counterexample or a failing step. Discard vague doubts.
- **Test on small finite models in exact arithmetic**, at the points where the claim can fail.
- **Stop checking only when two consecutive rounds find nothing new.**
- **Check citations that carry weight** against the source, or reprove them.
- **In Lean, formalize the definitions and statements first** and have a human check them before any proof work.
- **Keep the working context in files** (digest, notation, decisions), not in one long session. Restate the key
  definitions at each stage.
- **Record model versions** and rerun the checks after switching models.
- **Keep failed approaches.** They often become impossibility results.
- **Favour diversity of angles over the number of agents.**
- **Ask what a formulation assumes.** A formulation that supplies the key objects by assumption should be challenged.

## 4. Records to keep while working

**Error log entry** (`ai_process/errors.md`), one line per error in AI-generated mathematics:

| Error | Found by | Resolution |
|---|---|---|
| what was claimed, and why it is wrong | which check (agent, run, assistant on rereading, second provider, author) | what was changed, with a pointer to the paper |

**Discussion record** (`ai_process/discussions.md`). Date; the question or objection; what was examined; the
conclusion; what changed in the paper. In the paper, a Discussion is a formal summary in italics, marked
"◇ Discussion", never a transcript. A LaTeX environment for this is in the case study's `preamble.tex`.

**Revision record.** Which comment (reader, referee, editor) prompted the revision; the panel run in response
(prompts, roles, number of agents); the errors it found; what the author decided. Name a commenter only with their
consent; editors and referees are usually anonymous.

## 5. The report: nine items in three tiers

| Item | What to report | Tier | Verifiable |
|---|---|---|---|
| 1. Tools | providers, models and versions, mode of access, dates | i–iii | S/P |
| 2. Division of labour | who posed the question, chose the formulation, decided on content; tasks given to AI | i–iii | S |
| 3. Workflow | agents and sessions, roles, order, review loops, author's interventions | iii | P |
| 4. Knowledge base | how the literature was gathered, confidence labels, statements checked against sources | iii | P |
| 5. Error log | every error in AI-generated mathematics, how found, how resolved | ii–iii | S/P |
| 6. Guardrails | adversarial review, second provider, recomputation, counterexamples, reproved citations | ii–iii | P |
| 7. Formal verification | what was formalized, setting, hypotheses, comparison with the paper | iii (encouraged) | V |
| 8. Verification status | per part: AI-reviewed, human-reviewed, formally checked, unchecked | ii–iii | S/V |
| 9. Records | formal proofs, scripts, process records, in a public repository with history | iii (encouraged) | V |

V: verifiable from public artifacts. P: open to inspection. S: self-declared.

**Verification status table** (`ai_process/status.md` and the paper):

| Part of the paper | AI review | Second provider | Human review | Formal check | Date |
|---|---|---|---|---|---|

## 6. Running the panel in different tools

Ready-made agent definitions for every role in this protocol are in the `agents/` folder of the repository:
proposer, adversarial checker, judge, chair, prover, checking run, literature strand, Lean formalizer, and a prompt
for review by a second provider. The folder also has a context template and a generic panel workflow
(`agents/workflow/proof-panel.js`).

- **Claude Code.** Run each stage as subagents or as a scripted workflow: proposers in parallel, each followed by its
  checker, then the judge. Pass the shared context once and ask for structured output. The case study's workflow
  script is in `ai_process/revision_pureLR_workflow.js` of the repository and can serve as a template.
- **Other assistants.** Run each role as a separate session with the same context document and the role prompt.
  Keep the outputs as files, and let a final session act as the judge.
- **Any tool.** Keep the role prompts, the outputs and the judge's report. They are item 9.

## 7. Limits

- This protocol was distilled from **one** case study. Expect to adapt it.
- It encodes procedure, not judgment. The author's understanding of the problem cannot be delegated.
- Models and tools change quickly. Record the versions used (item 1).
- The skill was drafted by an AI assistant at the author's request. Check it against your own practice before relying
  on it.
