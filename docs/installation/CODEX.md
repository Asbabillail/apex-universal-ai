# Use APEX in Codex

Codex supports repository-local Agent Skills. Use an authorized coding workspace to install APEX's three skill folders for that repository.

## Repository-local installation

1. Download and extract APEX's repository ZIP from GitHub.
2. Open your own coding project (the project where you intend Codex to use the skills).
3. Create \`.agents/skills/\` in the **root of your coding project**.
4. Copy the three folders from APEX's \`skills/\` directory into \`.agents/skills/\`. Keep \`SKILL.md\` and the \`references/\` subfolders together.
5. In a Codex session for that project, request the relevant skill by its name, e.g., "Use apex-prompt-engineering to clarify the requirements before writing code."
6. Confirm skill discovery in your Codex environment. If your version does not load repository-local skills, refer to its current instructions or use the generic copy/paste fallback.

Example structure:

\`\`\`text
your-project/
  .agents/skills/
    apex-prompt-engineering/SKILL.md
    apex-model-intelligence/SKILL.md
    apex-tool-workflow-intelligence/SKILL.md
\`\`\`

Codex skill use is not permission to write to a repository, deploy, read secrets, or perform other actions without the host's approval policies. Codex runtime support and file layout can vary by configuration.

[Official Codex skills engineering example](https://developers.openai.com/blog/skills-agents-sdk) · [APEX generic fallback](../../distributions/generic/APEX-COMMUNITY-INSTRUCTIONS.md)

[Report a problem](../FEEDBACK.md).
