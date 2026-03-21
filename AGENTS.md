# AGENTS.md - Paperclip Companies Repository

You are working in the Paperclip Companies repository — a collection of specialized AI agent definitions organized in a hierarchical corporate structure.

## Repository Structure

```
companies/
├── default/          # Template agents (ceo, cto, engineer, etc.)
├── vp/              # VP-level strategic leadership (12 agents)
├── director/        # Director-level operational management
├── engineering/     # Technical specialists (23 agents)
├── design/          # Creative & UX specialists
├── game-development/# Game dev specialists
└── AGENTS.md        # This file
```

## Quick Start

```bash
# Create new agent from template
git checkout -b add-{agent-name}
mkdir -p {category}/{agent-name}

# Copy template files from default/ceo/
cp default/ceo/SOUL.md {category}/{agent-name}/
cp default/ceo/AGENTS.md {category}/{agent-name}/
cp default/ceo/HEARTBEAT.md {category}/{agent-name}/
cp default/ceo/TOOLS.md {category}/{agent-name}/

# Edit files, then commit
git add {category}/{agent-name}/
git commit -m "feat: add {agent-name} agent"
```

## The Paperclip 4-File Format

Every agent **MUST** have exactly these 4 files:

| File | Purpose | Key Sections |
|------|---------|--------------|
| `SOUL.md` | Persona & identity | Strategic Posture, Voice & Tone, Critical Rules, Success Metrics |
| `AGENTS.md` | Capabilities & authority | Memory system, Safety, References |
| `HEARTBEAT.md` | Execution checklist | Identity check, Planning, Assignments, Delegation, Extraction |
| `TOOLS.md` | Skills & technologies | Core skills, Domain tools, Integration |

## File Templates

### SOUL.md Structure

```markdown
# SOUL.md -- {Agent Name}

You are the {Agent Name}.

## Strategic Posture

- 10-15 bullet points defining decision framework
- Start with "Default to..." or "Protect..." or "Own..."
- Each point is a principle, not a task

## Voice and Tone

- 8-12 bullet points on communication style
- Include: directness level, technical depth, how to disagree
- Example: "Lead with the constraint" or "Quantify the tradeoff"

## Critical Rules

### {Category} Rules
- **MANDATORY**: Capitalized, bold rules that must never be broken
- Regular rules with specific guidance
- Use "Never..." and "Always..." for clarity

## Success Metrics

- 4-6 measurable outcomes
- Format: "Zero X..." or "All Y validated..." or "< N seconds"
```

### AGENTS.md Template

```markdown
You are the {Agent Name}.

Your home directory is $AGENT_HOME. Everything personal to you -- life, memory, knowledge -- lives there.

Company-wide artifacts live in the project root, outside your personal directory.

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

## Code Style Guidelines

### Markdown Formatting

- **Headers**: Use ATX style (`#` not `===`)
- **Line length**: Wrap at ~100 characters for readability
- **Lists**: Use `-` for unordered, `1.` for ordered
- **Code blocks**: Always specify language: ` ```python `, ` ```bash `
- **No trailing whitespace**: Check before committing

### Writing Style

- **Voice**: Active voice, present tense ("You are..." not "This agent is...")
- **Rules**: Imperative form ("Never do X" not "You should not do X")
- **Specificity**: Quantify when possible ("< 200 lines" not "small functions")
- **Directness**: Lead with the point, then context. No corporate filler.
- **Language**: Plain English. "Use" not "utilize." "Start" not "initiate."

### Directory Naming

- Use lowercase with hyphens: `backend-architect`, not `BackendArchitect`
- Be descriptive but concise: `frontend-developer` not `senior-frontend-software-engineer`
- Group by function: engineering agents in `engineering/`, design in `design/`

### Cross-References

- Use `$AGENT_HOME` for agent-specific paths
- Use relative paths for cross-agent references
- Link to related agents when relevant

## Validation

Before marking an agent as complete, verify:

```bash
# Check all 4 files exist
ls {category}/{agent-name}/{SOUL,AGENTS,HEARTBEAT,TOOLS}.md

# Validate markdown syntax
cat {category}/{agent-name}/SOUL.md | head -5

# Check no trailing whitespace
grep -n ' $' {category}/{agent-name}/*.md
```

### Validation Checklist

- [ ] All 4 files exist (SOUL.md, AGENTS.md, HEARTBEAT.md, TOOLS.md)
- [ ] Directory name uses lowercase-hyphen format
- [ ] SOUL.md has Strategic Posture, Voice & Tone, Critical Rules, Success Metrics
- [ ] AGENTS.md references para-memory-files skill
- [ ] HEARTBEAT.md follows the 8-step template
- [ ] TOOLS.md lists relevant skills and tools
- [ ] No trailing whitespace in any file
- [ ] Consistent formatting (check similar agents for reference)

## Git Workflow

```bash
# Create feature branch
git checkout -b add-{agent-name}

# Stage agent directory
git add {category}/{agent-name}/

# Commit with conventional commit
git commit -m "feat: add {agent-name} agent"

# No build/test required — this is a documentation repository
git push origin add-{agent-name}
```

## File Organization Rules

1. **Never commit** `.DS_Store`, `.ruff_cache/`, or IDE-specific files
2. **Always use** directories for agents — no flat files
3. **Group by function** — agents belong in their domain category
4. **Keep consistency** — copy structure from similar agents in the same category

## Reference Templates

- `default/ceo/` - The canonical template
- `engineering/frontend-developer/` - Good technical agent example
- `engineering/backend-architect/` - Clean, minimal structure

## Questions?

- Check `default/ceo/` for the canonical template
- Look at existing agents in the same category for domain-specific patterns
- Follow the organizational hierarchy in this file
