"""Read LiveCodeBench `code_generation_lite` rows. The files are downloaded data: no code in
them is executed, and the pickled private tests are decoded with an unpickler that refuses
every global (the payload is a plain str)."""

import base64
import io
import json
import pickle
import zlib
from pathlib import Path

RELEASE_V6_FILES = ("test.jsonl", "test2.jsonl", "test3.jsonl", "test4.jsonl", "test5.jsonl", "test6.jsonl")


class _NoGlobals(pickle.Unpickler):
    def find_class(self, module, name):
        raise pickle.UnpicklingError(f"refusing global {module}.{name}")


def decode_private(blob: str) -> list:
    try:
        return json.loads(blob)
    except Exception:
        raw = zlib.decompress(base64.b64decode(blob.encode("utf-8")))
        obj = _NoGlobals(io.BytesIO(raw)).load()
        if not isinstance(obj, str):
            raise ValueError("unexpected private test payload")
        return json.loads(obj)


def iter_rows(raw_dir: str | Path):
    """Yield every problem of release_v6, in file order."""
    for name in RELEASE_V6_FILES:
        with open(Path(raw_dir) / name, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    row = json.loads(line)
                    row["_source_file"] = name
                    yield row
