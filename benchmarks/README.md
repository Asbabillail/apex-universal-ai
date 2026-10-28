# APEX benchmark evidence

This directory separates **manual observations**, **automated fixture checks**, and **future live-model evaluations**.

- [Five-scenario pilot (October 2026)](2026-10-manual-pilot.md): privacy-safe, human-assessed observations from a real requirements conversation. Its source documents and full outputs are private, so it is **not an independently reproducible benchmark**.
- [CI workflow](../.github/workflows/apex-ci.yml): static skill/manifests contract checks and Promptfoo Echo tests against prerecorded strings. Echo tests do not execute the APEX plugin or demonstrate model quality.
- [Testing policy](../docs/TESTING.md): planned live evaluations and release gates.

## Evidence labeling rules

Use `source → scope → operation → observed result → status/date`. A claim validated in one account, project, repo or test run cannot be reused as proof of success somewhere else.

For public live-model benchmarks, publish non-sensitive prompts, model+environment versions, grading rubric, raw responses (where rights and consent permit), usage/latency measured at run time, limitations, and reproducible test instructions. Never publish identifiable CVs, private repositories, credentials, or conversations without explicit permission.

No official or independent accreditation is claimed. A "pass" means only that the specified checks ran and met their declared criteria.
