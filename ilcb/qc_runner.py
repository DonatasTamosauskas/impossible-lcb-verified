"""Inside the sandbox: run each program in its own interpreter, report exit code and failing line."""

import json
import re
import subprocess
import sys

progs = json.load(open("/w/programs.json"))
out = {}
for name, src in progs.items():
    try:
        r = subprocess.run([sys.executable, "-I", "-c", src], capture_output=True, text=True, timeout=60)
        code, err = r.returncode, r.stderr
    except subprocess.TimeoutExpired:
        code, err = 124, "timeout"
    line = None
    m = re.findall(r'File "<string>", line (\d+), in check', err)
    if m:
        line = src.split("\n")[int(m[-1]) - 1].strip()
    last = err.strip().splitlines()[-1][:200] if err.strip() else ""
    out[name] = {"exit": code, "failing_line": line, "last": last}
print(json.dumps(out))
