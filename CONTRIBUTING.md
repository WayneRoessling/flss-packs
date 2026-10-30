# Contributing a pack, a programme or a protocol

Thank you. Three things first.

1. **It is yours, and you give it.** By opening a pull request you contribute the file under this repository's MIT licence, and you
   confirm that you wrote it or have the right to give it. Put your name in the file's `author` field if you want it shown in FLSS;
   leave it out to stay anonymous. FLSS shows exactly what you put there.
2. **Nothing about a real person.** A pack holds no record of anyone: no figure from your own life, no name of anyone else, no entry.
   A programme holds targets and rules, a protocol holds if-then plans. If you want to share what worked for you, share the plan, not
   the diary.
3. **Nothing clinical.** FLSS never names a condition or a treatment and never gives medical, legal or financial advice. A protocol
   that names a diagnosis, a medicine or a dose is declined. A programme that promises an outcome is declined.

## How

1. Copy the matching example folder (`packs/_example`, `programmes/_example`, `protocols/_example`).
2. Write your file against the schema in `schema/`. The validation workflow runs on every pull request and tells you the first error
   in plain words.
3. Write the `README.md`: who it is for, what it adds, what it asks a person to record.
4. Open the pull request. A reviewer with the matching role reads it (see `REVIEWERS.md`): a pack reviewer for an area pack, a
   library reviewer for a protocol. A pack that carries guidance text or a capture kind also goes to FLSS's clinical adviser, as every
   shipped pack does.
5. The reviewer writes `REVIEW.md` beside your file: who reviewed it, when, and what they checked. Only then does it ship with a
   release.

## What is checked

- The file validates against its schema.
- Every sentence passes FLSS's tone rules: no exclamation mark, no *streak*, no *missed*, no *fail*, no *must* or *should*, no
  condition or treatment named, an invitation rather than an instruction.
- No figure is typed where FLSS would show it as a person's own.
- A programme makes a draft plan a person approves; it never makes a baseline.
- A protocol's pieces are each something a person can keep or drop.

## Attribution

FLSS shows the `author` field as you wrote it, on the pack's card and on anything made from it, and nothing else about you. Changing or
removing it later is one pull request.
