# Use APEX with Claude

Claude supports personal custom skills where available; it does **not** directly import the whole APEX ChatGPT plugin as a single universal installation.

## Quickest way: paste instructions

Open [APEX Community Instructions](../../distributions/generic/APEX-COMMUNITY-INSTRUCTIONS.md) and paste them into a new Claude chat before asking your actual question.

## Native custom skills

1. Download the repository via **Code → Download ZIP** and extract it.
2. In the extracted \`skills/\` directory, choose **one** skill folder (for example, \`apex-prompt-engineering\`).
3. Create a ZIP containing that **single folder**, including its \`SKILL.md\` and any \`references/\` files. Do not zip the whole repository for one skill.
4. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**, as available.
5. Upload that ZIP and enable the skill. Repeat separately for model and workflow skills if you want all three.
6. Start a new chat and ask Claude to use the relevant skill. If Skills is unavailable, use the copy/paste method.

Claude's official guide notes that skill execution depends on capabilities and workspace settings, including code execution being enabled where required. Only upload skills from authors you trust and inspect their contents first.

[Official Claude instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

[Report a problem](../FEEDBACK.md).
