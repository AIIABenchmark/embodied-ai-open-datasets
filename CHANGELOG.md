# Changelog

## [2.0.0-117] - 2026-09-26

### Added

- Migrated the uploaded 117-row dataset catalog.
- Created 116 unique Dataset Cards.
- Preserved the duplicate Ego2Robot source row in migration audit files.
- Preserved all original 14 fields under `legacy`.
- Added normalized taxonomy fields for source, modality, embodiment, task, environment and application.
- Generated Markdown catalogs, statistics and Excel export.
- Added migration report and audit files.

## 2026-09-29 — Excel link fields fixed
- Added the exact columns `论文/技术报告链接` and `数据开源链接` to the Excel export.
- Both URL columns are exported as clickable hyperlinks when a valid URL is available.
- The Excel generator now falls back to the migrated `legacy` fields, preventing link loss in future rebuilds.
