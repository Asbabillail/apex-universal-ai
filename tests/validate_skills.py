#!/usr/bin/env python3
"""Offline contract check for APEX skill bundle. Does NOT evaluate LLM behavior."""
from pathlib import Path
import json, re, sys, yaml

ROOT=Path(__file__).resolve().parents[1]
MANDATORY={"apex-prompt-engineering", "apex-model-intelligence", "apex-tool-workflow-intelligence"}
errors=[]
for rel in ("plugin.json", ".codex-plugin/plugin.json"):
    try:
        j=json.loads((ROOT/rel).read_text(encoding="utf-8"))
        if j.get("name")!="apex-prompt-intelligence": errors.append(f"{rel}: unexpected name")
        if j.get("version")!="3.0.0-alpha.2": errors.append(f"{rel}: unexpected version")
    except Exception as ex: errors.append(f"{rel}: {ex}")
for name in sorted(MANDATORY):
    path=ROOT/"skills"/name/"SKILL.md"
    try:
        t=path.read_text(encoding="utf-8")
        found=re.match(r"\A---\n(.*?)\n---\n",t,re.S)
        if not found: errors.append(f"{name}: invalid YAML frontmatter");continue
        fm=yaml.safe_load(found.group(1))
        if fm.get('name')!=name: errors.append(f"{name}: name mismatch")
        if not isinstance(fm.get('description'),str) or len(fm['description'])<40: errors.append(f"{name}: missing description")
        if len(t)>18000:errors.append(f"{name}: too long for targeted progressive disclosure")
        if re.search(r'(?i)(sk-[A-Za-z0-9]{25,}|ghp_[A-Za-z0-9]{30,})',t): errors.append(f"{name}: potential credential")
    except Exception as ex:errors.append(f"{name}: {ex}")
core=(ROOT/'skills/apex-prompt-engineering/SKILL.md').read_text()
model=(ROOT/'skills/apex-model-intelligence/SKILL.md').read_text()
work=(ROOT/'skills/apex-tool-workflow-intelligence/SKILL.md').read_text()
checks={"intent alignment":all(x in core for x in ["Listen", "Analyze", "Clarify", "Reanalyze", "Align"]),
 "token discipline":"per token" in core and "requirement" in core,
 "model availability": "verified_at" in model and "availability" in model,
 "permission boundaries":all(x in work for x in ["L0:","L1:","L2:","L3:"]),
 "workflow patterns":all(x in work for x in ["Loop", "Graph", "Code-first"]),
 "evidence protocol": (ROOT/'skills/apex-tool-workflow-intelligence/references/evidence-protocol.md').exists() and "references/evidence-protocol.md" in work,
 "cross-project scope": "project scope" in core and "model-picker access" in model and "different repository" in work,
 "skill count": len(list((ROOT/'skills').glob('*/SKILL.md')))==3}
for title,ok in checks.items():
 if not ok: errors.append(f"contract: {title}")
report={"test_kind":"static_contract_only","version":"3.0.0-alpha.2","checks":checks,"passed":len(errors)==0,"errors":errors,"does_not_verify":["real model behavior","ChatGPT plugin activation","live tool access","cross-provider correctness","token savings"]}
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports/static-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
sys.exit(0 if not errors else 1)
