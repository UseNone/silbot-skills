"""Refresh the reviewed portable subset; never reintroduce excluded skills."""
import subprocess
from build_catalog import ROOT, build

PORTABLE = ["algorithmic-art", "canvas-design", "doc-coauthoring", "frontend-design", "internal-comms", "mcp-builder", "skill-creator", "slack-gif-creator", "theme-factory", "webapp-testing"]
subprocess.run(["git", "fetch", "https://github.com/anthropics/skills.git", "main"], cwd=ROOT, check=True)
subprocess.run(["git", "checkout", "FETCH_HEAD", "--", *["skills/" + name for name in PORTABLE]], cwd=ROOT, check=True)
build()
