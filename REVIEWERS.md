# Reviewers

A reviewer reads what people contribute and writes the `REVIEW.md` that lets it ship. A reviewer never sees anyone's FLSS record: the
roles here are roles on *content*, granted by FLSS's operator, and nothing else (FLSS's ADR-FLSS-007).

| Role | Reads | Who |
|---|---|---|
| `pack_review` | Area packs and programmes: the schema, the tone, that nothing is clinical, that a programme makes a draft and never a baseline | *to be named by the owner* |
| `library_review` | Protocols and techniques for FLSS's coping library: the tone, the evidence grade claimed, that nothing names a condition or a treatment, that each piece is something a person can keep or drop | *to be named by the owner* |
| the clinical adviser | Anything that reaches FLSS's crisis path: a capture kind, guidance text. She is the only reviewer of the crisis path, and her review is recorded in FLSS, not here | Polly Timberlake |

A reviewer may put their name on what they reviewed, in `REVIEW.md`; FLSS shows it beside the pack if they do.

## Writing a REVIEW.md

```
reviewer: <name, or "anonymous reviewer">
role: pack_review | library_review
date: YYYY-MM-DD
checked:
  - the file validates against the schema
  - every sentence passes the tone rules
  - nothing names a condition, a treatment, a medicine or a dose
  - no figure is typed where FLSS would show it as a person's own
  - <what else you looked at>
decision: approved | changes requested
notes: <one or two lines, if any>
```
