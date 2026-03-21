# TOOLS.md -- Unreal Systems Engineer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Unreal Engine 5 C++ Development

- **Build System**: `.Build.cs` module configuration, `PublicDependencyModuleNames`, `PrivateDependencyModuleNames`, circular dependency avoidance
- **Reflection System**: `UCLASS()`, `USTRUCT()`, `UENUM()`, `UPROPERTY()`, `UFUNCTION()` macros; understanding of Unreal Header Tool
- **Smart Pointers**: `TSharedPtr<>`, `TWeakPtr<>`, `TUniquePtr<>` for non-UObject; `TWeakObjectPtr<>` for UObject non-owning refs
- **Garbage Collection**: `UPROPERTY()` requirement for UObject pointers; `IsValid()` vs `nullptr`; pending kill state handling
- **Tick Architecture**: `PrimaryActorTick.TickInterval` for configurable frequency; timers over tick for low-frequency logic

## Gameplay Ability System (GAS)

- **Project Setup**: Add `"GameplayAbilities"`, `"GameplayTags"`, `"GameplayTasks"` to `.Build.cs` PublicDependencyModuleNames
- **Attributes**: `UAttributeSet` subclass; `FGameplayAttributeData` with `ATTRIBUTE_ACCESSORS`; `ReplicatedUsing` for network updates
- **Abilities**: `UGameplayAbility` subclass; `ActivateAbility()`, `EndAbility()`; `BlueprintNativeEvent` for designer overrides
- **Tags**: `FGameplayTag` hierarchy; `GameplayTags` manager; tag-based activation constraints and gameplay effects
- **Replication**: Ability system component handles replication; never manually replicate ability state; `GAMEPLAYATTRIBUTE_REPNOTIFY`
- **Effects**: `UGameplayEffect` for attribute modifications; stacking rules; duration types (instant, duration, infinite)

## Performance Optimization

- **Blueprint vs C++**: Per-frame Blueprint ~10x slower than C++ — all Tick logic in C++; Blueprint for high-level orchestration
- **Tick Management**: Configurable `TickInterval` (20Hz for AI, 60Hz only for input/camera); `bCanEverTick` false by default
- **Timer Usage**: `GetWorldTimerManager()` for periodic tasks; avoid `Tick` for anything < 60Hz
- **Data Structures**: Use `TMultiMap`, `TSet` with custom hash for performance; avoid `TArray` linear searches in hot paths
- **Nanite Budget**: 16M instances max per scene; track per-level; use `stat Nanite` to monitor; avoid Nanite for skeletal/spline/procedural

## Memory Safety Patterns

- **UPROPERTY Mandatory**: All UObject-derived pointers must have `UPROPERTY()` macro — without it, GC collects unpredictably
- **Weak Pointers**: `TWeakObjectPtr<AActor>` for non-owning references; always `IsValid()` before use
- **Shared Pointers**: `TSharedPtr<>` for shared non-UObject heap allocations; `TWeakPtr<>` for non-owning
- **Actor Lifespan**: Actors can be destroyed mid-frame — always check `IsValid()` across frame boundaries
- **Pending Kill**: Objects flagged for GC return false for `IsValid()` but non-null pointer — never `!= nullptr` checks

## Build Configuration

- **Generate Project Files**: Always run `GenerateProjectFiles.bat` after modifying `.Build.cs` or `.uproject`
- **Module Dependencies**: Explicit `PublicDependencyModuleNames` and `PrivateDependencyModuleNames`; circular deps cause linker errors
- **PCH Usage**: `PCHUsageMode.UseExplicitOrSharedPCHs` recommended; include common headers in precompiled header
- **Reflection Macros**: Missing `UCLASS()`/`USTRUCT()` causes silent runtime failures (no class registration) — compile warnings catch these
- **Plugin Development**: Use `FPrimaryModule` for game module, `FDefaultModuleImpl` for library; define `IModuleInterface` for custom startup/shutdown

## Editor & Tooling

- **Editor Utilities**: `WithEditor` macros for editor-only code; `Validation` classes for asset checking
- **Custom Editors**: `IDetailsView` customization; `SNew` widget creation; property delegates
- **Asset Validation**: Write `IAssetValidator` implementations; integrate into asset pipeline
- **Commandlets**: `UCommandlet` for batch processing; `Main()` entry point; suitable for automated pipeline tasks

## Networking & Replication

- **GAS Replication**: Attributes via `ReplicatedUsing`; abilities auto-replicated through `UAbilitySystemComponent`
- **RPCs**: `Server`, `Client`, `NetMulticast` exec specifiers; `WithValidation` for server-side input validation
- **Replication Conditions**: `COND_OwnerOnly`, `COND_SkipOwner`, `COND_InitialOnly`, `COND_ReplayOrOwner`
- **Network Prediction**: Client-side prediction where latency unacceptable; server reconciliation for corrections
- **Bandwidth**: Minimize replicated properties; use `DOREPLIFETIME` efficiently; group related state

## Advanced Capabilities

### Mass Entity System
- `UMassEntitySubsystem` for high-performance simulation of thousands of entities
- `FMassFragment` as data components; `FMassTag` as boolean flags; `FMassChunkFragment` for batched processing
- `FMassProcessor` implementations with `Execute()` function; automatic parallelization via task graph
- `UMassRepresentationSubsystem` to bridge Mass entities to visual Actors (ISM, LOD switching)
- Use-cases: crowd simulation, projectile swarms, particle systems, AI pathfinding at scale

### Chaos Physics
- `UGeometryCollectionComponent` for fractureable meshes; author fractures in editor's Fracture tool
- `UChaosDestructionListener` for event callbacks on fracture events; apply gameplay effects based on damage location
- Constraint types: `Chaos::FPhysicsConstraintType::Rigid`, `Soft`, `Spring`, `Suspension` for realistic joint behavior
- LOD strategy: full Chaos simulation near player, cached animation playback at distance using `UChaosSolverActor`
- Profile with Chaos trace channel in Unreal Insights; solver iteration count affects performance vs accuracy

### Custom Subsystems
- `UGameInstanceSubsystem` for global state persisting across level loads; `GetGameInstance()` access
- `ULocalPlayerSubsystem` for per-local-player data (input bindings, UI preferences); `GetLocalPlayer()` access
- `UEngineSubsystem` for engine-wide services (logging, analytics); available even without a game instance
- Custom `IInputProcessor` to intercept raw input before `PlayerController`; use `FSlateApplication` for UI input
- `FTickableGameObject` for engine-tick-level tasks independent of Actor lifecycle; `Tick()` called even in pause

### Advanced GAS
- `GameplayEffect` magnitude curves: `FBasedFixedMagnitude` with `Curve` for attribute scaling over level
- `FGameplayTagResponseTable` for automatic ability activation/termination based on tag state changes
- `ULyraAbilityTask` async task pattern for multi-stage abilities with network-safe coroutines
- `GameplayCue` for visual/audio feedback: `OnActive`, `WhileActive`, `OnRemove`; replicate via `GameplayCueManager`
- Ability system batching: `FActiveGameplayEffectsContainer` optimizations; effect compilation to minimize replication overhead

## Performance Profiling

- **Unreal Insights**: Main profiling tool; trace sessions; analyze CPU, GPU, load, and network tracks
- **Stat Commands**: `stat unit`, `stat rhi`, `stat scenerendering`, `stat nanite`, `stat g Eli` for quick metrics
- **GPUTiming**: Insert `FRHIGPUTimer` scopes in C++ code for precise GPU timing of custom passes
- **Memory**: `memreport -full` for detailed memory breakdown; `stat streaming` for texture/streaming memory
- **Network**: `netprofile` and `netstats` for bandwidth analysis; `netdebug` for replication visualization

## Integration Recommendations

- Use para-memory-files for all system architecture diagrams, GAS ability trees, performance budget tracking
- Read Unreal Engine C++ API docs for `UObject`, `AActor`, `UGameplayAbility`, `UAttributeSet`, `UWorldPartition`
- Establish C++/Blueprint boundary document: list all C++ classes, their Blueprint-exposable API, intended designer usage
- Profile with Unreal Insights from day one; establish baseline frame time before adding features
- Always call `GenerateProjectFiles.bat` after `.Build.cs` changes; verify no circular dependencies with `UnrealBuildTool`
- Enforce `IsValid()` checks in code review; use static analysis tools to catch missing validity checks
- Budget Nanite instances per level in shared spreadsheet; track across all scenes; 16M is hard limit
- Document tick intervals per system: AI (20Hz), physics (variable), UI (60Hz), animation (30Hz typical)
