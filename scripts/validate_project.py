#!/usr/bin/env python3
"""Check project structure, not teaching quality. Python 3.9+, standard library only."""

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import unquote, urlsplit

REQUIRED = (
    "SKILL.md", "README.md", "CURRICULUM.md", "CHANGELOG.md", "LICENSE",
    "docs/COACHING.md", "docs/EVIDENCE_AND_REVIEW.md",
    "templates/SESSION.md", "templates/PROGRESS.md", "examples/questions.md",
    "tests/ACCEPTANCE.md", "scripts/validate_project.py", ".gitignore",
)


def validate(root: Path) -> Tuple[List[str], Dict[str, int]]:
    """Return errors and structural counts without network access or file writes."""
    root = root.resolve()
    errors: List[str] = []
    text: Dict[str, str] = {}
    for name in REQUIRED:
        try:
            text[name] = (root / name).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {name}: {exc}")
    if errors:
        return errors, {}

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    for name, body in text.items():
        require(bool(body.strip()), f"Empty file: {name}")
        require("\ufffd" not in body, f"Replacement character in {name}")
        require(body.endswith("\n"), f"Missing final newline: {name}")
        require(not re.search(r"[\t ]+$", body, re.M), f"Trailing whitespace: {name}")

    front = re.match(r"\A---\n(.*?)\n---\n", text["SKILL.md"], re.S)
    require(front is not None, "SKILL.md must start with YAML-style front matter")
    version = re.search(r"^version: (\d+\.\d+\.\d+)$", front.group(1), re.M) if front else None
    require(version is not None, "SKILL.md must declare a semantic version")
    if version:
        value = version.group(1)
        require(f"v{value}" in text["README.md"], "README version does not match SKILL")
        require(f"## {value}" in text["CHANGELOG.md"], "CHANGELOG version does not match SKILL")
        for name in ("templates/SESSION.md", "templates/PROGRESS.md"):
            require(f"template_version: {value}" in text[name], f"Template version mismatch: {name}")

    skill = text["SKILL.md"]
    for marker in ("10 轮有效互动", "10–14", "30 次", "3–5", "用户可随时", "AI 构造案例",
                   "不擅自", "in_progress", "paused", "ended_early", "completed", "私有位置"):
        require(marker in skill, f"Missing core rule marker in SKILL: {marker}")

    units = re.findall(r"^\| (\d{2}) \|", text["CURRICULUM.md"], re.M)
    require(units == [f"{i:02d}" for i in range(1, 31)], "Curriculum must contain units 01–30 exactly once, in order")
    stages = re.findall(r"^\| (S[1-6]) ", text["CURRICULUM.md"], re.M)
    require(stages == [f"S{i}" for i in range(1, 7)], "Curriculum must contain stages S1–S6")

    examples = text["examples/questions.md"]
    question_ids = re.findall(r"^## (Q\d{2}) ", examples, re.M)
    require(question_ids == [f"Q{i:02d}" for i in range(1, 9)], "Examples must contain Q01–Q08")
    for block in re.split(r"(?=^## Q\d{2} )", examples, flags=re.M)[1:]:
        for marker in ("【AI 构造案例】", "**你要决定：**", "**训练价值：**"):
            require(marker in block, f"Example missing {marker}: {block.splitlines()[0]}")

    cases = re.findall(r"^\| (T\d{2}) \|", text["tests/ACCEPTANCE.md"], re.M)
    require(cases == [f"T{i:02d}" for i in range(1, 17)], "Acceptance scenarios must contain T01–T16")
    for name, fields in {
        "templates/SESSION.md": ("session_id", "curriculum_unit", "status", "completed_rounds", "saved_location"),
        "templates/PROGRESS.md": ("current_phase", "current_unit", "completed_standard_sessions", "saved_location"),
    }.items():
        for field in fields:
            require(re.search(rf"^{field}: null$", text[name], re.M) is not None,
                    f"Public template must leave {field} unset: {name}")

    for pattern in ("private/", "sessions/", "progress/", "*.private.md", ".env"):
        require(pattern in text[".gitignore"].splitlines(), f"Missing privacy ignore pattern: {pattern}")

    link_count = 0
    for name, body in text.items():
        if not name.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", body):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            link_count += 1
            destination = ((root / name).parent / unquote(url.path)).resolve()
            require(destination.is_relative_to(root) and destination.is_file(),
                    f"Broken or out-of-project relative link in {name}: {target}")

    try:
        ast.parse(text["scripts/validate_project.py"])
    except SyntaxError as exc:
        errors.append(f"Validator syntax error: {exc}")

    return errors, {"files": len(text), "units": len(units), "questions": len(question_ids),
                    "acceptance_scenarios": len(cases), "relative_links": link_count}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, counts = validate(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: " + ", ".join(f"{name}={value}" for name, value in counts.items()))
    print("Static checks only. Conversation behavior and learning outcomes are not validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
