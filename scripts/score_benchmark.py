#!/usr/bin/env python3
"""Report actual provider usage, lexical requirement signals, and optional human ratings."""
import argparse,json
from pathlib import Path
from statistics import mean
ROOT=Path(__file__).resolve().parents[1]
FIELDS=('requirement_retention','reasoning_quality','tool_accuracy')
def lexical_score(c,s):
  groups=c['retention_signals']
  hits=sum(any(z.casefold() in s.casefold() for z in g) for g in groups)
  mx=c.get('max_words')
  return {'signals_matched':hits,'signals_total':len(groups),'lexical_coverage':hits/len(groups),
    'within_word_limit':None if mx is None else len(s.split())<=mx}
def analyze(cases,outputs,annotations=None):
  by={r['case_id']:r for r in outputs}
  details=[]; usage=[];rated=[]
  for c in cases:
    r=by.get(c['id']);ok=bool(r and r.get('status')=='ok')
    item={'case_id':c['id'],'category':c['category'],'executed':ok,
      'lexical':lexical_score(c,r.get('output_text','')) if ok else None,
      'latency_ms':r.get('latency_ms') if ok else None,'manual':None}
    if ok and isinstance(r.get('usage'),dict) and all(isinstance(r['usage'].get(k),int) for k in ('input_tokens','output_tokens','total_tokens')):usage.append(r['usage'])
    a=(annotations or {}).get('ratings',{}).get(c['id'])
    if a and all(isinstance(a.get(k),int) and 0<=a[k]<=4 for k in FIELDS):
      item['manual']={k:a[k] for k in FIELDS};rated.append(item['manual'])
    details.append(item)
  done=[x for x in details if x['executed']]
  signals=[x['lexical']['lexical_coverage'] for x in done]
  limits=[x['lexical']['within_word_limit'] for x in done if x['lexical']['within_word_limit'] is not None]
  delays=[x['latency_ms'] for x in done if isinstance(x['latency_ms'],int)]
  return {'report_kind':'real model API if executed; APEX skill-text proxy, not installed ChatGPT plugin',
    'total_cases':len(cases),'successful_responses':len(done),'missing_or_errored':len(cases)-len(done),
    'lexical_retention_proxy_mean':mean(signals) if signals else None,
    'word_limit_passes':sum(limits) if limits else None,'word_limit_cases':len(limits),
    'actual_provider_usage_tokens':{k:sum(u[k] for u in usage) for k in ('input_tokens','output_tokens','total_tokens')} if usage else None,
    'mean_latency_ms':mean(delays) if delays else None,'reviewed_cases':len(rated),
    'human_quality_scores_0_to_4':{k:mean(x[k] for x in rated) for k in FIELDS} if rated else None,
    'end_to_end_real_tool_execution_accuracy':None,
    'limits':['lexical matching is NOT semantic grading','tool receipts are simulated, no live tools','token savings need matched baseline'],
    'cases':details}
def main():
  p=argparse.ArgumentParser()
  p.add_argument('--input',required=True);p.add_argument('--output',default='reports/live-score.json')
  p.add_argument('--annotations');a=p.parse_args()
  inp=Path(a.input);inp=inp if inp.is_absolute() else ROOT/inp
  if not inp.is_file():p.error('no real model output file')
  outputs=[json.loads(x) for x in inp.read_text().splitlines() if x.strip()]
  cs=json.loads((ROOT/'benchmarks/cases.json').read_text())['cases']
  ann=None
  if a.annotations:
    an=Path(a.annotations);ann=an if an.is_absolute() else ROOT/an
    ann=json.loads(an.read_text())
  result=analyze(cs,outputs,ann)
  dest=Path(a.output);dest=dest if dest.is_absolute() else ROOT/dest
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
