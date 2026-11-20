export const meta = {
  name: 'reference-solutions',
  description: 'Write and sandbox-verify reference solutions for one slice of benchmark task batches',
  phases: [{ title: 'Solve', detail: 'one agent per batch file; each solution verified against all official tests' }],
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
          status: { type: 'string', enum: ['pass', 'failed'] },
          attempts: { type: 'integer' },
          unique_answer: { type: 'boolean' },
          statement_issue: { type: 'string' },
          notes: { type: 'string' },
        },
        required: ['task_id', 'status', 'attempts', 'unique_answer', 'statement_issue', 'notes'],
      },
    },
  },
  required: ['results'],
}
const names = []
for (let i = args.from; i <= args.to; i++) names.push(`${args.prefix}_${String(i).padStart(2, '0')}`)
phase('Solve')
const out = await parallel(names.map(n => () =>
  agent(
    `Read <repo>/tools/AGENT_BRIEF.md and follow it exactly. ` +
    `Your batch file is <repo>/work/batches/${n}.txt. ` +
    `Report one result per task id in the batch. In "notes" give the algorithm in one short sentence, plus the diagnosis if the task failed.`,
    { label: `solve:${n}`, phase: 'Solve', schema: SCHEMA, model: args.model }
  ).then(r => (r ? { batch: n, results: r.results } : { batch: n, results: null }))
))
const done = out.filter(Boolean)
const flat = done.flatMap(b => b.results || [])
log(`${flat.filter(r => r.status === 'pass').length}/${flat.length} passed; batches without a report: ${done.filter(b => !b.results).map(b => b.batch).join(', ') || 'none'}`)
return { slice: `${args.prefix} ${args.from}-${args.to}`, missing_batches: done.filter(b => !b.results).map(b => b.batch), results: flat }
