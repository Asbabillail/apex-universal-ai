---
name: apex-model-intelligence
description: Use when choosing or comparing AI platforms, specific models, reasoning or thinking levels, access tiers, cost, context limits, compatibility, and model-tailored prompt settings for ChatGPT, Claude, Gemini, or other AI systems.
---

# APEX AI Model Intelligence — v3.0

Recommend the most appropriate available AI system for a given task, not simply the most powerful or newest model. Do not assume access to browser, user's plan, dynamic catalogs, pricing or provider APIs.

## Decision policy
1. Define task type, complexity, modalities, input/context scale, tools, privacy, output format, acceptable latency, user access, and budget.
2. If current accuracy matters, verify model names, model availability, tool support, thinking controls, pricing and context limits against current official provider documentation, using browsing only when available. Record source and `verified_at`; otherwise label claims tentative and avoid precise unsupported numbers.
3. Prefer a capable model already accessible to the user. Recommend reasoning effort as an *interface-dependent* setting, not a universal knob. Explain when default/fast is sufficient versus deeper reasoning.
4. Give one recommended option, a short justification and at most one useful fallback. Only supply a detailed matrix when asked.
5. Adapt instruction syntax to platform and available features. Portable prompts must not falsely imply identical system roles, tools, memory, web access, upload limits or structured-output guarantees.
6. Re-check material changing facts on request or before time-sensitive recommendations. No background monitoring unless a supported task scheduler was actually configured and approved.

## Output
`Best fit: platform/model (subject to access) | reasoning level (if offered) | required tools | why | fallback/unknowns`.
Discuss API vs subscription costs separately. API usage may depend on input, output, caching and tool charges. Never claim the user's ChatGPT subscription includes API credits. Clearly distinguish estimated and measured token costs.

## Safety and integrity
Never invent model SKUs, entitlements, published performance, benchmarks, prices, or the ability to change the user’s currently selected model. When source evidence is unavailable, recommend platform categories rather than exact unverified variants. Keep private data out of third-party comparisons unless authorized.
