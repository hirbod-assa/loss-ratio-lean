export const meta = {
  name: 'proof-panel',
  description: 'Proof panel: proposers on distinct angles, one adversarial checker per proposal, a judge, and a chair note',
  whenToUse: 'Attack a precisely stated target with several independent proposals, refute each, and synthesize the best result for the author',
  phases: [
    { title: 'Propose', detail: 'one proposer per angle' },
    { title: 'Refute', detail: 'one adversarial checker per proposal' },
    { title: 'Judge', detail: 'rank, synthesize, check independently' },
    { title: 'Chair', detail: 'note to the author' },
  ],
}

// Usage (Claude Code): fill in the context file, then run this workflow with
//   args = { context: 'path/to/context.md', scratch: 'ai_process/panels/<run>', angles: [ {key, text}, ... ],
//            agentsDir: 'path/to/agents' }
// With agentsDir, each agent reads its role file from that folder, so nothing needs to be installed. Without it,
// the agent files must be installed in .claude/agents/ (or ~/.claude/agents/) BEFORE the session starts, since
// Claude Code reads agent definitions at start-up.
// Generic template distilled from the panel of the case study (ai_process/revision_pureLR_workflow.js).

const A = args || {}
const CONTEXT = `Read the problem context file ${A.context} in full before doing anything else; it fixes the setting, target, established facts, traps, the author's constraints and the notation. Scratch files go under ${A.scratch}/<your-label>/. Never edit the draft, never commit or push.`
const ANGLES = A.angles || []
// Role instructions: read from agentsDir if given, otherwise use the installed agent type of the same name.
const role = (name) => A.agentsDir
  ? { pre: `Your role and instructions are in the file ${A.agentsDir}/${name}.md. Read it first (ignore its YAML header) and follow it exactly.\n\n`, opts: {} }
  : { pre: '', opts: { agentType: name } }
const R = { proposer: role('proof-proposer'), checker: role('proof-adversarial-checker'), judge: role('proof-judge'), chair: role('proof-chair') }
if (!ANGLES.length) throw new Error('args.angles must list the angles, each {key, text}; include one angle on limits and minimality')

const PROPOSAL = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    statement: { type: 'string', description: 'LaTeX-ready statement' },
    necessity: { type: 'string' },
    sufficiency: { type: 'string', description: 'with explicit treatment of every degenerate case in the context' },
    justification: { type: 'string' },
    numerical_check: { type: 'string', description: 'script path and output; targeted tests at the failure points' },
    gaps: { type: 'array', items: { type: 'string' }, description: 'GAP items and impossibility results' },
  },
  required: ['name', 'statement', 'necessity', 'sufficiency', 'justification', 'numerical_check', 'gaps'],
}
const VERDICT = {
  type: 'object',
  properties: {
    respects_constraints: { type: 'boolean' },
    proves_stated_claim: { type: 'boolean', description: 'false if the proof establishes a different (e.g. weaker) statement' },
    necessity_ok: { type: 'boolean' },
    sufficiency_ok: { type: 'boolean' },
    counterexample: { type: 'string' },
    errors: { type: 'array', items: { type: 'string' } },
    repairs: { type: 'array', items: { type: 'string' } },
    overall: { type: 'string', enum: ['survives', 'survives with repairs', 'refuted'] },
    notes: { type: 'string' },
  },
  required: ['respects_constraints', 'proves_stated_claim', 'necessity_ok', 'sufficiency_ok', 'counterexample', 'errors', 'repairs', 'overall', 'notes'],
}

const results = await pipeline(
  ANGLES,
  (a) => agent(`${R.proposer.pre}${CONTEXT}\n\nYour angle: ${a.text}\n\nReturn your best single proposal in the structured format.`,
    { label: `propose:${a.key}`, phase: 'Propose', schema: PROPOSAL, ...R.proposer.opts }),
  (p, a) => p && agent(`${R.checker.pre}${CONTEXT}\n\nRefute the following proposal.\n\nPROPOSAL:\n${JSON.stringify(p, null, 2)}`,
    { label: `refute:${a.key}`, phase: 'Refute', schema: VERDICT, ...R.checker.opts })
    .then(v => ({ angle: a.key, proposal: p, verdict: v })),
)
const ok = results.filter(Boolean)
log(`${ok.length}/${ANGLES.length} proposals went through proposal and refutation`)

phase('Judge')
const report = await agent(`${R.judge.pre}${CONTEXT}\n\nJudge the panel. Write your report to ${A.scratch}/judge_report.md as well as returning it.\n\nPANEL RESULTS:\n${JSON.stringify(ok, null, 2)}`,
  { label: 'judge', phase: 'Judge', ...R.judge.opts })

phase('Chair')
const note = await agent(`${R.chair.pre}${CONTEXT}\n\nWrite the chair's note to the author on this panel.\n\nJUDGE REPORT:\n${report}\n\nPANEL RESULTS:\n${JSON.stringify(ok, null, 2)}`,
  { label: 'chair', phase: 'Chair', ...R.chair.opts })

return { note, report, results: ok }
