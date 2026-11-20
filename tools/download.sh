#!/bin/sh
# Fetch LiveCodeBench code_generation_lite (release_v6, ~4.5 GB) at the pinned revision and check hashes.
set -eu
REV=0fe84c3912ea0c4d4a78037083943e8f0c4dd505
mkdir -p data/lcb_raw
cd data/lcb_raw
for f in test.jsonl test2.jsonl test3.jsonl test4.jsonl test5.jsonl test6.jsonl; do
  [ -f "$f" ] || curl -L --fail -o "$f" "https://huggingface.co/datasets/livecodebench/code_generation_lite/resolve/$REV/$f"
done
shasum -a 256 -c ../../curation/lcb_raw.sha256
