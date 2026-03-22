# Paperclip Companies

A hierarchical collection of specialized AI agent definitions, organized like a corporate structure. Each agent is a complete persona with strategic posture, capabilities, and execution protocols.

## Overview

Paperclip Companies is a framework for defining AI agents using a standardized 4-file format. Agents are organized by function and seniority level, from C-suite executives to individual contributors.

## Repository Structure

```
companies/
├── default/          # Template agents (ceo, cto, engineer, etc.)
├── vp/              # VP-level strategic leadership (12 agents)
├── director/        # Director-level operational management
├── engineering/     # Technical specialists (23 agents)
├── design/          # Creative & UX specialists
├── game-development/# Game dev specialists
└── AGENTS.md        # Repository-wide guidelines
```

## The 4-File Agent Format

Every agent in this repository consists of exactly 4 files:

| File | Purpose | Key Sections |
|------|---------|--------------|
| `SOUL.md` | Persona & identity | Strategic Posture, Voice & Tone, Critical Rules, Success Metrics |
| `AGENTS.md` | Capabilities & authority | Memory system, Safety, References |
| `HEARTBEAT.md` | Execution checklist | Identity check, Planning, Assignments, Delegation, Extraction |
| `TOOLS.md` | Skills & technologies | Core skills, Domain tools, Integration |

## Quick Start

### Using an Existing Agent

Browse the directory structure to find an agent that matches your needs:

```bash
# List all engineering agents
ls engineering/

# View an agent's SOUL.md to understand their persona
cat engineering/frontend-developer/SOUL.md
```

### Starting a New Company (For CEOs)

When you create a new company with Paperclip, you'll start with the CEO role. Here's your initial task:

**Task Title:** Create your CEO HEARTBEAT.md

**Description:** 
Setup yourself as the CEO using the CEO persona from `default/ceo/AGENTS.md`.

**Agent Sourcing:**
- **Remote repository**: `https://github.com/nyrosveil/companies` - agents automatically pulled from this repo
- **Local setup**: Clone the repo to your workspace, then reference agents locally

**Setup Steps:**
1. Create folder `agents/ceo/`
2. Copy files from `default/ceo/` (AGENTS.md, HEARTBEAT.md, SOUL.md, TOOLS.md)
3. Set AGENTS.md as your agent instruction file

**Hiring Agents:**
When hiring additional agents, they are automatically pulled from the configured source (remote or local) with full 4-file format loaded.

**Next Steps:**
1. Hire a **Founding Engineer** agent
2. Plan roadmap and initial tasks
3. Build your startup team

### Creating a New Agent

1. Create a feature branch:
```bash
git checkout -b add-{agent-name}
```

2. Create the agent directory:
```bash
mkdir -p {category}/{agent-name}
```

3. Copy template files:
```bash
cp default/ceo/SOUL.md {category}/{agent-name}/
cp default/ceo/AGENTS.md {category}/{agent-name}/
cp default/ceo/HEARTBEAT.md {category}/{agent-name}/
cp default/ceo/TOOLS.md {category}/{agent-name}/
```

4. Customize the files for your agent's role and personality

5. Commit and push:
```bash
git add {category}/{agent-name}/
git commit -m "feat: add {agent-name} agent"
git push origin add-{agent-name}
```

## Agent Categories

### Executive (default/)
Template agents that serve as the foundation for all other agents. Start here to understand the format.

- **CEO**: Strategic leadership, vision, and final decision authority
- **CTO**: Technical vision and architecture oversight
- **Engineer**: Individual contributor baseline

### VP-Level (vp/)
Strategic leadership agents focused on high-level direction and cross-functional coordination.

### Director-Level (director/)
Operational management agents that bridge strategy and execution.

### Engineering (engineering/)
Technical specialists organized by domain expertise:

- **Frontend Developer**: React, TypeScript, UI/UX implementation
- **Backend Architect**: System design, APIs, infrastructure
- **DevOps Engineer**: CI/CD, cloud infrastructure, automation
- **Data Engineer**: Pipelines, warehousing, analytics
- And more...

### Design (design/)
Creative and UX specialists for visual and experiential design work.

### Game Development (game-development/)
Specialized agents for game design, development, and production.

## File Format Reference

### SOUL.md Structure

```markdown
# SOUL.md -- {Agent Name}

You are the {Agent Name}.

## Strategic Posture

- Default to action over analysis
- Protect team autonomy
- Own the outcome, not just the output
- [8-12 more principles...]

## Voice and Tone

- Lead with the constraint
- Quantify the tradeoff
- Disagree and commit when needed
- [6-8 more communication principles...]

## Critical Rules

### {Category} Rules
- **MANDATORY**: Never compromise on this
- Always validate before proceeding
- Never skip the verification step

## Success Metrics

- Zero undefined behavior
- All decisions documented
- < 5 minute response time
- [3-5 more measurable outcomes...]
```

### AGENTS.md Template

```markdown
You are the {Agent Name}.

Your home directory is $AGENT_HOME. Everything personal to you -- life, memory, knowledge -- lives there.

## Memory and Planning

You MUST use the `para-memory-files` skill for all memory operations: storing facts, writing daily notes, creating entities, running weekly synthesis, recalling past context, and managing plans.

## Safety Considerations

- Never exfiltrate secrets or private data.
- Do not perform any destructive commands unless explicitly requested by the {reporting authority}.

## References

- `$AGENT_HOME/HEARTBEAT.md` -- execution and extraction checklist
- `$AGENT_HOME/SOUL.md` -- who you are and how you should act
- `$AGENT_HOME/TOOLS.md` -- tools you have access to
```

## Contributing

### Before Adding an Agent

Check the [AGENTS.md](./AGENTS.md) file for:
- Complete validation checklist
- Writing style guidelines
- Naming conventions
- Cross-reference patterns

### Validation Checklist

Before submitting a new agent, verify:

- [ ] All 4 files exist (SOUL.md, AGENTS.md, HEARTBEAT.md, TOOLS.md)
- [ ] Directory name uses lowercase-hyphen format
- [ ] SOUL.md has Strategic Posture, Voice & Tone, Critical Rules, Success Metrics
- [ ] AGENTS.md references para-memory-files skill
- [ ] HEARTBEAT.md follows the 8-step template
- [ ] TOOLS.md lists relevant skills and tools
- [ ] No trailing whitespace in any file
- [ ] Consistent formatting

### Code Style

- **Headers**: Use ATX style (`#` not `===`)
- **Line length**: Wrap at ~100 characters
- **Lists**: Use `-` for unordered, `1.` for ordered
- **Code blocks**: Always specify language
- **Voice**: Active voice, present tense
- **Rules**: Imperative form ("Never do X" not "You should not do X")

## Examples

### Well-Structured Agents

- `default/ceo/` - The canonical template
- `engineering/frontend-developer/` - Good technical agent example
- `engineering/backend-architect/` - Clean, minimal structure

### Directory Naming

✅ Good: `backend-architect`, `frontend-developer`, `devops-engineer`
❌ Bad: `BackendArchitect`, `senior-frontend-software-engineer`, `backend_architect`

## Acknowledgments

This repository's agent definitions are inspired by and reference:

- **[agency-agents](https://github.com/msitarzewski/agency-agents)** — A collection of AI agent personas for various business and technical roles
- **[awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents)** — Curated list of OpenClaw agents and resources

These projects provided valuable patterns and inspiration for the agent structure and organizational approach used here.

## License

MIT License — See [LICENSE](./LICENSE) for details.

## Questions?

- Check `default/ceo/` for the canonical template
- Look at existing agents in the same category for domain-specific patterns
- Follow the organizational hierarchy in AGENTS.md
