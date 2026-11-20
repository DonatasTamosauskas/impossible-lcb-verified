export const meta = {
  name: 'task-audit',
  description: 'Independent audit of benchmark tasks: answer uniqueness, statement defects, unfair visible tests',
  phases: [{ title: 'Audit', detail: 'one agent per batch of task sheets' }],
}
const SCHEMA = {
  type: 'object',
  properties: {
    results: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          task_id: { type: 'string' },
          unique_answer: { type: 'boolean' },
          statement_defect: { type: 'string', enum: ['none', 'minor', 'blocking'] },
          statement_note: { type: 'string' },
          bad_asserts: { type: 'array', items: { type: 'string' } },
          bad_assert_note: { type: 'string' },
          verdict: { type: 'string', enum: ['keep', 'keep_without_bad_asserts', 'drop'] },
        },
        required: ['task_id', 'unique_answer', 'statement_defect', 'statement_note', 'bad_asserts', 'bad_assert_note', 'verdict'],
      },
    },
  },
  required: ['results'],
}
const names = []
for (let i = args.from; i <= args.to; i++) names.push(`${args.prefix}_${String(i).padStart(2, '0')}`)
phase('Audit')
const out = await parallel(names.map(n => () =>
  agent(
    `Read <repo>/tools/AUDIT_BRIEF.md and follow it exactly. ` +
    `Your batch file is <repo>/work/audit_batches/${n}.txt. ` +
    `Report one result per task id in the batch.`,
    { label: `audit:${n}`, phase: 'Audit', schema: SCHEMA, model: args.model }
  ).then(r => ({ batch: n, results: r ? r.results : null }))
))
const done = out.filter(Boolean)
const flat = done.flatMap(b => b.results || [])
log(`${flat.length} audited; keep ${flat.filter(r => r.verdict === 'keep').length}, trim ${flat.filter(r => r.verdict === 'keep_without_bad_asserts').length}, drop ${flat.filter(r => r.verdict === 'drop').length}`)
return { missing_batches: done.filter(b => !b.results).map(b => b.batch), flagged: flat.filter(r => r.verdict !== 'keep' || r.statement_defect !== 'none'), n: flat.length }
