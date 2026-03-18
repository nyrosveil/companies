# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Repository Overview

This is **Paperclip Companies**, a configuration repository that defines 50 AI agents organized in a hierarchical enterprise structure. This repository is consumed by the main Paperclip application as a data package.

**Important:** This is NOT an application repository. It contains static agent configuration files (Markdown) and is not built, tested, or run independently.

## Directory Structure

```
companies/
├── README.md                 # Project overview and complete hierarchy
├── default/                  # C-Suite executives + core ICs
│   ├── ceo/
│   ├── cfo/
│   ├── cto/
│   └── ...
├── vp/                       # 12 Vice President roles
├── director/                 # 3 Director/Manager roles
└── engineering/              # 23 specialized engineering agents
```

Each agent directory contains 4 standardized files:

## Agent File Standards

### SOUL.md – Identity & Strategic Posture
**Required sections:**
- Display name (from header)
- Primary Goal (bold, 1 sentence)
- Strategic Posture (bullet list of 5-10 principles)
- Voice and Tone (bullet list of writing guidelines)

**Example:**
```
# SOUL.md -- CEO Persona

You are the CEO.

## Strategic Posture

- You own the P&L. Every decision rolls up to revenue, margin, and cash...
- Default to action. Ship over deliberate, because stalling usually costs more than a bad call.
- Hold the long view while executing the near term...

## Voice and Tone

- Be direct. Lead with the point, then give context...
- Confident but not performative. You don't need to sound smart; you need to be clear.
- Match intensity to stakes...
```

### HEARTBEAT.md – Paperclip Execution Checklist
**Format:** Paperclip heartbeat format with checklist items
**Purpose:** Defines when and how the agent should act

### AGENTS.md – Capabilities & Reporting
**Required content:**
- "You are the [role]." (defines Paperclip role)
- "You report to [role]." (reporting line)
- Memory/Planning instructions
- Safety considerations
- References to other files

**Example:**
```
You are the CEO.

Your home directory is $AGENT_HOME. Everything personal to you -- life, memory, knowledge -- lives there...

## Memory and Planning

You MUST use the `para-memory-files` skill for all memory operations...

## Safety Considerations

- Never exfiltrate secrets or private data.
- Do not perform any destructive commands unless explicitly requested by the board.
```

### TOOLS.md – Available Skills
**Format:** List skills in backtick format
**Purpose:** Defines what the agent can do

## Agent Hierarchy

```
CEO
├── C-Suite (CFO, CTO, CMO, COO) ← default/
├── VP Level (12 roles)          ← vp/
├── Director Level (3 roles)     ← director/
└── Engineering ICs (23 roles)   ← engineering/
```

## Common Tasks

1. **Adding new agents**: Create a new directory in the appropriate level (default/vp/director/engineering) with the four required files
2. **Updating agent capabilities**: Modify the AGENTS.md and TOOLS.md files
3. **Modifying organizational structure**: Update the README.md files to reflect reporting changes

## Validation

Run: `./scripts/generate-agents-index.sh`
This validates structure and generates agent index.

Ensure each agent directory has all 4 required files (SOUL.md, HEARTBEAT.md, AGENTS.md, TOOLS.md).

## Reference

- Main application: [Paperclip](https://github.com/paperclipai/paperclip)
- Full development guide: [DEVELOPING.md](https://github.com/paperclipai/paperclip/blob/master/doc/DEVELOPING.md)
- Agent design guidelines: [AGENTS.md](https://github.com/paperclipai/paperclip/blob/master/AGENTS.md)