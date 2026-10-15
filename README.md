# Curiosity OS Starter v1.0

**Think it. Plan it. Build it. Verify it.**

A beginner-friendly AI coding-agent starter repository. This repo does not contain a finished app. It contains explicit planning gates, Arabic copy-paste prompts, documentation templates, and lightweight repository checks.

## Start here
1. Read [START_HERE.md](START_HERE.md) (Arabic).
2. Open `prompts/01_UNDERSTAND_IDEA.txt`, replace the idea placeholder, and paste it into a **repository-connected coding agent** (Codex Cloud or Claude Code on the web).
3. Review the proposed spec and architecture before writing `أوافق على الخطة`.
4. Continue with `02_BUILD_MVP.txt`, `03_TEST_AND_SECURITY.txt`, and `04_HANDOFF.txt`.

## Built-in guardrails
- `AGENTS.md`: instructions for supported coding agents including Codex.
- `CLAUDE.md`: points Claude Code to the shared instructions.
- `docs/`: project brief, research, product spec, architecture, security, and build log.
- `.github/workflows/quality.yml`: runs basic repository contract checks.

## Important limitations
- This template does **not** install OpenSpec or Superpowers. Those are optional advanced tools and should be installed separately where supported.
- The automated checks only validate starter structure and detect a few obvious secret patterns. They are **not an application security audit**.
- Public deployment and use of paid/cloud services require explicit user approval.
- Codex/Claude interfaces and availability depend on subscription and workspace settings.

## Validation
```bash
python3 scripts/verify_project.py
python3 -m unittest discover -s tests -v
```

## Maintainers and community
Copy/fork the template and adapt it. Do not commit real customer data, secrets, or copyrighted third-party assets.

## Primary official resources (checked October 2026)
- Codex Cloud: https://help.openai.com/en/articles/20001545-using-codex-cloud
- Codex Cloud getting started: https://learn.chatgpt.com/docs/cloud
- Claude Code on the web: https://support.claude.com/en/articles/12618689-claude-code-on-the-web
- GitHub uploads: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- OpenSpec (optional): https://github.com/Fission-AI/OpenSpec
- Superpowers (optional): https://github.com/obra/superpowers
