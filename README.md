# APEX — Universal AI Intelligence

![APEX static and fixture checks](https://github.com/Asbabillail/apex-universal-ai/actions/workflows/apex-ci.yml/badge.svg)

**APEX v3.0.0-alpha.2 — experimental development release**

> The right prompt. The right model. The right tools.

APEX is an open-source collection of AI-agent skills for refining user intent, composing concise prompts, evaluating AI model suitability, and designing permission-aware tool workflows. It is **not** a foundation model or a standalone always-running autonomous agent.

## What is implemented in this alpha
- **Core Intelligence:** Intent alignment, adaptive prompting methods, requirement-preserving compression and handover summaries.
- **AI Model Intelligence:** A procedure for source-backed platform/model/reasoning recommendations, not a live benchmark database.
- **Tool & Workflow Intelligence:** Capability-aware recommendations for plugins, skills, tools, agents, loops and graphs.

## What is *not* verified yet
- The skills have **not been evaluated against commercial AI models** in this repository.
- Installation and activation across ChatGPT, Claude and Gemini must be tested separately; support depends on the environment.
- No measured token reduction, model ranking, agent success rate or universal plugin compatibility is claimed.
- Skills cannot grant access to external accounts, create scheduled tasks or execute code by themselves.

## Getting started
1. Explore the relevant `SKILL.md` under `skills/`.
2. Use the native Agent Skills workflow supported by your AI environment, where available.
3. Tell APEX your goal, preferred mode (Quick, Collaborative or Advanced) and access constraints.
4. Verify model/tool access; authorize consequential actions separately.

### Example request
> APEX, collaborative: Help me plan a family trip; clarify what matters before creating a concise reusable prompt.

## Free, reproducible tests
- Structural checks: `python -m pip install PyYAML==6.0.2 && python tests/validate_skills.py`
- Fixture smoke checks: `npx --yes promptfoo@latest eval -c evals/promptfooconfig.yaml -o reports/promptfoo-echo.json`
- CI: See [GitHub Actions](../../actions).

**Important:** Promptfoo Echo repeats predefined sample text. The fixture tests verify test configuration and assertions; they **do not invoke APEX or measure model quality**. Tests may depend on package availability and GitHub runner limits.

See [Testing Policy](docs/TESTING.md) for evidence scope, known limitations, and proposed live-model evaluations.

## Evidence and pilot evaluations
Read [the anonymized five-scenario pilot](benchmarks/2026-10-manual-pilot.md) and [benchmark policy](benchmarks/README.md). These are **manual self-reviewed findings**, not a reproducible live-model benchmark. Actual CI checks are structural and prerecorded Promptfoo Echo fixtures; they do not assess AI reasoning. The alpha.2 update adds claim/source/scope/operation/result discipline to prevent overclaiming tool availability or execution.

## Roadmap
1. **Alpha:** Skill packaging, static checks and no-API smoke tests.
2. **Beta:** Reproducible live-model evals, installation evidence for each platform and multilingual usability review.
3. **Stable:** Documented quality gates, compatibility matrix, reliable release process, and independent contributions.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions and reproducible issue reports are welcome. Do not include confidential prompts, private conversations or credentials.

## Security
See [SECURITY.md](SECURITY.md). External actions require available tools and appropriate authorization.

## License
[MIT License](LICENSE). APEX is a community project; it is not officially certified or endorsed by OpenAI, Google, Anthropic, Promptfoo or GitHub.

## Synthetic 20-case benchmark

[Public synthetic cases](benchmarks/cases.json) and [evaluation protocol](benchmarks/README.md) are included. Offline structural tests run in CI. Live model calls require a separately authorized API key and explicit metered API approval; no API calls occur automatically. The runnable [model runner](scripts/run_live_benchmark.py) and [scorer](scripts/score_benchmark.py) test APEX skill text without native plugin tools; see [verification records](docs/certificates/README.md).
