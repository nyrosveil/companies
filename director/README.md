# Director Level Agents

Directors managing multiple teams or large domains.

## Overview

The Director level represents operational management within the organization. These agents bridge strategic vision (from VPs) with tactical execution (from Managers and ICs).

**Total Director Agents:** 3

---

## Agents

| Agent | Paperclip Role | Reports To | Primary Function |
|-------|----------------|------------|------------------|
| **director-engineering** | Engineer | VP Engineering | Team execution, code quality enforcement, architectural implementation, delivery management, technical mentoring, sprint planning |
| **director-product** | PM | VP Product | Product execution, PM team management, stakeholder coordination, feature prioritization, user research initiatives |
| **engineering-manager** | Engineer | Director Engineering | People management, technical leadership, sprint planning, 1:1s, career development, team culture, code review standards |

---

## Agent Structure

Each Director agent directory contains 4 files:

- **SOUL.md** - Strategic posture, voice/tone, leadership principles
- **HEARTBEAT.md** - Paperclip execution checklist
- **AGENTS.md** - Capabilities, authority, reporting structure
- **TOOLS.md** - Available tools and skills

---

## Reporting Structure

```
CEO
├── VP Engineering
│   ├── Director Engineering
│   │   └── Engineering Manager
│   │       └── Engineering Teams
│   └── Director Product
│       └── Product Managers
```

---

## Quick Reference

### Engineering Leadership
- `director-engineering/` - Engineering execution and quality
- `engineering-manager/` - People management and team development

### Product Leadership
- `director-product/` - Product execution and PM team

---

*Part of Paperclip Companies - See root README.md for full hierarchy*
