# APEX platform compatibility (alpha)

**Evidence level:** These are provider-documented installation workflows plus APEX's published files. **Not** proof that the complete APEX three-skill package has passed end-to-end tests on each platform. Actual behavior and feature availability vary by plan, region and account.

| Platform | Free copy/paste fallback | Reusable native option | APEX status |
| --- | --- | --- | --- |
| ChatGPT | Paste [generic instructions](../distributions/generic/APEX-COMMUNITY-INSTRUCTIONS.md) in a fresh chat | Personal Skills upload for eligible accounts; public plugin listing pending | Native external installation **unverified** |
| Claude | Paste generic instructions | Upload **one skill ZIP per skill** under Customize → Skills (when available) | Not independently tested |
| Gemini | Paste generic instructions | Create a Gem with the adapted instruction text | Not independently tested |
| Codex | Paste generic instructions | Copy skill folders to a supported repository-local skills directory | Not independently tested |
| Other AI assistants | Paste generic instructions | Provider-specific, if available | Not independently tested |

**Feature limits:** Installing APEX instructions does not itself authorize file access, GitHub, web research, API calls, scheduling or account actions. Model availability and thinking effort depend on the specific service. Benchmark fixtures don't demonstrate cross-platform model quality.

**Source docs:**
- [OpenAI plugins](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
- [OpenAI skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Gemini Gems](https://support.google.com/gemini/answer/15146780)
- [Codex repository skills example](https://developers.openai.com/blog/skills-agents-sdk)

Testing? [Submit a feedback report](https://github.com/Asbabillail/apex-universal-ai/issues/new?template=feedback.yml).
