"""Run untrusted Python in a throwaway container: no network, non-root, read-only root."""

import subprocess
import uuid

IMAGE = "python:3.11-slim@sha256:9c900dea9e8fb7e16277c179b555cc72d29a352dbc33cff48ad5a0412fd5bfc7"


def docker_run(cmd: list[str], mounts: dict[str, str] | None = None, stdin: str | None = None,
               timeout: int = 60, memory: str = "2g") -> subprocess.CompletedProcess:
    name = "ilcb_" + uuid.uuid4().hex[:12]
    argv = ["docker", "run", "--rm", "-i", "--name", name, "--network", "none",
            "--memory", memory, "--memory-swap", memory, "--cpus", "1", "--pids-limit", "128",
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges", "--read-only",
            "--tmpfs", "/tmp:rw,nosuid,nodev,size=64m", "--user", "65534:65534",
            "--env", "PYTHONIOENCODING=utf-8", "--env", "PYTHONDONTWRITEBYTECODE=1"]
    for host, guest in (mounts or {}).items():
        argv += ["-v", f"{host}:{guest}:ro"]
    argv += [IMAGE, *cmd]
    try:
        return subprocess.run(argv, input=stdin, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        subprocess.run(["docker", "kill", name], capture_output=True)
        return subprocess.CompletedProcess(argv, 124, "", f"sandbox wall-clock limit ({timeout}s) exceeded")
