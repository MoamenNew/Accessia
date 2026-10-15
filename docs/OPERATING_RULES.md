# Operating Rules | قواعد التشغيل

## Phase 1 — Discover
Clarify who uses it, the problem, must-have functionality, data sensitivity and success criteria. Ask no more than three blocking questions. Avoid overengineering.

## Phase 2 — Spec + architecture (NO CODING)
Maintain `PROJECT_BRIEF.md`, `RESEARCH.md`, `PRODUCT_SPEC.md`, `ARCHITECTURE.md`, and `SECURITY.md`. Compare at least two realistic implementation options when complexity warrants it. State assumptions, scope exclusions, likely costs, and acceptance tests. Request explicit approval.

## Phase 3 — Implement after `أوافق على الخطة`
Make small commits/changes. For each change: write code, run tests available, review errors, record result. Stay inside agreed MVP scope. New infrastructure or recurring cost: pause and ask.

## Phase 4 — Verify
Functional tests, input validation, common failure paths, basic secret checks, access control if relevant, dependency review if relevant. Use reputable scanners if installed and authorized; list what was NOT tested.

## Phase 5 — Handoff
Short Arabic explanation and exact run steps. Ask separate approval before a public deployment, paid services or production secrets.

## Guardrails
- No unattended publishing, spending, destructive operations, scraping prohibited data, or use of real customer/medical/payment data as demonstration material.
- No logs containing keys or personal data.
- Do not turn off security checks just to get a green build.
- Keep a human confirmation gate for auth, billing, sensitive information, and production deployment.
- Web/terminal environments differ. Report limitations candidly.
