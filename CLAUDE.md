# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a multi-agent organizational system that implements a complete C-suite and functional team structure using the PARA-based agent coordination framework. The project establishes a company simulation with specialized agent personas for different business roles.

## Project Structure

```
companies/
├── default/                    # Agent home directories (PARA structure)
│   ├── ceo/                  # Chief Executive Officer
│   ├── cfo/                  # Chief Financial Officer
│   ├── cto/                  # Chief Technology Officer
│   ├── cmo/                  # Chief Marketing Officer
│   ├── pm/                   # Product Manager
│   ├── engineer/             # Software Engineer
│   ├── designer/             # UX/UI Designer
│   ├── devops/               # Operations/Infrastructure
│   ├── qa/                   # Quality Assurance
│   ├── researcher/           # Research/Analysis
│   └── general/              # General/Administrative
├── .omc/                     # Project memory and state tracking
├── README.md                 # Project overview
└── CLAUDE.md                 # This file
```

## Agent Personas

Each agent has three core files:
- `SOUL.md` - Persona definition and strategic posture
- `HEARTBEAT.md` - Execution checklist and coordination protocols
- `AGENTS.md` - Agent capabilities and responsibilities
- `TOOLS.md` - Available tools and skills

## Development Commands

### Agent Operations
```bash
# Initialize or update agent configurations
para-memory-files update-agent <role>

# Run agent heartbeat check
para-memory-files heartbeat <role>

# Access agent memory
para-memory-files recall <role> <topic>
```

### Project Management
```bash
# Create new agent persona
para-memory-files create-agent <role>

# Generate planning documents
para-memory-files plan <topic>

# Run weekly synthesis
para-memory-files synthesize
```

### Memory Operations
```bash
# Store facts in agent memory
para-memory-files store <agent> <fact>

# Retrieve agent context
para-memory-files recall <agent> <context>

# Update agent persona
para-memory-files update-persona <agent> <persona-content>
```

## Key Architecture Patterns

### PARA-Based Organization
- **Projects**: Active initiatives and tasks
- **Areas**: Ongoing responsibilities (like each agent role)
- **Resources**: Reference materials and documentation
- **Archives**: Completed work and historical data

### Agent Coordination
- Each agent operates autonomously with defined responsibilities
- HEARTBEAT.md provides execution checklists for coordination
- PARA memory system enables knowledge sharing and context persistence
- Multi-agent collaboration through defined interfaces and protocols

### Persona-Driven Development
- Each agent has a distinct strategic posture and voice
- SOUL.md defines decision-making frameworks and values
- Agents maintain consistent behavior through persona definitions
- Coordination happens through structured communication protocols

## Testing and Validation

### Agent Validation
```bash
# Validate agent configuration
para-memory-files validate <agent>

# Test agent coordination
para-memory-files test-coordination <scenario>

# Verify memory persistence
para-memory-files verify-memory <agent>
```

### System Testing
```bash
# Run full system integration test
para-memory-files integration-test

# Validate PARA structure
para-memory-files validate-structure

# Test agent communication
para-memory-files test-communications
```

## Common Development Tasks

### Creating New Agents
1. Create agent directory in `default/`
2. Generate SOUL.md, HEARTBEAT.md, AGENTS.md, TOOLS.md
3. Configure memory and coordination protocols
4. Add to system coordination

### Updating Agent Personas
1. Modify SOUL.md with strategic posture updates
2. Update HEARTBEAT.md with new execution checklists
3. Revise AGENTS.md for capability changes
4. Test coordination impacts

### Memory System Operations
1. Use para-memory-files for all memory operations
2. Follow atomic fact schemas for data consistency
3. Implement memory decay rules for relevance
4. Maintain qmd recall for query management

## Build and Deployment

### System Initialization
```bash
# Initialize PARA structure
para-memory-files init-project

# Set up agent coordination
para-memory-files setup-coordination

# Configure memory system
para-memory-files configure-memory
```

### Deployment
```bash
# Deploy agent system
para-memory-files deploy

# Validate deployment
para-memory-files validate-deployment

# Run health checks
para-memory-files health-check
```

## Configuration Files

- `.omc/project-memory.json` - System memory and state tracking
- `default/*/SOUL.md` - Agent persona definitions
- `default/*/HEARTBEAT.md` - Execution protocols
- `default/*/AGENTS.md` - Agent capabilities
- `default/*/TOOLS.md` - Available tools and skills

## Important Notes

- All agent operations should use the para-memory-files skill for consistency
- Memory operations follow strict schemas and decay rules
- Coordination happens through structured protocols, not ad-hoc communication
- Each agent maintains autonomy within their defined responsibilities
- System stability depends on consistent persona adherence

## Support and Documentation

- Use `para-memory-files help` for system operations
- Refer to individual agent HEARTBEAT.md for role-specific protocols
- Consult SOUL.md for persona context and decision frameworks
- System documentation in .omc/ directory

This repository implements a sophisticated multi-agent organizational system that requires understanding of agent coordination, memory management, and persona-driven behavior for effective development.