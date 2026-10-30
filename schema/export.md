# A person's full export

**What it is** (ADR-FLSS-006 §5; CD-FLSS-022 §4.6; `01_impl/src/backend/platform/export.py`). One zip file the signed-in person
downloads from Settings › Your record. It holds everything, ST3 and ST4 included, in open formats, so that no connector, vendor or
FLSS itself can hold the record captive. It imports again into an empty FLSS account and reproduces the same charts.

## Layout

```
manifest.json
<schema>.<table>.jsonl       one file per record table, one JSON object per line, every column as stored
csv/<measure key>.csv        one file per measure: local_date, observed_at, value, unit, source, is_void, supersedes_id, reason, tier
```

## `manifest.json`

| Key | Meaning |
|---|---|
| `format` | `flss-export` |
| `format_version` | `1` |
| `schema_version` | the database migration the export was made at (an Alembic revision id) |
| `packs` | `[{pack_id, version}]`, every pack installed |
| `account` | `{time_zone, display_unit, look, evening_hearth}` |
| `deployment_mode` | `local` or `hosted` |
| `catalogue_version` | the settings catalogue's version |
| `tiers` | `{tier: rows}`, how many rows at each sensitivity tier (ST0 to ST4) |
| `not_exported` | `{table: reason}`, the operational tables that hold no record |
| `files` | `{name: {rows, sha256}}`, every file in the zip with its row count and hash |

## Reading it

- Every record table carries `account_id` and `tier`; the tier is the row's sensitivity (ADR-FLSS-010: ST0 structure, ST1 shape,
  ST2 names and figures, ST3 mood, symptoms and other people, ST4 the private record and crisis data).
- Feed URLs are redacted; there are no keys or tokens in an export.
- The audit log (`trust.audit_entry.jsonl`) is exported with its hash chain, which verifies after import.
- A measure's CSV is the plain series a spreadsheet or another tool reads; the JSON Lines are the whole record.

## Importing it

The operator's `import-record` command reads a zip into an empty account, screens every registered input as historical, and resets
every higher-risk feature to off (moving modes changes what may leave a machine). A tampered zip, or one for a non-empty account,
is refused.
