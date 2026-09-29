# 🤖 Embodied AI Open Datasets

> **A community-driven open dataset catalog for Embodied AI, Robot Learning and Vision-Language-Action research.**

**具身智能开放数据集知识库**：系统性梳理与跟踪具身智能领域开源数据集。


## 🧱 Architecture

```text
data/datasets/*.yaml
        │
        ├── validate.py
        │
        └── build.py
              ├── Dataset Catalog
              ├── Category Catalogs
              ├── Timeline
              └── Statistics
                       │
                       └── generate_excel.py
                              ↓
                       Excel export
```

**YAML 是唯一数据源；Markdown、统计页面和 Excel 都是自动生成结果。**

## 🔎 Explore

- [Full Dataset Catalog](docs/datasets.md)
- [By Data Source](docs/datasets-by-source.md)
- [By Modality](docs/datasets-by-modality.md)
- [By Embodiment](docs/datasets-by-embodiment.md)
- [By Task](docs/datasets-by-task.md)
- [By Application Stage](docs/datasets-by-application.md)
- [Timeline](docs/timeline.md)
- [Statistics](statistics/overview.md)

## 🗃️ Dataset Card

每个数据集独立存储为：

```text
data/datasets/<dataset-id>.yaml
```

核心维度：

**Source × Modality × Embodiment × Task × Environment × Application × Availability × License**



## 🤝 Community Contribution

### Add a dataset

使用 GitHub Issue：

[New Dataset](../../issues/new?template=new-dataset.yml)

或者复制：

```text
templates/dataset-template.yaml
```

提交：

```text
data/datasets/<dataset-id>.yaml
```

### Report an update

- [Update Dataset](../../issues/new?template=update-dataset.yml)
- [Report Error / Broken Link](../../issues/new?template=report-error.yml)

## 🔄 Dynamic Update

合并 PR 后，GitHub Actions 可以自动：

1. 校验 YAML；
2. 检查 ID 与 taxonomy；
3. 生成 Dataset Catalog；
4. 生成分类页面；
5. 更新统计；
6. 导出 Excel。


## 📐 Taxonomy

分类体系见：

```text
data/taxonomy.yaml
```

当前包括：

- Data Source
- Modality
- Embodiment
- Task
- Environment
- Application Stage
- Availability
- License
- Data Format


## 📖 Citation

```bibtex
@misc{embodied_ai_open_datasets,
  title        = {Embodied AI Open Datasets},
  author       = {CAICT EAI Bench Team},
  year         = {2026},
  howpublished = {GitHub repository},
  note         = {Community-driven catalog of open datasets for Embodied AI}
}
```

## 📜 License

The repository code and metadata structure are released under the MIT License.

Individual datasets remain subject to their original owners' licenses and terms of use.
