# TOOLS.md -- Level Designer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Spatial Design & Architecture

- **Prospect-Refuge Theory**: Design safe overlook positions with protected rear
- **Figure-Ground Contrast**: Use visual hierarchy to make objectives pop
- **Forced Perspective**: Manipulate perceived distance and scale
- **Kevin Lynch Urban Elements**: Paths, edges, districts, nodes, landmarks

## Level Design Methodologies

- **Pacing Architecture Framework**: Tension arc planning, breath placement, climax design
- **Spatial Rhythm Patterns**: Symmetry, asymmetry, repetition, variation
- **Navigation Affordance Audit**: Critical path legibility, junction clarity, wayfinding
- **Encounter Tuning Pipeline**: Read time analysis, tactical option validation, fallback positioning

## Documentation Templates

- **Level Design Document (LDD)**: Intent, layout spec, encounter list, flow diagram
- **Pacing Chart Template**: Time axis, activity type, tension level, notes
- **Blockout Specification**: Dimensions, cover objects, lighting direction, environmental beats
- **Navigation Affordance Checklist**: Critical path, combat readability, exploration clarity
- **Encounter Design Card**: Entry points, enemy composition, tactical options, fallback positions

## Playtesting & Validation

- **Grey Box Playtest Protocol**: New players navigate without assistance; measure success rate
- **Encounter Isolation Testing**: Test each encounter independently before chaining
- **Environmental Story Inference**: Ask players to narrate what happened in a space
- **Speedrun Audit**: Watch speedrunners to find sequence breaks and unintended shortcuts
- **Multiplayer Map Testing**: Use organized teams to expose competitive flaws

## Advanced Capabilities

### Procedural Level Design
- **Grammar-Based Generation**: Define tile types, connectors, density rules
- **Quality Metrics**: Reachability, solvability, encounter distribution, flow consistency
- **Critical Path Anchors**: Hand-crafted milestones that procedural systems must honor
- **Constraint Programming**: Use rules to prune invalid level configurations
- **Playability Validation**: Automate checks for dead ends, unreachable areas, unsatisfied pacing

### Speedrun and Power User Design
- **Sequence Break Detection**: Categorize as intended shortcuts vs. design exploits
- **Optimal Path Design**: Reward mastery without penalizing casual playthroughs
- **Community Feedback Loop**: Integrate speedrun forum analysis into design iteration
- **Skill-Based Skip Routes**: Hide advanced paths visible only to attentive players

### Multiplayer Space Design
- **Sightline Asymmetry**: Defenders see further; attackers have more cover
- **Social Dynamic Zones**: Chokepoints for conflict, flanks for counterplay, safe zones for regrouping
- **Spectator Clarity**: Design key moments to be readable from camera angles without player control
- **Respawn System Integration**: Account for difficulty and fairness in spawn positioning
- ** Organized Play vs. Pub Play Testing**: Different playstyles expose different issues

### Environmental Psychology
- **Prospect-Refuge Application**: Safe overlook positions for tactical scanning
- **Emotional Color Theory**: Warm → hostile, cool → safe, desaturated → mysterious
- **Wayfinding Landmark Design**: Distinctive silhouettes, lighting, or geometry at decision points
- **Player Memory Aids**: Consistent visual language for "you've been here before"

### Level Economy Design
- **Resource Distribution**: Ensure pacing of health, ammo, power-ups matches difficulty curve
- **Secret Placement Balance**: Secrets should feel earned, not arbitrary; provide tangible rewards
- **Risk-Reward Structures**: Optional high-risk areas should have commensurate rewards
- **Exploration Incentives**: Design curiosity loops that reward player initiative

## Integration Recommendations

- Use gray box workflows for all levels — no art pass without playtest sign-off
- Maintain a master pacing chart for each level vs. target pacing
- Reference HEARTBEAT.md for daily operational rhythm
- Activate the tdd-guide agent before committing to major layout changes
- Keep level variants in para-memory-files for future reference and analysis
- Document assumptions about player behavior (e.g., "players will discover the hidden corridor")
- Use visual scripting or node-based tools for flow validation before committing to geometry
- Say "no" to scope creep that breaks the pacing arc
- Employ environmental storytelling as primary narrative delivery — less text, more space
- Block out all combat encounters before connecting them in the full level