"""Build the public catalog from this curated checkout, without dependencies."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"claude-api", "academy-guide", "brand-guidelines", "web-artifacts-builder", "docx", "pdf", "pptx", "xlsx", "discernment-nudge"}

def metadata(text, key, fallback):
    if not text.startswith("---\n"):
        return fallback
    lines = text.split("---", 2)[1].splitlines()
    for index, line in enumerate(lines):
        if line.startswith(key + ":"):
            value = line.split(":", 1)[1].strip()
            if value in {">", "|", ">-", "|-"}:
                parts = []
                for continuation in lines[index + 1:]:
                    if continuation and not continuation[0].isspace():
                        break
                    parts.append(continuation.strip())
                return " ".join(parts).strip()
            return value.strip("\"'")
    return fallback

def build():
    entries = []
    for directory in sorted((ROOT / "skills").iterdir()):
        skill = directory / "SKILL.md"
        if not skill.is_file():
            continue
        content = skill.read_text(encoding="utf-8")
        if directory.name in EXCLUDED or "license: Proprietary" in content:
            raise ValueError("Excluded skill reintroduced: " + directory.name)
        files = []
        for file in sorted(directory.rglob("*")):
            if file.is_file() and not file.is_symlink():
                data = file.read_bytes()
                try:
                    data.decode("utf-8")
                    data = data.replace(b"\r\n", b"\n")
                except UnicodeDecodeError:
                    pass
                files.append({"path": file.relative_to(directory).as_posix(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        entries.append({"id": directory.name, "name": metadata(content, "name", directory.name),
            "description": metadata(content, "description", ""), "path": skill.relative_to(ROOT).as_posix(),
            "origin": "silbot" if (directory.name.startswith("learn-from-") or directory.name == "write-like-me") else "anthropics/skills",
            "revision": hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest(), "files": files})
    (ROOT / "catalog.json").write_text(json.dumps({"version": 1, "repository": "UseNone/silbot-skills", "skills": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(entries)} skills")

if __name__ == "__main__":
    build()
