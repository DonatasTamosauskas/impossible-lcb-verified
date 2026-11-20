"""Runs inside the sandbox container: call the solution on every official test case."""

import json
import signal
import sys
import time
import traceback

PER_TEST_SECONDS = int(sys.argv[1]) if len(sys.argv) > 1 else 10


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def short(v, n=300):
    s = repr(v)
    return s if len(s) <= n else s[:n] + f"... ({len(s)} chars)"


def main():
    spec = json.load(open("/w/tests.json"))
    out = {"status": "FAIL", "passed": 0, "total": len(spec["cases"])}
    try:
        ns = {"__name__": "solution"}
        exec(compile(open("/w/solution.py").read(), "solution.py", "exec"), ns)
        fn = ns[spec["entry_point"]]
    except BaseException:
        out["error"] = "solution failed to load:\n" + traceback.format_exc()[-1500:]
        print(json.dumps(out)); return
    signal.signal(signal.SIGALRM, _alarm)
    slowest, t_all = 0.0, time.time()
    for i, (args, expected) in enumerate(spec["cases"]):
        t0 = time.time()
        fail = None
        signal.alarm(PER_TEST_SECONDS)
        try:
            got = fn(*args)
            signal.alarm(0)
            if type(got) is not type(expected) or got != expected:
                fail = {"got": short(got), "got_type": type(got).__name__}
        except _Timeout:
            fail = {"error": f"time limit exceeded ({PER_TEST_SECONDS}s)"}
        except BaseException:
            signal.alarm(0)
            fail = {"error": traceback.format_exc()[-1200:]}
        slowest = max(slowest, time.time() - t0)
        if fail:
            out["first_failure"] = {"case_index": i, "args": short(args), "expected": short(expected), **fail}
            break
        out["passed"] += 1
    if out["passed"] == out["total"]:
        out["status"] = "PASS"
    out["slowest_test_seconds"] = round(slowest, 2)
    out["total_seconds"] = round(time.time() - t_all, 2)
    print(json.dumps(out))


main()
