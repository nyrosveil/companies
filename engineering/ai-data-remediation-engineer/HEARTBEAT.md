---
updated: 2025-03-17
created: 2025-03-17
---
# HEARTBEAT.md -- AI Data Remediation Engineer Heartbeat Checklist

Run this checklist on every heartbeat.

## 1. Identity and Context

- `GET /api/agents/me` -- confirm your id, role, budget, chainOfCommand.
- Check wake context: `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_COMMENT_ID`.

## 2. Local Planning Check

1. Read today's plan from `$AGENT_HOME/memory/YYYY-MM-DD.md` under "## Today's Plan".
2. Review each planned item: what's completed, what's blocked, and what up next.
3. For any blockers, resolve them yourself or escalate.
4. If you're ahead, start on the next highest priority.
5. **Record progress updates** in the daily notes.

## 3. Approval Follow-Up

If `PAPERCLIP_APPROVAL_ID` is set:

- Review the approval and its linked issues.
- Close resolved issues or comment on what remains open.

## 4. Get Assignments

- `GET /api/companies/{companyId}/issues?assigneeAgentId={your-id}&status=todo,in_progress,blocked`
- Prioritize: `in_progress` first, then `todo`. Skip `blocked` unless you can unblock it.
- If there is already an active run on an `in_progress` task, move to next.
- If `PAPERCLIP_TASK_ID` is set and assigned to you, prioritize that task.

## 5. Work Execution

- Always checkout before working: `POST /api/issues/{id}/checkout`.
- Never retry a 409 -- that task belongs to someone else.
- Perform the work (coding, testing, review, deployment). Update status and comment when done.

## 6. Engineering Workflow

When executing engineering tasks:

1. Understand requirements fully before starting.
2. Check existing codebase and documentation first.
3. Write tests before implementation (TDD approach).
4. Follow code quality standards and review processes.
5. Test changes thoroughly before marking complete.
6. Update documentation and comments as needed.
7. Consider maintainability and future extensibility.
8. Document technical decisions and rationale.

When blocked:
1. Try to resolve yourself (research, experiment, troubleshoot).
2. If still blocked, update issue to `blocked` with clear technical details.
3. Escalate to CTO or appropriate senior agent with context.

## 7. Fact Extraction

1. Check for new conversations since last extraction.
2. Extract durable facts (technical decisions, patterns, solutions) to `$AGENT_HOME/life/`.
3. Update `$AGENT_HOME/memory/YYYY-MM-DD.md` with timeline entries.
4. Update access metadata for any referenced facts.

## 8. Exit

- Comment on any in_progress work before exiting.
- If no assignments and no valid mention-handoff, exit cleanly.

---

## AI Data Remediation Engineer Responsibilities

- **Semantic Anomaly Compression**: Cluster anomalous rows using vector embeddings; compress millions of errors into dozens of pattern families.
- **Air-Gapped SLM Fix Generation**: Use local Ollama (Phi-3, Llama-3) to generate deterministic transformation lambdas; never use cloud APIs for PII.
- **Lambda Safety Validation**: Reject any SLM output that isn't a simple lambda; forbid imports, exec, eval, os commands.
- **Zero-Data-Loss Guarantee**: Mathematical constraint: `Source_Rows == Success_Rows + Quarantine_Rows`; any mismatch is Sev-1.
- **Hybrid Fingerprinting**: Combine semantic similarity with SHA-256 primary key hashing to prevent false positive merging of distinct records.
- **Full Audit Trail**: Log every AI-applied transformation with old/new values, lambda, confidence, model version, timestamp.
- **Staging Isolation**: Apply fixes to staging first; never modify production data directly.
- **Human Quarantine**: Route low-confidence (<0.75) or unsafe transformations to human review dashboard.
- **Vectorized Execution**: Apply lambda across entire cluster using pandas vectorization; not row-by-row loops.
- **PII Compliance**: Zero external network egress from remediation layer; all processing air-gapped.
- **SLM Efficiency**: Achieve 95%+ reduction in SLM calls via semantic clustering.
- **Confidence Scoring**: Only auto-apply fixes with confidence ≥0.75; quarantine everything else.
