# The assistant's tools

**What they are** (ADR-FLSS-019; CD-FLSS-039; `01_impl/src/backend/contexts/assistant_access/tools.yaml`). Six read-only tools a
person's own AI assistant may call over MCP (Streamable HTTP, JSON-RPC: `initialize`, `ping`, `tools/list`, `tools/call`), at
`POST /mcp` on the person's install, with a personal access token the person makes in Settings › Assistant access. A token is
capped at a tier the person chooses, **ST0 to ST2 and never above**: an assistant is never given the person's own words, a mood, a
journal entry, a note, a person, a calendar title, a place, a transaction or the vault. A field above the cap is left out and
counted. In a crisis pause every tool answers with the reviewed help text and no data.

| Tool | First tier | Arguments | Answers |
|---|---|---|---|
| `flss_today` | 1 | none | today's plans and their slots, by area |
| `flss_areas` | 1 | none | the areas, their kinds, postures and seasons, and each one's status in words |
| `flss_area` | 2 | `area_id` (uuid) | one area: its measures, its plan, its sub-areas, its status |
| `flss_measure` | 2 | `measure_id` (uuid), `days` (7 to 90, default 28) | one measure: its recent values, its estimate, its projection in words |
| `flss_week_plan` | 1 | `date` (YYYY-MM-DD, optional) | the week's planned slots by day |
| `flss_day` | 1 | `date` (optional) | the day's planned and recorded time by area, and the interruptions count |

Every call is audited to the person (the tool, how many fields were kept and left out, the tiers returned) and rate-limited
(60 a minute). A tool runs in a database transaction that is read-only, so nothing it does can write. The full input schemas are in
`tools.yaml`, which `tools/list` serves verbatim.

## Connecting an assistant

Settings › Assistant access › *Connect your assistant* shows the address, the header and the steps for the assistants that connect
by URL and bearer token. On a person's own machine the API listens on the loopback only, so the assistant runs there too.
