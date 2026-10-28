# Testing policy

| Check | Evidence | Meaning | Limit |
|---|---|---|---|
| Python contract validator | `reports/static-results.json` | Manifest and instruction structure matches contract | Does not exercise an LLM |
| Promptfoo Echo | `reports/promptfoo-echo.json` in CI | Deterministic fixture assertions pass | Does not invoke APEX |
| Live model evaluation (future) | Versioned dataset, responses and review | Behavior with specific model/version | Requires current model access, may cost money |
| Host runtime integration (future) | Screenshots/logs or reproducible traces | Skill loads and tools are routed correctly | Platform-dependent |

**No third-party certification:** Any APEX verification record is self-issued and only covers tests explicitly listed. Do not label it independent certification or official endorsement by OpenAI, Anthropic, Google, GitHub or Promptfoo.

## Future live eval gates
Minimum 60 reviewed cases across daily prompting, writing, research, education, coding, multilingual requests, model selection, plugin routing, context compression and adversarial permissions. Track critical requirement retention, routing accuracy, real tool authorization, token usage, latency, and honest uncertainty. Publish raw test definitions and dated reports. Do not assert percentages before running the suite.

## Manual pilot (separate from CI)
Five maintainer-provided APEX conversations were reviewed manually, with a privacy-safe summary in [the pilot report](../benchmarks/2026-10-manual-pilot.md). The original task materials were private and are not published. Those ratings are preliminary and cannot be reproduced from the public dataset. Do not equate the score with independent certification, measured model quality, or the six prerecorded Echo fixtures. Alpha.2 adds evidence provenance and project-scope checks to its static contract validator; these only verify instruction text/format, not runtime behavior.
