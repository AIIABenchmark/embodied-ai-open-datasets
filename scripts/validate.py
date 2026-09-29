#!/usr/bin/env python3
from pathlib import Path
import sys,yaml,re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/datasets"
TAX=ROOT/"data/taxonomy.yaml"
REQ=["id","name","year","description","source","modality","embodiment","tasks","application","links","status"]
def load(p):
    with open(p,encoding="utf-8") as f:return yaml.safe_load(f)
def main():
    tax=load(TAX)
    valid={
      "source":set(x["id"] for x in tax["source"]),
      "modality":set(tax["modality"]),
      "task":set(tax["task"]),
      "environment":set(tax["environment"]),
      "application":set(tax["application"]),
      "availability":set(tax["availability"]),
      "license":set(tax["license"]),
      "data_format":set(tax["data_format"]),
      "emb_type":set(tax["embodiment"]["type"]),
      "platform":set(tax["embodiment"]["platforms"])
    }
    errors=[]; ids=set()
    for p in sorted(DATA.glob("*.yaml")):
        try:r=load(p)
        except Exception as e: errors.append(f"{p}: YAML error: {e}"); continue
        for k in REQ:
            if k not in r or r[k] in (None,"",[]): errors.append(f"{p}: missing {k}")
        rid=r.get("id")
        if rid in ids: errors.append(f"{p}: duplicate id {rid}")
        if rid: ids.add(rid)
        if rid and p.stem!=rid: errors.append(f"{p}: filename/id mismatch")
        for k,tk in [("source","source"),("modality","modality"),("tasks","task"),("application","application"),("data_format","data_format")]:
            for v in r.get(k,[]) or []:
                if v not in valid[tk]: errors.append(f"{p}: invalid {k}={v}")
        e=r.get("embodiment") or {}
        for v in e.get("type",[]) or []:
            if v not in valid["emb_type"]: errors.append(f"{p}: invalid embodiment type={v}")
        for v in e.get("platforms",[]) or []:
            if v not in valid["platform"]: errors.append(f"{p}: invalid platform={v}")
        for v in r.get("environment",[]) or []:
            if v not in valid["environment"]: errors.append(f"{p}: invalid environment={v}")
        a=(r.get("access") or {}).get("availability")
        if a and a not in valid["availability"]: errors.append(f"{p}: invalid availability={a}")
        l=(r.get("license") or {}).get("type")
        if l and l not in valid["license"]: errors.append(f"{p}: invalid license={l}")
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(" - "+e for e in errors))
        sys.exit(1)
    print(f"VALIDATION PASSED: {len(ids)} dataset records checked.")
if __name__=="__main__":main()
