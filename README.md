# Paperclip Companies

*A simulated corporate environment with specialized AI agents organized in hierarchical teams*

---

## Overview

Paperclip Companies is an organizational structure repository that models a complete corporate environment using specialized AI agents. Each agent represents a specific role with defined responsibilities, expertise areas, and decision-making authority, all working together through the Paperclip coordination framework.

**Total Agents**: 60+ across 4 organizational levels
**Structure**: Hierarchical reporting with clear authority lines
**Purpose**: Demonstrate multi-agent collaboration in a realistic corporate setting

---

## Organizational Hierarchy

```
CEO (1)
│
├─ VP Level (12) - Strategic Leadership
│   ├─ VP-Product
│   ├─ VP-Engineering
│   ├─ VP-Marketing
│   ├─ VP-Sales
│   ├─ VP-Customer-Success
│   ├─ VP-Finance
│   ├─ VP-Operations
│   ├─ VP-Research-Development
│   ├─ VP-Business-Development
│   ├─ VP-Information-Security
│   ├─ VP-Legal
│   └─ VP-Agent-Resources
│
├─ Director Level (4) - Operational Management
│   ├─ Director-Design (NEW)
│   ├─ Director-Engineering
│   ├─ Director-Product
│   └── Engineering-Manager
│
├─ Engineering Team (23) - Technical Specialists
│   ├─ AI/ML: autonomous-optimization-architect, ai-data-remediation-engineer
│   ├─ Backend: backend-architect, software-architect, database-optimizer
│   ├─ DevOps: devops-automator, sre, incident-response-commander
│   ├─ Frontend: frontend-developer, senior-developer, mobile-app-builder
│   ├─ Platform: embedded-firmware-engineer, wechat-mini-program-developer
│   ├─ Security: security-engineer, threat-detection-engineer
│   └─ Specialized: solidity-smart-contract-engineer, rapid-prototyper
│
├─ Design Team (8) - Creative & Experience Specialists
│   ├─ UX/UI Focus:
│   │   ├── UX Architect
│   │   ├── UX Researcher
│   │   ├── UI Designer
│   │   └── Visual Storyteller
│   └─ Technical/Graphics Focus:
│       ├── Inclusive Visuals Specialist
│       ├── Whimsy Injector
│       ├── Image Prompt Engineer
│       └── Brand Guardian
│
└─ Other Functional Agents (~12) - Domain Specialists
    ├─ Executive: ceo, cfo, cmo, coo, cto
    ├─ Operations: pm, qa, researcher, engineer, devops, designer, general
```

---

## Quick Navigation

| Directory | Purpose | Agent Count |
|-----------|---------|-------------|
| `vp/` | VP-level strategic leadership | 12 |
| `director/` | Director-level operational management | 4 |
| `engineering/` | Technical specialists and ICs | 23 |
| `design/` | Creative, UX, and brand specialists | 8 |
| `default/` | Template agents for reference | 12 |

---

## Agent Structure

Each agent follows the **Paperclip 4-file format**:

```
agent-directory/
├── SOUL.md         # Identity, personality, strategic posture
├── HEARTBEAT.md    # Execution checklist, workflow processes
├── AGENTS.md       # Authority, reporting, relationships
└── TOOLS.md        # Skills, technologies, tools
```

### File Purpose

- **SOUL.md**: Who you are - role definition, core responsibilities, voice & tone, decision framework
- **HEARTBEAT.md**: How you work - execution checklist, fact extraction, quality gates
- **AGENTS.md**: Your authority - reporting structure, decision rights, delegation framework
- **TOOLS.md**: What you can do - skills, tools, platforms, best practices

---

## Recent Updates

### 2026-03-20: Design Team Conversion
**Added 9 new agent directories** to convert standalone design agents to Paperclip format:

**New Director Role**:
- `director/design-director/` - Strategic leadership for all design functions, reports to VP-Product

**New Specialist Agents**:
- `design/ux-architect/` - CSS architecture, design systems, responsive layouts
- `design/ux-researcher/` - User research, usability testing, insights
- `design/ui-designer/` - Component libraries, accessibility, pixel-perfect specs
- `design/visual-storyteller/` - Video, data viz, photography, cross-platform content
- `design/inclusive-visuals-specialist/` - AI bias mitigation, cultural accuracy
- `design/whimsy-injector/` - Micro-interactions, gamification, Easter eggs
- `design/image-prompt-engineer/` - AI prompt engineering, photography expertise
- `design/brand-guardian/` - Brand strategy, governance, trademark protection

**Archive Created**: Original 8 standalone `.md` files moved to `design/legacy-design-docs/`

---

## Getting Started

### For New Contributors

1. **Understand the structure**: Read this README and explore the directory organization
2. **Pick an agent**: Choose based on your task's domain (engineering, design, strategy)
3. **Review the agent's files**: Start with `SOUL.md` to understand their role
4. **Check HEARTBEAT**: See how they execute work and produce deliverables
5. **Coordinate**: Use the Paperclip control plane to assign tasks and orchestrate

### For Paperclip Integration

All agents are configured to work with the Paperclip coordination system:

- Each agent has a home directory (`$AGENT_HOME`)
- Agents reference `para-memory-files` skill for knowledge management
- Execution follows heartbeat checklists
- Cross-agent coordination via delegation frameworks
- Fact extraction into memory stores for institutional knowledge

### For Development Tasks

```bash
# Explore agent capabilities
ls vp/ director/ engineering/ design/

# Read specific agent definition
cat design/ux-architect/SOUL.md
cat engineering/frontend-developer/TOOLS.md

# Check agent relationships
cat director/design-director/AGENTS.md
```

---

## Key Design Principles

### Organizational Clarity
- **Clear reporting lines**: Every agent knows who they report to and who reports to them
- **Specialized roles**: One agent = one clear domain of expertise
- **Minimal overlap**: Responsibilities are distinct and well-bounded

### Interoperability
- **Standard format**: All agents use the same 4-file structure
- **Shared skills**: Common skills like `para-memory-files` enable coordination
- **Delegation patterns**: Directors delegate to specialists; cross-functional collaboration documented

### Scalability
- **Flat where possible**: Specialists report to directors, no unnecessary layers
- **Composable teams**: New agents can be added without restructuring
- **Clear interfaces**: AGENTS.md defines authority boundaries

---

## Development Commands

### Repository Management
```bash
git status --porcelain          # Check working tree
git diff --no-pager             # View unstaged changes
git log --oneline -10           # Recent commit history
```

### File Exploration
```bash
find . -name "*.md" -o -name "*.json" | head -20
ls -la vp/ director/ engineering/ design/
```

### Search Patterns
```bash
grep -r "paperclip" .           # Find Paperclip references
grep -r "reports to" .          # Find reporting relationships
```

---

## Architecture Highlights

### Agent Categories

**Strategic (VP Level)**: Set direction, allocate resources, make high-level decisions
**Operational (Director Level)**: Execute strategy, manage teams, coordinate functions
**Technical (Engineering)**: Build and maintain systems, solve technical problems
**Creative (Design)**: User experience, visual design, brand, content creation
**Domain (Default)**: Cross-functional specialists (PM, QA, Researcher, etc.)

### Coordination Patterns

- **Top-down**: VPs set strategy, Directors plan execution, Agents execute
- **Cross-functional**: Agents coordinate across teams for integrated deliverables
- **Parallel execution**: Independent tasks can run simultaneously
- **Quality gates**: HEARTBEAT checklists ensure consistent execution

---

## Contributing

### Adding a New Agent

1. **Choose category**: VP, Director, Engineering, Design, or Default
2. **Create directory**: `mkdir -p [category]/[agent-name/`
3. **Create 4 files**: Use existing agents as templates
4. **Define relationships**: Set reporting lines in AGENTS.md
5. **Update documentation**: Add to README and relevant quick-ref files

### Agent Creation Best Practices

- Follow the 4-file structure exactly
- Use existing agents as templates for tone and depth
- Define clear, bounded responsibilities
- Document relationships and authority explicitly
- Include practical skills and tools knowledge
- Add safety considerations appropriate to the role

---

## Resources

- **CLAUDE.md** - Claude Code specific guidance for this repository
- **Agent SOUL.md files** - Role definitions and capabilities
- **Agent HEARTBEAT.md files** - Execution processes and checklists

---

## License & Usage

This repository is a **simulated organizational structure** for demonstrating multi-agent AI coordination. Agents are designed to work with the Paperclip control plane for task orchestration and knowledge management.

---

**Maintained by**: The Paperclip Companies architecture team
**Last updated**: 2026-03-21
**Total agents**: 60+
**Levels**: CEO → VP → Director → Engineering/Design/Functional ICs

---

*Building the future of multi-agent collaboration, one specialized role at a time.*