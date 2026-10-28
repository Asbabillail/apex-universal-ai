# Synthetic 20-case benchmark

Four synthetic cases each for intent, compression, model recommendations, tools/workflow decisions, and evidence integrity.

- `cases.json`: public fictional prompts and lexical signals; no private CVs or source repositories.
- `LIVE_EVALUATION_STATUS.json`: tracks the current **unrun** API benchmark accurately.
- Lexical signal matching is only a proxy; it is not a verified model-quality score.
- Real model evaluation requires user-provided API credentials and separate approval for usage charges. A ChatGPT subscription is **not** API funding.
- Tool-evidence tasks use fictional receipts to test *claims*. Real tool execution requires a different harness with actual tool logs.

A full local execution kit, including the runner, scorer, test contracts, report template and signed-off CI records, is available as the user's complete downloadable project ZIP.
