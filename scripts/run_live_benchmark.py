#!/usr/bin/env python3
"""Opt-in live OpenAI Responses API benchmark of APEX SKILL-TEXT PROXY (no native plugin tools)."""
import argparse,json,os,sys,time
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
ROOT=Path(__file__).resolve().parents[1]
def instructions():
  names=['apex-prompt-engineering','apex-model-intelligence','apex-tool-workflow-intelligence']
  text='\n\n'.join((ROOT/'skills'/n/'SKILL.md').read_text() for n in names)
  return ("Apply these APEX skills. This is a text-only proxy: NO browser, GitHub, deployment, "
    "scheduler or other tools are connected. Tool receipts in prompts are fictional. "
    "Do not claim actual execution. Honor approval boundaries.\n\n"+text)
def main():
  a=argparse.ArgumentParser()
  a.add_argument('--model',default='gpt-6-luna')
  a.add_argument('--limit',type=int,default=20)
  a.add_argument('--output',default='reports/live-outputs.jsonl')
  a.add_argument('--dry-run',action='store_true')
  a.add_argument('--i-approve-api-charges',action='store_true')
  args=a.parse_args()
  cases=json.loads((ROOT/'benchmarks/cases.json').read_text())['cases']
  if not 1<=args.limit<=len(cases): a.error('invalid case limit')
  if args.dry_run:
    print(f'DRY RUN - {args.limit} synthetic cases; zero model calls');return 0
  if not args.i_approve_api_charges or not os.getenv('OPENAI_API_KEY'):
    print('NO MODEL RUN: require explicit --i-approve-api-charges and OPENAI_API_KEY',file=sys.stderr);return 2
  p=ROOT/args.output
  p.parent.mkdir(exist_ok=True,parents=True)
  if p.exists(): print('Refusing to overwrite results',file=sys.stderr);return 2
  with p.open('x',encoding='utf-8') as f:
    for c in cases[:args.limit]:
      request_body={'model':args.model,'instructions':instructions(),'input':c['request'],'max_output_tokens':1200,'store':False}
      req=Request('https://api.openai.com/v1/responses',data=json.dumps(request_body).encode(),
        headers={'Content-Type':'application/json','Authorization':'Bearer '+os.environ['OPENAI_API_KEY']},method='POST')
      start=time.monotonic()
      try:
        with urlopen(req,timeout=120) as h:d=json.loads(h.read())
      except (HTTPError,URLError,TimeoutError,ValueError) as e:
        f.write(json.dumps({'case_id':c['id'],'status':'error','error_type':type(e).__name__,'http_code':getattr(e,'code',None)})+'\n')
        print('API call error (stopped without automatic retries)',file=sys.stderr);return 1
      out='\n'.join(k.get('text','') for o in d.get('output',[]) for k in o.get('content',[]) if k.get('type')=='output_text')
      f.write(json.dumps({'case_id':c['id'],'status':'ok','model_returned':d.get('model'),'model_requested':args.model,
        'output_text':out,'usage':d.get('usage'),'latency_ms':round((time.monotonic()-start)*1000),
        'evaluation_scope':'skill-text proxy, no tool access'},ensure_ascii=False)+'\n')
      f.flush()
      print('completed',c['id'])
  os.chmod(p,0o600)
  print('Saved private measured outputs to',p);return 0
if __name__=='__main__':sys.exit(main())
