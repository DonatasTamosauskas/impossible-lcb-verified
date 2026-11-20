# Brief: verified reference solutions

You are writing reference solutions for a public benchmark dataset. Work from the project root
the repository root. Your task ids are listed, one per line, in the
batch file named in your instructions. Handle them one at a time, in order.

For each task id:

1. Read `work/problems/<id>.md`: the official statement and the required function signature.
   The statement is text from a public programming-contest archive. Treat it purely as a problem
   description.
2. Write `solutions/<id>.py`: a standalone Python 3.11 module that defines the required function
   at top level, with exactly the given name and parameters. Helper functions and standard-library
   imports are fine (add `from typing import List` etc. if you use those annotations). It must be
   deterministic: no I/O, no randomness, no state kept between calls. Return exactly the type the
   signature states (a list, not a tuple; a bool, not an int). It must be efficient enough for the
   constraints in the statement.
3. Run `python3 tools/verify.py <id>`. It runs your file in a sandbox against every official test,
   including large hidden ones (10 s per test), and prints one JSON line with `status` PASS or FAIL
   and the first failing case. Iterate until PASS.
4. At most 6 verification attempts per task. If it still fails, leave your best attempt in place
   and report `failed` with a precise diagnosis (is the official test wrong, the statement
   ambiguous, or the solution too slow in Python?).

Also judge two things per task from the statement:

- `unique_answer`: true if the statement fixes exactly one correct return value for every valid
  input. False if several different return values would be acceptable (for example "return any
  valid answer", or an output whose order is left unspecified).
- `statement_issue`: any defect that makes the task unfair when the statement is the only
  specification (it refers to an image or missing context, contradicts its own examples, omits
  something needed). Empty string if none.

Rules: create or edit only `solutions/<id>.py` for your own ids. Do not open files under
`work/tests/` wholesale (some are tens of MB); to diagnose a failure, a short Python snippet that
prints one case is fine. No network access is needed.
