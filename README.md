# 🤖 Embodied AI Open Datasets

> **A community-driven open dataset catalog for Embodied AI, Robot Learning and Vision-Language-Action research.**

**具身智能开放数据集知识库**：将数据集从传统 Excel 清单升级为结构化、可验证、可动态更新、可社区贡献的开放数据集 Catalog。

## 📊 Current Baseline

本版本以原始 Excel 为迁移源：

- **117 条原始记录**
- **116 个唯一数据集**
- **1 条重复记录：Ego2Robot**
- **14 个原始字段**
- 所有原始字段均保存在对应 Dataset Card 的 `legacy` 字段中，迁移过程中不丢失原始信息。

> 注意：本仓库的 117 条记录来自当前上传 Excel。若未来发现还有第 118–177 条数据，请继续提交新版 Excel或直接通过 Issue/PR 补充。

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

同时保留原始中文字段：

```yaml
legacy:
  ...
```

因此 V2.0 是“结构化升级”，而不是重新人工抄录一遍数据。

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

因此以后新增一个数据集，不需要人工维护多个表格。

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

## ⚠️ Migration Note

本次迁移中的部分结构化字段是根据原始中文字段进行**规则化映射**，例如 Task、Environment、Modality、Embodiment。

这些字段应视为 **V2.0 初始标签**，而不是对原始资料的二次事实认定。

每条 Dataset Card 都保留：

```yaml
notes: ...
legacy: ...
```

建议后续由维护者依据官方论文、项目页和数据集页面逐条复核。

## 📖 Citation

```bibtex
@misc{embodied_ai_open_datasets,
  title        = {Embodied AI Open Datasets},
  author       = {AIIA / CAICT Embodied AI Benchmark Team},
  year         = {2026},
  howpublished = {GitHub repository},
  note         = {Community-driven catalog of open datasets for Embodied AI}
}
```

## 📜 License

The repository code and metadata structure are released under the MIT License.

Individual datasets remain subject to their original owners' licenses and terms of use.
