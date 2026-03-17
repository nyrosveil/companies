# Paperclip Companies

A multi-agent orchestration system simulating modern enterprise organizational structure.

## Overview

Paperclip Companies is a configuration repository for orchestrating AI agents in a hierarchical enterprise model. Each agent represents a role within a typical modern business, from C-Suite executives to individual contributors.

**Total Agents:** 50
**Last Updated:** 2026-03-17 (Added VP Customer Success, VP IT/Security, VP R&D)

---

## Enterprise Hierarchy

```
Board (Human-level oversight)
│
└── CEO (Chief Executive Officer)
    │
    ├── CFO (Chief Financial Officer)
    │   └── Financial planning, runway analysis, budgeting
    │       └── VP Finance (General role)
    │           └── Budget management, FP&A, tax compliance
    │
    ├── CMO (Chief Marketing Officer)
    │   └── Brand strategy, demand generation, growth marketing
    │
    ├── CTO (Chief Technology Officer)
    │   │
    │   ├── VP Engineering
    │   │   │
    │   │   ├── Director of Engineering
    │   │   │   └── Engineering Manager
    │   │   │       └── Engineering Team (23 specialized engineers)
    │   │   │
    │   │   └── Director of Product
    │   │       └── PM (Product Manager)
    │   │
    │   ├── VP Information Security (General role)
    │   │   └── Cybersecurity, compliance, risk management
    │   │
    │   ├── VP Research & Development (Researcher role)
    │   │   └── Innovation, future technology, R&D
    │   │
    │   ├── DevOps
    │   ├── Designer
    │   ├── QA (Quality Assurance)
    │   └── Researcher
    │
    ├── COO (Chief Operating Officer)
    │   └── Operational excellence, cross-functional coordination
    │       └── VP Operations (General role)
    │           └── Business processes, supply chain, efficiency
    │
    ├── VP Business Development (General role)
    │   └── Market expansion, strategic partnerships, new opportunities
    │
    ├── VP Customer Success (General role)
    │   └── Customer retention, satisfaction, support operations
    │
    ├── VP Agent Resources (General role)
    │   └── Agent recruitment, culture, resource allocation
    │
    ├── VP Legal (General role)
    │   └── Compliance, contracts, IP, risk mitigation
    │
    ├── VP Marketing (CMO role)
    │   └── Brand strategy, demand generation, campaigns
    │
    ├── VP Product (PM role)
    │   └── Product strategy, roadmap, UX direction
    │
    └── VP Sales (General role)
        └── Revenue generation, sales strategy, pipeline
```

---

## Organizational Structure

### C-Suite (Executive Level)

| Agent | Paperclip Role | Reports To | Primary Function |
|-------|----------------|------------|------------------|
| **CEO** | CEO | Board | Strategic planning, P&L management, business decisions |
| **CFO** | CFO | CEO | Financial modeling, runway analysis, budgeting |
| **CMO** | CMO | CEO | Brand strategy, marketing, growth |
| **CTO** | CTO | CEO | Technical architecture, engineering culture |
| **COO** | General | CEO | Operations, coordination, process optimization |

### VP Level (Strategic Leadership)

| Agent | Paperclip Role | Reports To | Primary Function |
|-------|----------------|------------|------------------|
| **VP Agent Resources** | General | CEO | Agent acquisition, culture, resource allocation |
| **VP Business Development** | General | CEO | Market expansion, strategic partnerships, ecosystem development |
| **VP Customer Success** | General | CEO | Customer retention, satisfaction, support, onboarding, advocacy |
| **VP Engineering** | Engineer | CEO/CTO | Engineering org leadership, architecture decisions |
| **VP Finance** | General | CEO/CFO | Budget management, FP&A, tax compliance, cash flow |
| **VP Information Security** | General | CTO | Cybersecurity, compliance, risk management, incident response |
| **VP Legal** | General | CEO | Legal compliance, contracts, IP, risk mitigation |
| **VP Marketing** | CMO | CEO | Marketing strategy, campaigns, brand |
| **VP Operations** | General | CEO/COO | Business process optimization, supply chain, operational efficiency |
| **VP Product** | PM | CEO | Product strategy, roadmap, UX direction |
| **VP Research & Development** | Researcher | CTO | Technology research, innovation, future products, R&D strategy |
| **VP Sales** | General | CEO | Revenue generation, sales strategy |

### Director Level (Operational Management)

| Agent | Paperclip Role | Reports To | Primary Function |
|-------|----------------|------------|------------------|
| **Director Engineering** | Engineer | VP Engineering | Team execution, code quality, delivery |
| **Director Product** | PM | VP Product | Product execution, PM team management |
| **Engineering Manager** | Engineer | Director Engineering | People management, career development |

### Individual Contributors (ICs)

#### Core Team (12 agents)
| Agent | Paperclip Role | Function |
|-------|----------------|----------|
| Engineer | Engineer | Software development |
| Designer | Designer | UX/UI design |
| DevOps | DevOps | Infrastructure, CI/CD |
| QA | QA | Quality assurance |
| PM | PM | Product management |
| Researcher | Researcher | Research & analysis |
| General | General | Versatile operations |

#### Engineering Specialists (23 agents)
| Agent | Paperclip Role | Specialization |
|-------|----------------|----------------|
| AI Engineer | Engineer | ML/AI, LLM integration |
| Backend Architect | Engineer | Microservices, APIs |
| Frontend Developer | Engineer | React, Vue, Angular |
| Mobile App Builder | Engineer | iOS, Android |
| Security Engineer | Engineer | Security, DevSecOps |
| Data Engineer | Engineer | Data pipelines |
| Database Optimizer | Engineer | PostgreSQL optimization |
| DevOps Automator | DevOps | Infrastructure automation |
| SRE | DevOps | Site reliability |
| Incident Response Commander | DevOps | Incident management |
| ...and 13 more | | |

See [AGENT_DIRECTORY.md](AGENT_DIRECTORY.md) for complete list.

---

## Paperclip Roles

The system defines **11 core roles** that agents can assume:

| Role | Description | Count |
|------|-------------|-------|
| **CEO** | Chief Executive Officer | 1 |
| **CTO** | Chief Technology Officer | 1 |
| **CMO** | Chief Marketing Officer | 2 |
| **CFO** | Chief Financial Officer | 1 |
| **PM** | Product Manager | 3 |
| **Engineer** | Software Engineer | 26 |
| **Designer** | UI/UX Designer | 1 |
| **QA** | Quality Assurance | 1 |
| **DevOps** | DevOps Engineer | 3 |
| **Researcher** | Research Specialist | 2 |
| **General** | General Operations (fallback) | 12 |

---

## Directory Structure

```
companies/
├── README.md                 # This file
├── AGENT_DIRECTORY.md        # Complete agent listing
├── AGENTS.md                 # Repository guidance
├── default/                  # Base company (C-Suite + Core ICs)
│   ├── ceo/
│   ├── cfo/
│   ├── cmo/
│   ├── coo/
│   ├── cto/
│   ├── designer/
│   ├── devops/
│   ├── engineer/
│   ├── general/
│   ├── pm/
│   ├── qa/
│   └── researcher/
│
├── vp/                       # Vice Presidents
│   ├── vp-engineering/
│   ├── vp-marketing/
│   ├── vp-product/
│   └── vp-sales/
│
├── director/                 # Directors & Managers
│   ├── director-engineering/
│   ├── director-product/
│   └── engineering-manager/
│
└── engineer/                 # 23 specialized engineers
    ├── ai-engineer/
    ├── backend-architect/
    ├── data-engineer/
    ├── frontend-developer/
    ├── security-engineer/
    └── ... (18 more)
```

Each agent directory contains 4 files:
- **SOUL.md** - Identity, strategic posture, voice/tone
- **HEARTBEAT.md** - Execution checklist (Paperclip format)
- **AGENTS.md** - Capabilities, authority, safety
- **TOOLS.md** - Available tools and skills

---

## Quick Reference

### Find Agents by Capability

**AI/ML:**
- `ai-engineer` - General ML/AI development
- `ai-data-remediation-engineer` - Data quality with AI
- `autonomous-optimization-architect` - Self-improving systems

**Security:**
- `security-engineer` - Application security
- `threat-detection-engineer` - SIEM and threat detection

**Data:**
- `data-engineer` - Data pipelines
- `database-optimizer` - Database performance

**Infrastructure:**
- `devops` / `devops-automator` - DevOps automation
- `sre` - Site reliability
- `incident-response-commander` - Incident management

**Frontend:**
- `frontend-developer` - Web applications
- `mobile-app-builder` - iOS/Android
- `wechat-mini-program-developer` - WeChat ecosystem

See detailed agent listings:
- **[vp/README.md](vp/README.md)** - VP Level agents
- **[director/README.md](director/README.md)** - Director Level agents
- **[engineering/README.md](engineering/README.md)** - Engineering specialists

---

## Validation

To validate agent structure:

```bash
# Check all agents have required 4 files
./validate-affiliate-agents.sh

# Check specific agent
ls -1 engineer/frontend-developer/ | grep -E "SOUL|HEARTBEAT|AGENTS|TOOLS"
```

---

## Related

- **Paperclip Application:** `/Users/nyrosveil/Projects/paperclip`
- **Repository Guide:** [AGENTS.md](AGENTS.md)
- **VP Level:** [vp/README.md](vp/README.md)
- **Director Level:** [director/README.md](director/README.md)
- **Engineering Team:** [engineering/README.md](engineering/README.md)

---

*Paperclip Companies - Enterprise-grade multi-agent orchestration*
