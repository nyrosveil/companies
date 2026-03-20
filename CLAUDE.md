# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Paperclip Companies** organizational structure repository containing specialized AI agents for a simulated corporate environment. The repository houses 50+ AI agents organized across multiple hierarchical levels:

- **CEO** (1 agent)
- **VP Level** (12 agents) - Strategic leadership across major functional areas
- **Director Level** (3 agents) - Operational management
- **Engineering Team** (23 agents) - Technical specialists and individual contributors
- **Other Functional Agents** (15+ agents) - CMO, CFO, PM, QA, Researcher, etc.

## Development Commands

### Repository Management
```bash
git status --porcelain          # Check working tree status
git diff --no-pager            # View unstaged changes
git log --oneline -10          # View recent commit history
git commit -m "$(cat <<'EOF'\n<type>: <description>\n\n<optional body>\nEOF\n)"                    # Create commit with conventional format
git push -u origin <branch>    # Push to remote with upstream tracking
gh pr create --title "<title>" --body "$(cat <<'EOF'\n## Summary\n<1-3 bullet points>\n\n## Test plan\n[Bulleted markdown checklist of TODOs for testing]\n\n\ud83e� Generated with [Claude Code](https://claude.com/claude-code)\nEOF\n)"                   # Create GitHub PR
```

### File Operations
```bash
find . -name "*.md" -o -name "*.json" | head -20    # Find documentation and config files
ls -la                                             # List directory contents with details
grep -r "pattern" .                                # Search for patterns in files
```

## Architecture & Structure

### Agent Organization
Each agent has a dedicated directory containing 4 files:
- `SOUL.md` - Identity, specializations, voice/tone
- `HEARTBEAT.md` - Execution checklist
- `AGENTS.md` - Capabilities, authority, reporting structure
- `TOOLS.md` - Technical tools and skills

### Hierarchy Levels
1. **VP Level** - Strategic leadership (12 agents)
2. **Director Level** - Operational management (3 agents)
3. **Engineering Team** - Technical specialists (23 agents)
4. **Functional Agents** - Domain specialists (CMO, CFO, PM, etc.)

### Key Directories
- `engineering/` - 23 specialized engineering agents
- `vp/` - 12 VP-level strategic agents
- `director/` - 3 director-level operational agents
- `default/` - Default agent configurations

## Agent Access Patterns

### For Specialized Tasks
- **Engineering:** Use `engineering/` agents based on technology stack
- **Strategic:** Use `vp/` agents for high-level decisions
- **Operational:** Use `director/` agents for execution
- **Domain-specific:** Use functional agents (e.g., `default/cmo/` for marketing)

### Parallel Execution
When facing multiple independent tasks, launch agents in parallel:
```bash
# GOOD: Parallel execution
Launch 3 agents in parallel:\n1. Agent 1: Security analysis of auth module\n2. Agent 2: Performance review of cache system\n3. Agent 3: Type checking of utilities\n```

## Development Guidelines

### Code Style
- **Functional Programming:** Prefer pure functions over OOP
- **Immutability:** Create new objects, never mutate existing ones
- **Small Files:** 200-400 lines typical, 800 max
- **Single Responsibility:** Functions should be single-purpose and short (<30 lines)

### Error Handling
- **Explicit Failure:** Raise specific error types, never silently ignore exceptions
- **Root Cause:** Fix the root cause, not symptoms
- **Comprehensive:** Handle errors at every level with user-friendly messages

### Security
- **Secrets:** Never hardcode API keys or secrets
- **Input Validation:** Validate all user input at system boundaries
- **Authentication:** Verify auth/authorization before access

## Testing Requirements

### Coverage Minimum: 80%
- **Unit Tests:** Individual functions, utilities, components
- **Integration Tests:** API endpoints, database operations
- **E2E Tests:** Critical user flows

### TDD Workflow
1. Write test first (RED)
2. Run test - it should FAIL
3. Write minimal implementation (GREEN)
4. Run test - it should PASS
5. Refactor (IMPROVE)
6. Verify coverage (80%+)

## Git Workflow

### Commit Message Format
```
<type>: <description>

<optional body>
```
Types: feat, fix, refactor, docs, test, chore, perf, ci

### Pull Request Process
1. Analyze full commit history (not just latest commit)
2. Use `git diff [base-branch]...HEAD` to see all changes
3. Draft comprehensive PR summary
4. Include test plan with TODOs
5. Push with `-u` flag if new branch

## Agent Orchestration

### Available Agents
Located in `~/.claude/agents/`:
- `planner` - Implementation planning for complex features
- `architect` - System design and architectural decisions
- `tdd-guide` - Test-driven development enforcement
- `code-reviewer` - Code review after writing code
- `security-reviewer` - Security analysis before commits
- `build-error-resolver` - Fix build errors when they occur

### Immediate Usage (No Prompt Needed)
1. Complex features - Use **planner** agent
2. Code just written - Use **code-reviewer** agent
3. Bug fix/new feature - Use **tdd-guide** agent
4. Architectural decision - Use **architect** agent

## Multi-Perspective Analysis

For complex problems, use split role sub-agents:
- Factual reviewer
- Senior engineer
- Security expert
- Consistency reviewer
- Redundancy checker

## Build & Development

### Context Management
- Use context-mode MCP tools for large output (>20 lines)
- Avoid last 20% of context window for large-scale refactoring
- Use `ctx_batch_execute` for research tasks

### Performance Optimization
- **Haiku 4.5:** Quick lookups, lightweight agents
- **Sonnet 4.6:** Standard development work
- **Opus 4.5:** Complex architectural decisions, maximum reasoning

## Troubleshooting

### Build Failures
1. Use **build-error-resolver** agent
2. Analyze error messages
3. Fix incrementally
4. Verify after each fix

### Test Failures
1. Use **tdd-guide** agent
2. Check test isolation
3. Verify mocks are correct
4. Fix implementation, not tests (unless tests are wrong)

## Security Guidelines

### Mandatory Checks Before Commit
- [ ] No hardcoded secrets
- [ ] All user inputs validated
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection enabled
- [ ] Authentication/authorization verified
- [ ] Rate limiting on endpoints
- [ ] Error messages don't leak sensitive data

### Security Response Protocol
If security issue found:
1. STOP immediately
2. Use **security-reviewer** agent
3. Fix CRITICAL issues before continuing
4. Rotate any exposed secrets
5. Review entire codebase for similar issues

## Hooks System

### Auto-Accept Permissions
Use with caution:
- Enable for trusted, well-defined plans
- Disable for exploratory work
- Never use dangerously-skip-permissions flag
- Configure `allowedTools` in `~/.claude.json` instead

## File Organization Principles

### High Cohesion, Low Coupling
- Many small files > few large files
- Organize by feature/domain, not by type
- Extract utilities from large modules
- 200-400 lines typical, 800 max

### Documentation
- Code is the primary documentation
- Keep docstrings in-place (JSDoc/Google Style)
- Store knowledge as current state, not historical changelog

## Quick Reference

### By Technology Stack
- **AI/ML:** ai-engineer, ai-data-remediation-engineer, autonomous-optimization-architect
- **Backend:** backend-architect, software-architect, database-optimizer
- **Data:** data-engineer
- **DevOps:** devops-automator, sre, incident-response-commander, git-workflow-master
- **Frontend:** frontend-developer, mobile-app-builder, senior-developer
- **Mobile/Platform:** mobile-app-builder, wechat-mini-program-developer, feishu-integration-developer
- **Security:** security-engineer, threat-detection-engineer
- **Specialized:** embedded-firmware-engineer, solidity-smart-contract-engineer, rapid-prototyper

---

*Part of Paperclip Companies - See root README.md for full hierarchy*