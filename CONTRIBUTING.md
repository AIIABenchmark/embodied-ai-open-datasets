# 🤝 Contributing to Embodied AI Open Datasets

Thank you for helping maintain the Embodied AI dataset catalog.

本项目欢迎研究机构、企业、开发者和研究人员共同补充、修正和完善具身智能开放数据集信息。

---

## 1. What can you contribute?

You can:

- Add a new dataset.
- Update an existing dataset.
- Correct metadata.
- Add missing paper/project/download links.
- Report broken links.
- Improve taxonomy definitions.
- Report duplicated or discontinued datasets.

---

## 2. Add a New Dataset

### Method A — GitHub Issue

Use the **New Dataset** issue template.

Please provide:

- Dataset name
- Official project/dataset URL
- Paper URL, if available
- Organization
- Release year
- Source type
- Modality
- Robot embodiment
- Tasks
- Environment
- Dataset scale
- Access status
- License
- Short description

A maintainer will review the submission and convert approved information into a structured Dataset Card.

### Method B — Pull Request

Copy:

```text
templates/dataset-template.yaml
```

to:

```text
data/datasets/<dataset-id>.yaml
```

Use a lowercase, stable, URL-safe ID.

Examples:

```text
open-x-embodiment.yaml
droid.yaml
agibot-world.yaml
```

---

## 3. Required Fields

Every dataset record must contain:

```text
id
name
year
description
source
modality
embodiment
tasks
application
links
status
last_verified
```

Optional fields may be omitted when information is genuinely unavailable.

Do not invent values merely to fill a field.

---

## 4. Taxonomy Rules

Use values defined in:

```text
data/taxonomy.yaml
```

If a required concept does not exist, do not create an arbitrary label.

Instead:

1. Open an issue describing the missing concept.
2. Explain why the existing taxonomy is insufficient.
3. Propose the new term.
4. After taxonomy approval, add it to the dataset record.

This keeps the catalog consistent over time.

---

## 5. Links

Prefer authoritative links in this order:

1. Official dataset page
2. Official project page
3. Official code repository
4. Official paper page
5. Trusted archival/download page

Avoid linking to unofficial mirrors when an authoritative source exists.

---

## 6. Availability

Do not equate “paper available” with “dataset available”.

Use:

```text
open
registration_required
request_access
partial
benchmark_only
unavailable
unknown
```

---

## 7. License

Record the dataset license when explicitly stated by the dataset owner.

Do not infer a license from the code repository license.

For example, a repository may use MIT while the dataset itself is restricted to research use.

---

## 8. Verification

Every dataset record has:

```yaml
last_verified: YYYY-MM-DD
```

When you update a dataset, refresh this field.

---

## 9. Local Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Validate:

```bash
python scripts/validate.py
```

Build generated documents:

```bash
python scripts/build.py
```

Generate Excel:

```bash
python scripts/generate_excel.py
```

---

## 10. Pull Request Checklist

Before submitting a PR:

- [ ] Dataset ID is unique.
- [ ] Required fields are complete.
- [ ] Taxonomy values are valid.
- [ ] Official links have been checked.
- [ ] Access status is accurate.
- [ ] Dataset license is not confused with code license.
- [ ] `last_verified` is updated.
- [ ] `python scripts/validate.py` passes.
- [ ] Generated files are updated if required.

---

## 11. Duplicate Datasets

If multiple releases belong to the same dataset family, do not automatically create separate records.

Use the dataset name and project identity to determine whether the release is:

- a new dataset;
- a new version;
- a benchmark derived from an existing dataset;
- or a duplicate listing.

When uncertain, open an issue for discussion.

---

## 12. Corrections

If information is wrong, please use:

**Report an Error**

rather than silently changing unrelated records.

Small corrections are welcome through direct PRs.

---

## 13. Maintainer Review

Maintainers may review:

- relevance to Embodied AI;
- source reliability;
- duplicate status;
- taxonomy consistency;
- license/access accuracy;
- link validity.

The catalog is intended to be factual and descriptive rather than a ranking of datasets.

---

## 14. Code of Conduct

Please keep contributions factual, constructive and respectful.

Do not use the dataset catalog to promote unsupported claims about dataset quality, model performance or research institutions.
