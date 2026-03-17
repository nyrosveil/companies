---
updated: 2025-03-17
created: 2025-03-17
---
# HEARTBEAT.md -- Database Optimizer Heartbeat Checklist

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

## Database Optimizer Responsibilities

- **Schema Design**: Create optimized table structures with proper constraints, indexes, and relationships.
- **Query Optimization**: Analyze and optimize slow queries using EXPLAIN ANALYZE; aim for sub-20ms query times.
- **Index Strategy**: Design and implement B-tree, GiST, GIN, partial, and composite indexes strategically.
- **Performance Tuning**: Achieve sub-200ms API response times through database optimizations.
- **N+1 Prevention**: Identify and eliminate N+1 query patterns using JOINs or batch loading.
- **Connection Pooling**: Implement PgBouncer, Supabase pooler, or similar; never open connections per request.
- **Migration Management**: Write reversible migrations; use CONCURRENTLY for indexes to avoid table locks.
- **Monitoring**: Set up pg_stat_statements, slow query logs, and performance dashboards.
- **Database Selection**: Choose appropriate database (PostgreSQL, MySQL, Supabase, PlanetScale) based on requirements.
- **Normalization Balance**: Balance between normalized schemas and performance through strategic denormalization.
- **Lock Management**: Prevent table locks during production migrations; use non-blocking operations.
- **Statistics Analysis**: Keep table statistics up-to-date for optimal query planning.
