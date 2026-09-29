#!/usr/bin/env python3
from pathlib import Path
from collections import Counter, defaultdict
import yaml

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/datasets"
DOCS=ROOT/"docs"
STATS=ROOT/"statistics"

def records():
    out=[]
    for p in sorted(DATA.glob("*.yaml")):
        with open(p,encoding="utf-8") as f:
            out.append(yaml.safe_load(f))
    return out

def labels(xs):
    return ", ".join(str(x).replace("_"," ") for x in (xs or []))

def catalog(rs):
    L=["# 📚 Embodied AI Dataset Catalog","",
       "> Automatically generated from `data/datasets/*.yaml`. Do not edit manually.","",
       f"**Datasets: {len(rs)}**","",
       "| Dataset | Year | Source | Modality | Embodiment | Tasks | Application |",
       "|---|---:|---|---|---|---|---|"]
    for r in sorted(rs,key=lambda x:(x.get("year",0),x.get("name","")),reverse=True):
        e=(r.get("embodiment") or {}).get("type",[])
        L.append(f"| **{r.get('name','')}** | {r.get('year','')} | {labels(r.get('source'))} | "
                 f"{labels(r.get('modality'))} | {labels(e)} | {labels(r.get('tasks'))} | {labels(r.get('application'))} |")
    return "\n".join(L)+"\n"

def dimension(rs, getter, title, filename):
    groups=defaultdict(list)
    for r in rs:
        for v in getter(r):
            groups[v].append(r["name"])
    L=[f"# {title}","","> Automatically generated.",""]
    for k in sorted(groups):
        L += [f"## {k.replace('_',' ').title()}",""]
        L += [f"- {n}" for n in sorted(groups[k])]
        L.append("")
    (DOCS/filename).write_text("\n".join(L),encoding="utf-8")

def main():
    rs=records()
    DOCS.mkdir(exist_ok=True); STATS.mkdir(exist_ok=True)
    (DOCS/"datasets.md").write_text(catalog(rs),encoding="utf-8")
    dimension(rs,lambda r:r.get("source",[]),"Datasets by Data Source","datasets-by-source.md")
    dimension(rs,lambda r:r.get("modality",[]),"Datasets by Modality","datasets-by-modality.md")
    dimension(rs,lambda r:r.get("tasks",[]),"Datasets by Task","datasets-by-task.md")
    dimension(rs,lambda r:r.get("application",[]),"Datasets by Application Stage","datasets-by-application.md")
    dimension(rs,lambda r:(r.get("embodiment") or {}).get("type",[]),"Datasets by Embodiment","datasets-by-embodiment.md")
    years=defaultdict(list)
    for r in rs: years[r.get("year","Unknown")].append(r["name"])
    L=["# 📅 Dataset Timeline","","| Year | Datasets |","|---:|---|"]
    for y in sorted(years,reverse=True): L.append(f"| {y} | {', '.join(sorted(years[y]))} |")
    (DOCS/"timeline.md").write_text("\n".join(L)+"\n",encoding="utf-8")
    counters={
        "Data Source":Counter(v for r in rs for v in r.get("source",[])),
        "Modality":Counter(v for r in rs for v in r.get("modality",[])),
        "Task":Counter(v for r in rs for v in r.get("tasks",[])),
        "Embodiment":Counter(v for r in rs for v in (r.get("embodiment") or {}).get("type",[])),
        "Application":Counter(v for r in rs for v in r.get("application",[])),
    }
    L=["# 📈 Statistics","",f"**Total dataset cards: {len(rs)}**",""]
    for title,c in counters.items():
        L += [f"## {title}","","| Category | Count |","|---|---:|"]
        L += [f"| {k.replace('_',' ')} | {v} |" for k,v in c.most_common()]
        L.append("")
    (STATS/"overview.md").write_text("\n".join(L),encoding="utf-8")

if __name__=="__main__": main()
