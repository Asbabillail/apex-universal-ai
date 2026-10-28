# APEX v3 — privacy-safe manual pilot

**Review date:** October 29, 2026  
**Plugin version during pilot:** `3.0.0-alpha.1`  
**Follow-up correction:** Evidence-scope instructions added in `3.0.0-alpha.2`  
**Evidence category:** Maintainer-provided APEX response transcripts, manually assessed; **not independent, blinded, or CI-tested AI output**.

## Scenario and privacy

A user asked APEX to help plan a professional portfolio website using two candidate-supplied résumé drafts with conflicting descriptions and a privately hosted reference portfolio. The candidate's identity, CV details, contact information, and private repository are intentionally omitted. These materials have **not** been placed in this public benchmark.

The pilot assessed whether APEX stayed in collaborative discovery, distinguished claims from evidence, selected appropriate architecture and tools, compressed context without losing material decisions, and corrected overstatements.

## Preliminary manual rubric

| Test | Behaviors evaluated | Fully met | Partially verified |
| --- | --- | ---: | ---: |
| 01 — Intent and evidence | Recognize source conflict, ask useful questions, respect scope, privacy | 6/6 | 0 |
| 02 — Context compression | Retain key discrepancies, alternatives, pending decisions and restrictions | 6/6 | 0 |
| 03 — Model and tool recommendation | Appropriate architecture, model/tool reasoning, justified access claims | 5/6 | 1 |
| 04 — Agent workflow design | Simplicity, approval gates, test/recovery policy, actual execution evidence | 5/6 | 1 |
| 05 — Evidence self-audit | Corrections, tool provenance, cross-project scope, uncertainty | 5/6 | 1 |
| **Total** | **Maintainer-assessed checklist criteria** | **27/30** | **3** |

**Interpretation:** 27 of 30 preliminary checklist criteria were marked fully satisfied, and three partially satisfied. This is a *subjective pilot tally*, **not a 90% model performance claim**. No unbiased comparison group, confidence interval, unseen test set, or external grader was used. APEX reviewed its own outputs in Test 05, which is self-evaluation, not independent verification.

### Important observations and gaps

- **Intent:** APEX identified substantive discrepancies rather than automatically deciding which document was correct. It kept unresolved decisions open.
- **Compression:** The model reported an approximately 200-word handover of **202 whitespace-separated words**. That matches an approximate target but would exceed a strict 200-word maximum. **Model tokens were not measured**, so token reduction remains unverified.
- **Model/tool advice:** The recommended lightweight website architecture was reasonable, but exact model-picker access and actual tool actions need scope-specific verification.
- **Execution planning:** The suggested agent and bounded repair loops were plans; no website-building agent was executed in this pilot.
- **Evidence corrections:** Separating provider documentation, connected tool data, user context and inference improved credibility. A connected team's reported subscription plan does not imply an invoice-level audit. A successful tool action in one repository does not establish that the same action happened in a different repository.

## Verification limits

The maintainer supplied text responses, **not an independently replayable tool trace**, so statements about underlying calls were assessed against separately accessible evidence where possible. Source private documents were not copied. Tool availability, host permissions and exact model versions vary by session.

Do **not** combine this pilot with the repository's Promptfoo Echo pass count: those are prerecorded-fixture checks, not live-model behavior.

## What follows

1. Create consented, fully synthetic test cases approximating the same failure modes.
2. Capture actual responses and tool traces for a named model/version and host environment.
3. Add independent reviewers and measured token/latency data.
4. Distinguish structural, fixture, behavioral and deployment tests in every public report.
5. Re-run and disclose failures after each release.

**No current statement here constitutes a third-party certification or evidence that APEX outperforms other agents.**
