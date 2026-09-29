# Migration Report

## Source

`具身智能开源数据集清单(2).xlsx` / `Sheet1`

## Result

| Item | Count |
|---|---:|
| Source rows | 117 |
| Source columns | 14 |
| Unique dataset cards | 116 |
| Duplicate source rows | 1 |

## Duplicate

`Ego2Robot` appears twice in the source workbook with identical metadata. One Dataset Card was created and the duplicate source row was recorded in `migration-audit.csv`.

## Important

The migration is intentionally **lossless at the source-information level**: all original 14 fields are preserved under each record's `legacy` object.

The normalized fields are generated for machine-readable navigation and should be reviewed against authoritative sources before being treated as verified taxonomy metadata.
