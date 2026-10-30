"""Validate contributed packs, programmes and protocol sets against FLSS's published schemas and tone rules (PLAN-FLSS-006 Phase 2;
CAP-60.1; the public repository's validation workflow). It reads files, prints the first thing wrong with each, and writes nothing.

    python scripts/open_model_check.py <folder or file> ...        # from FLSS's repository, with its environment
    python tools/open_model_check.py packs programmes protocols    # in the public repository, with jsonschema and pyyaml alone

A file's kind is read from its ``kind`` key (``programme`` or ``protocol``); a file with none is an area pack. Outside FLSS's
repository the tone rules are not available and only the schemas are checked; the reviewer runs the tone check in FLSS.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

HERE = Path(__file__).resolve().parent
SCHEMA_DIRS = (HERE.parent / "01_impl" / "packs" / "schema", HERE.parent / "schema", HERE / "schema")
HUMAN_KEYS = ("title", "summary", "name", "author", "if_text", "then_text", "text", "label", "words")


def _schema(kind: str) -> dict:
    name = {"area": "area_pack", "programme": "programme", "protocol": "protocol"}[kind]
    for d in SCHEMA_DIRS:
        p = d / f"{name}.schema.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    raise SystemExit(f"no schema folder found beside {HERE}")


def _tone():
    try:
        sys.path.insert(0, str(HERE.parent / "01_impl" / "src"))
        from backend.contexts.intervention_policy import gate  # noqa: PLC0415

        return gate.check_tone
    except Exception:  # noqa: BLE001 — outside FLSS's repository the tone rules are not there
        return None


def _strings(node, out: list[str]) -> None:
    if isinstance(node, dict):
        for k, v in node.items():
            if k in HUMAN_KEYS and isinstance(v, str):
                out.append(v)
            else:
                _strings(v, out)
    elif isinstance(node, list):
        for v in node:
            _strings(v, out)


def check(path: Path, tone) -> list[str]:
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as exc:
        return [f"not YAML: {exc}"]
    if not isinstance(doc, dict):
        return ["not a document"]
    kind = doc.get("kind") if doc.get("kind") in ("programme", "protocol") else "area"
    errors = [f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}"
              for e in jsonschema.Draft202012Validator(_schema(kind)).iter_errors(doc)]
    words: list[str] = []
    _strings(doc, words)
    for w in words:
        if "!" in w:
            errors.append(f"an exclamation mark: {w[:60]!r}")
        if re.search(r"\b(streak|missed|fail(ed|ure)?|must|should)\b", w, re.IGNORECASE):
            errors.append(f"a word the tone rules refuse: {w[:60]!r}")
        if tone is not None:
            r = tone(w)
            if not r.passed:
                errors.append(f"tone: {w[:60]!r}: {r.findings[0]['rule']} {r.findings[0].get('token')}")
    return errors


def main(argv: list[str]) -> int:
    tone = _tone()
    files: list[Path] = []
    for arg in argv or ["."]:
        p = Path(arg)
        files += sorted(p.rglob("*.yaml")) if p.is_dir() else [p]
    bad = 0
    for f in files:
        if f.name in ("REVIEW.yaml", "REVIEWED.yaml") or f.name.startswith("_"):
            continue
        errors = check(f, tone)
        print(f"{'ok  ' if not errors else 'FAIL'} {f}" + (f": {errors[0]}" if errors else ""))
        bad += bool(errors)
    print(f"{len(files) - bad} ok, {bad} with something wrong" + ("" if tone else " (schemas only: the tone rules are not here)"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
