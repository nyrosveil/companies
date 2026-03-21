# TOOLS.md -- Unity Architect

## Core Skills
- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## ScriptableObject Patterns
- **FloatVariable/IntVariable/BoolVariable**: Shared runtime variables with change events
- **GameEvent / GameEvent<T>**: Type-safe event channels for decoupled communication
- **RuntimeSet<T>**: Global entity tracking without singletons; auto-registration via MonoBehaviour
- **ObjectReference Variable**: GameObject, Component, ScriptableObject references via SO assets
- **SO State Machines**: State as SO, transitions as events, encapsulated state logic
- **SO Command Pattern**: Command objects for undo/redo that survive session boundaries

## Unity Architecture Standards
- **Data-Driven Design**: All shared data in ScriptableObjects; no hardcoded references
- **Single Responsibility**: One concern per MonoBehaviour; prefab self-containment
- **Event-Driven Updates**: React to value changes via events; eliminate polling
- **Inspector Wiring**: Drag-and-drop SO references; no `Find()` or `GetComponent` chains across objects
- **Addressables**: Replace `Resources.Load` entirely; group by loading profile
- **Serialization Hygiene**: `EditorUtility.SetDirty` on SO mutations; never store scene refs in SOs

## Custom Editor Development
- **PropertyDrawers**: Custom inspectors for Variable SOs showing live runtime values
- **CustomEditors**: Full inspector overrides for complex SO types and component validation
- **ContextMenu Actions**: `[ContextMenu("Reset to Default")]` on SOs for designer convenience
- **Editor Validation**: Build-time checks for architecture rules (no `Find()`, proper SO usage)
- **Debug Overlays**: Scene view gizmos for event channels, SO values, runtime sets

## Performance Optimization
- **Profiler Deep Dive**: Use Unity Profiler's deep profiling to catch per-call allocations
- **Memory Profiler Package**: Audit managed heap; track allocation roots and retained graphs
- **GC Pressure Reduction**: Event-driven patterns; avoid allocations in `Update()`; use object pooling
- **Burst Compiler & Jobs**: `[BurstCompile]` jobs for CPU-bound batch operations; `NativeArray` for zero-GC
- **Frame Budgeting**: Allocate ms budgets per system (rendering, physics, gameplay) and enforce via CI

## Anti-Pattern Detection & Refactoring
- **God Class Detector**: Components >150 lines or multiple responsibilities → split
- **Singleton Inspector**: Identify inappropriate `DontDestroyOnLoad`; suggest SO alternatives
- **Coupling Analyzer**: Spot `GetComponent` chains, static dependencies, hardcoded strings
- **Update Bloat Finder**: Find polling logic that should be event-driven; convert to event subscriptions

## DOTS & Data-Oriented Design
- **Entities System**: Migrate performance-critical systems to ECS; keep MonoBehaviour for gameplay logic
- **Job System**: `IJobParallelFor` for batch operations (pathfinding, physics queries, animation)
- **Burst Compilation**: Near-native performance without manual SIMD; annotate Jobs with `[BurstCompile]`
- **Hybrid Architecture**: ECS for simulation, MonoBehaviours for presentation; map data flow between them

## Addressables & Asset Management
- **Addressable Groups**: Preloaded critical, on-demand scenes, DLC bundles; label-based organization
- **Async Scene Loading**: Addressables.LoadSceneAsync with progress callbacks; seamless streaming
- **Dependency Management**: Build asset dependency graphs to avoid duplicates; optimize memory
- **Remote Content**: Support downloadable content via remote Addressable groups; version management

## Advanced SO Patterns
- **SO State Machine**: States as ScriptableObjects with `Enter/Exit/Execute` methods; transitions via events
- **Configuration Layers**: Dev/staging/prod config SOs swapped at build time via build scripting
- **Command Pattern**: SO-based commands with `Execute/Undo`; persistable across sessions
- **Catalog Pattern**: `ItemDatabase : ScriptableObject` with dictionary caches for fast runtime lookup

## Tool Development
- **Editor Windows**: Custom Unity Editor windows for architecture validation, SO management
- **Asset Processors**: `AssetPostprocessor` scripts to enforce naming, import settings, validation
- **CI Integration**: Automated architecture audits in CI pipeline; fail builds on rule violations
- **Debug Utilities**: Scene view gizmos for event debugging; runtime SO value inspectors

## Integration Recommendations
- Use para-memory-files for architecture decision records, pattern documentation, and refactor plans
- Employ paperclip to coordinate architectural reviews and refactor milestones
- Reference HEARTBEAT.md for daily anti-pattern scanning checklist
- Activate tdd-guide agent before implementing new architectural patterns
- Build Editor tools that make data-driven design the path of least resistance
- Say "no" to `Resources.Load` and `GameObject.Find`; provide SO-based alternatives
- Profile allocations in every code review; flag per-frame allocations immediately
- Maintain a Unity Architecture Guide with examples; keep it versioned alongside code
- Conduct regular architecture office hours; review God Classes and singleton abuse
- Document all performance budgets (GC allocations, frame time, memory) and track compliance