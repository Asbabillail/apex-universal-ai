import json,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from score_benchmark import analyze,lexical_score
class BenchmarkContract(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.cases=json.loads((ROOT/'benchmarks/cases.json').read_text())['cases']
 def test_twenty_unique(self):
  self.assertEqual(len(self.cases),20);self.assertEqual(len(set(c['id'] for c in self.cases)),20)
 def test_five_balanced_categories(self):
  for x in ('intent','compression','model','tools','evidence'):self.assertEqual(sum(c['category']==x for c in self.cases),4)
 def test_fields(self):
  for c in self.cases:
   self.assertTrue(c['request']);self.assertTrue(c['review_focus']);self.assertTrue(c['retention_signals'])
 def test_no_private_names(self):
  text=(ROOT/'benchmarks/cases.json').read_text().casefold()
  for item in ('faizan','taif','yenepoya','nmf1947','547652833'):self.assertNotIn(item,text)
 def test_no_fake_results(self):
  a=analyze(self.cases,[])
  self.assertEqual(a['successful_responses'],0)
  self.assertIsNone(a['actual_provider_usage_tokens'])
  self.assertIsNone(a['human_quality_scores_0_to_4'])
 def test_lexical_check(self):
  self.assertEqual(lexical_score({'retention_signals':[['foo'],['bar','baz']]},'foo baz')['lexical_coverage'],1.0)
if __name__=='__main__':unittest.main()
