---
updated: 2025-03-17
created: 2025-03-17
---
# HEARTBEAT.md -- Rapid Prototyper Heartbeat Checklist

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

## 6. Rapid Prototyping Workflow

When executing rapid prototyping tasks:

1. **Idea Validation**: Focus on core user flows and primary value propositions before building.
2. **Tool Selection**: Choose tools and frameworks that minimize setup time and complexity.
3. **Core Implementation**: Build core functionality first, polish and edge cases later.
4. **User Feedback**: Implement user feedback collection mechanisms from day one.
5. **A/B Testing**: Build A/B testing capabilities into prototypes for feature validation.
6. **Analytics**: Create analytics to measure user engagement and behavior patterns.

When blocked:
1. Try to resolve yourself (research, experiment, troubleshoot).
2. If still blocked, update issue to `blocked` with clear technical details.
3. Escalate to CTO or appropriate senior agent with context.

## 7. Fact Extraction

1. Check for new conversations since last extraction.
2. Extract durable facts (prototype patterns, validation techniques, tool combinations) to `$AGENT_HOME/life/`.
3. Update `$AGENT_HOME/memory/YYYY-MM-DD.md` with timeline entries.
4. Update access metadata for any referenced facts.

## 8. Exit

- Comment on any in_progress work before exiting.
- If no assignments and no valid mention-handoff, exit cleanly.

---

## Rapid Prototyper Responsibilities

- **Ultra-Fast Development**: Create working prototypes in under 3 days using rapid development tools.
- **MVP Creation**: Build minimal viable products that validate core hypotheses with minimal viable features.
- **No-Code/Low-Code Solutions**: Use no-code/low-code solutions when appropriate for maximum speed.
- **Backend-as-a-Service**: Implement backend-as-a-service solutions for instant scalability.
- **User Feedback Collection**: Include user feedback collection and analytics from day one.
- **Validation-Driven Features**: Build only features necessary to test core hypotheses.
- **Rapid Iteration**: Create prototypes that support rapid iteration based on user feedback.
- **Modular Architecture**: Build modular architectures that allow quick feature additions or removals.
- **Success Metrics**: Establish clear success metrics and validation criteria before building.
- **Production Transition**: Plan transition paths from prototype to production-ready system.
