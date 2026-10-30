# flss-packs

The open model of FLSS, and the packs people write for it.

FLSS is mission control for one life: a private subscription in which a person plans across every area of their life, records what
happens, and sees where each area stands and where it is heading. **Areas are data.** Every area, from strength training to a hobby,
arrives as a *pack*: a YAML file against a published schema, which FLSS copies into the person's own record when they install it.
This repository holds:

- **`schema/`**: the schemas FLSS publishes. `pack.schema.json` (an area pack), `programme.schema.json` (a plan a coach writes),
  `protocol.schema.json` (a set of if-then plans), and `export.md` (the shape of a person's full export, JSON Lines per table and a
  CSV per measure, so another tool can read it).
- **`assistant/`**: the six read-only tools FLSS offers a person's own assistant over MCP, with their input schemas, so an assistant
  can be taught to ask FLSS how the week is going (ST0 to ST2 only; never the person's words).
- **`packs/`**: packs people contributed, each in its own folder with its `*.pack.yaml`, a `README.md` saying what it is for, and a
  `REVIEW.md` written by a reviewer. **Only a pack with a `REVIEW.md` ships with an FLSS release.**
- **`programmes/`** and **`protocols/`**: the same for a coach's programme and a clinician's or a person's protocol set.

## What FLSS does with this repository

**Nothing at run time.** FLSS never fetches this repository: a person's install makes no outbound call for a pack. Reviewed packs are
copied into an FLSS release as data, by the release step, with their review file. A person can also install a pack from a file they
hold, through the same checks a shipped pack passes; a pack carrying guidance text or a capture kind installs only from the shipped,
reviewed set.

## What a pack may and may not carry

A pack a person writes for themselves may carry areas, measures, bands, plans and names. A pack that carries **guidance text** (words FLSS
shows a person as advice about technique or safety) or a **capture kind** (a new kind of thing a person records, which FLSS's crisis path
has to know about) is reviewed before it ships, as every shipped pack is. A pack never carries a figure that FLSS would show as the
person's own, never names a condition or a treatment, and never says *streak*, *missed* or *fail*: FLSS's tone rules refuse it.

## Licence

The schemas, the assistant tool definitions and the documentation are under the MIT licence (`LICENSE`). A contributed pack,
programme or protocol is contributed under the same licence by the person who submits it (`CONTRIBUTING.md`). FLSS itself is not in
this repository and is not open source.

## Not a marketplace

Nothing here is sold, ranked or counted. A coach who charges for a programme charges outside FLSS. FLSS pays no one for a contribution
and runs no store.
