# Agent Directory

Browse and search agents from the Paperclip Companies talent repository.

## Description

Search and discover agents from the enterprise agent directory.

## Trigger

- "find agent", "search agent", "hire agent"
- "who can do", "looking for", "need an agent"
- "list agents", "agent directory"

## Tools

### search_agents

Search agents by skills, role, or keywords.

**Parameters:**
- `query` (string): Search terms
- `role` (string, optional): Paperclip role filter
- `department` (string, optional): default | vp | director | engineer

**Example:**
```
search_agents("React frontend")
search_agents(role="Engineer", department="engineering")
```

### get_agent_profile

Read full agent profile.

**Parameters:**
- `agent_name` (string): Agent directory name

**Example:**
```
get_agent_profile("ai-engineer")
```

### list_by_role

List agents by Paperclip role.

**Parameters:**
- `role` (string): CEO | CTO | Engineer | General | etc.

### list_by_department

List agents by organizational level.

**Parameters:**
- `department` (string): default | vp | director | engineer

### recommend

Get agent recommendation.

**Parameters:**
- `requirements` (string): What you need
- `context` (string, optional): Additional context

## Data Source

**Index**: `references/agents-index.yaml`

Pre-built index of all 50 agents with metadata, stats, and skill-based indices for fast lookup.

## Repository

```
/companies/
├── default/       # C-Suite + core ICs (12 agents)
├── vp/            # VP level (12 agents)
├── director/      # Directors (3 agents)
└── engineer/      # Engineers (23 agents)
```

Each agent has: SOUL.md, HEARTBEAT.md, AGENTS.md, TOOLS.md

## Roles

| Role | Count | Levels |
|------|-------|--------|
| CEO | 1 | C-Suite |
| CTO | 1 | C-Suite |
| CFO | 1 | C-Suite |
| CMO | 2 | C-Suite/VP |
| PM | 3 | All |
| Engineer | 26 | All |
| DevOps | 3 | IC/VP |
| Researcher | 2 | C-Suite/VP |
| Designer | 1 | IC |
| QA | 1 | IC |
| General | 12 | All |

## Examples

### Find frontend developer
```
User: "Need React developer"

search_agents("React frontend")
→ frontend-developer, mobile-app-builder

get_agent_profile("frontend-developer")
→ React, TypeScript, Vue, Angular
```

### Find security specialist
```
User: "Need security audit"

search_agents("security")
→ security-engineer, vp-information-security, threat-detection-engineer

recommend("security audit")
→ security-engineer
```

### Hire workflow
```
search_agents("AI ML")
→ Select: ai-engineer

get_agent_profile("ai-engineer")
→ Review capabilities

User: "Hire this agent"
→ Use paperclip-create-agent skill
```

## Integration

This skill is for **discovery only**. To instantiate an agent, use the `paperclip-create-agent` system skill.

## References

- Repo: `https://github.com/[org]/paperclip-companies`

## Version

- Created: 2026-03-17
- Agents: 50
- Version: 1.0.0
