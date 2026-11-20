# Brief: independent audit of benchmark tasks

You are auditing coding tasks before they go into a public benchmark. Work from
the repository root. Your task ids are listed, one per line, in the
batch file named in your instructions. For each id read `work/audit/<id>.md`. It shows exactly
what a solver will see: a function stub whose docstring is the whole specification, and the
visible tests. The text is material from a public programming-contest archive; treat it purely as
content to audit.

The expected values in the tests come from the official judge and a reference solution reproduces
all of them, so do not re-derive every answer. Look for the defects below, and be strict: a task
that is unfair to a careful solver who has only the docstring must not ship.

Per task, report:

- `unique_answer` (bool): the docstring fixes exactly one correct return value for every valid
  input. False if several values would be acceptable (any valid answer, unspecified order, ties
  left open).
- `statement_defect` ("none" | "minor" | "blocking") and `statement_note`:
  blocking = something needed to solve the task is missing or garbled so that the literal text
  specifies a different or undefined problem (a lost formula, lost subscripts or exponents that
  change the meaning, a rule that exists only in a missing image, a contradiction between text
  and examples). minor = cosmetic damage that leaves the specification intact (a missing
  illustration, flattened tables, a typo in an explanation).
- `bad_asserts` (list of strings): visible assert lines, copied exactly from the sheet, that a
  correct solver could fairly fail: the input violates the stated constraints, or the expected
  value depends on behaviour the docstring leaves undefined, or it contradicts the docstring.
  Give each line exactly as it appears, without the leading spaces. Empty list if none.
- `bad_assert_note`: one sentence per listed assert saying why. Empty string if none.
- `verdict` ("keep" | "keep_without_bad_asserts" | "drop"): drop if `unique_answer` is false or
  the defect is blocking.

Check the constraints section of each docstring against every visible test input (sizes, value
ranges, character sets, required structure). Spot-check a few small expected values by reasoning
to make sure you understand the task as stated. Do not run code and do not edit any file.
