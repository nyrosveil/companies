# TOOLS.md -- Narrative Designer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Dialogue & Branching Tools

- **Ink**: Unity-integrated dialogue scripting with flow control and variables
- **Yarn Spinner**: Node-based dialogue system for Unity and other engines
- **Twine**: Rapid prototyping of branching narrative structures
- **Articy:draft 3**: Professional narrative design tool with branching visualization
- **Chatterbox**: Character dialogue management and localization
- **Dialogue System for Unity**: Commercial solution with extensive features

## Documentation & Planning

- **Character Voice Pillar Template**: Vocabulary, rhythm, topics avoided, verbal tics, subtext default
- **World Bible**: Timeline, factions, rules of the world, banned retcons
- **Lore Tier Map**: Surface (all players), Engaged (explorers), Deep (lore hunters)
- **Narrative-Gameplay Integration Matrix**: Story beat → gameplay consequence → player feel
- **Environmental Storytelling Brief**: Props, placement, lighting, sound, tier classification
- **Branch Node Map**: Visual representation of all branching paths and convergence points

## Playtesting & Validation

- **Branch Walkthrough Protocol**: Systematically traverse every branch path to verify convergence and avoid dead ends
- **Environmental Story Inference Test**: Ask players to narrate what happened in a space without text prompts
- **Dialogue Authenticity Review**: "Would a real person say this?" checklist; eliminate exposition-as-conversation
- **Consequence Visibility Audit**: Track whether players notice the results of their choices
- **Localization QA**: Test gender-neutral fallbacks, cultural adaptation, string length constraints

## Advanced Capabilities

### Emergent and Systemic Narrative
- **Faction Reputation Systems**: Track player actions and modify NPC behavior accordingly
- **Relationship Value Networks**: Character dispositions based on player choices across multiple interactions
- **World State Flags**: Persistent world changes triggered by player decisions
- **Narrative Query Systems**: Dialogue and events that query systemic data to generate personalized responses
- **Narrative Surfacing Design**: Authored commentary triggered by systemic thresholds

### Choice Architecture and Agency Design
- **Meaningful Choice Framework**: Choices must differ in values, not just aesthetics
- **Fake Choice Design**: Deliberate illusion of agency for emotional effect
- **Delayed Consequence Systems**: Choices in act 1 manifest in act 3 for responsive world feel
- **Consequence Visibility Spectrum**: Map immediate vs. subtle, visible vs. inferred consequences
- **Branch Complexity Management**: Tools to visualize and prune combinatorial explosion

### Transmedia and Living World Narrative
- **ARG Integration**: Design alternate reality game elements that extend beyond the game
- **Social Media Canon**: Use Twitter/Discord posts as canonical story content
- **Lore Database Querying**: Build searchable knowledge base for writers to prevent contradictions
- **Narrative Debt Tracking**: System to track foreshadowing and dangling threads; ensure resolution or retirement
- **Modular Lore Architecture**: Each lore piece standalone but connectable through proper nouns and event refs

### Dialogue Tooling and Implementation
- **Engine-Integrated Dialogue**: Ink directly in Unity, Yarn Spinner in Godot, etc. — no translation layer
- **Branching Visualization Tools**: Single-view conversation trees for editorial review
- **Dialogue Telemetry**: Data-driven analysis of branch selection, line skipping, player engagement
- **Localization from Day One**: String externalization, gender-neutral fallbacks, cultural adaptation metadata
- **Voice Acting Pipeline**: Markdown-to-audio workflow with line marking, batch processing, quality control

### Cinematic and Cutscene Design
- **Timeline-Based Cutscenes**: Use engine timeline tools for precise animation and camera control
- **Interactive Cutscene Design**: Player input during cinematics for agency preservation
- **Cinematic Language**: Shot composition, pacing, editing principles for game cinematics
- **Performance Capture Direction**: Work with mocap actors; provide clear character intentions and beats

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