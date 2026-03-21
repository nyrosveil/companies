# TOOLS.md -- Unreal Technical Artist

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Material & Shader Systems

- **Material Editor**: Node-based shader authoring; Material Functions; Material Instances; parameter groups
- **Material Function Library**: Reusable logic encapsulation; input/output parameters; library organization
- **Quality Switch Node**: Platform-specific material variants within single graph; Low/Med/High tiers
- **Static Switch Parameters**: Material permutation control; audit cost of each additional switch
- **Shader Model Selection**: DefaultLit, Unlit, Subsurface, TwoSidedFoliage, etc.; choose per material use case
- **Substrate Material System** (UE5.3+): Multi-layered slabs; wet/dry layers; volumetric fog integration

### Material Performance Analysis

- **Material Stats Window**: Instruction count (Base Pass, Pixel Shader), texture sample count, static switch count
- **Shader Complexity Viewport Mode**: Visualize shader cost per pixel; red = expensive, blue = cheap
- **Platform Budgets**: Mobile: <200 instructions, <8 textures; Console: <400 instructions, <16 textures; PC: <800 instructions
- **Permutation Count Calculation**: 2^n where n = number of Static Switches; track and limit combinatorial explosion

## Niagara VFX Systems

- **Niagara System Architecture**: System, Emitter, Module stack; CPU vs GPU simulation selection
- **Emitter Types**: Burst, continuous, event-driven; spawn rate control; lifetime management
- **Module Stack**: Initialize, Update, Render; particle state manipulation; custom HLSL nodes
- **Parameter Binding**: Bind to Material parameters; Parameter Collections for global game state; user axes for runtime control
- **Scalability System**: Niagara Scalability assets; quality presets (Low/Med/High); significance handlers (distance, screen size)
- **Data Interfaces**: Physics scene queries; mesh surface sampling; audio spectrum analysis; custom struct passing

### Niagara Performance Tuning

- **Max Particle Count**: Always set; never unlimited; budget per effect type (dust: 50, explosion: 200, etc.)
- **GPU Simulation**: For >1000 particles; use compute shaders; avoid per-particle collision on GPU
- **CPU Simulation**: For <1000 particles or complex logic; easier debugging; lower GPU cost
- **Overdraw Management**: Minimize transparent layers; use Alpha Clip where possible; batch particle systems by material
- **Scalability Testing**: Test each preset on target hardware; adjust particle counts, texture resolution, update frequency

## PCG (Procedural Content Generation)

- **PCG Graph Editor**: Node-based procedural generation; deterministic output; input/output parameters
- **Point Generation**: Surface sampling; density parameters; biome filters; noise-based distribution
- **Transform Filters**: Position jitter; rotation variation; scale randomization; alignment to surface
- **Density Filters**: Poisson disk sampling; minimum separation; clustering controls
- **Exclusion Zones**: Road buffers; player path buffers; hand-placed actor exclusion; tag-based filtering
- **Spawner Nodes**: Static Mesh Spawner; Foliage Type; Hierarchical Instanced Static Mesh (HISM) placement
- **PCG Debugging**: Viewport visualization modes; point density heatmaps; attribute coloring; generation time metrics

### PCG Performance Considerations

- **Nanite Eligibility**: All PCG-placed static meshes should have Nanite enabled for massive instance counts
- **Cull Distance**: Set per asset class; distant instances automatically culled; streaming integration
- **PCG Streaming**: World Partition integration; generate on-demand as player approaches; hitch-free generation
- **Parameter Exposing**: Document all designer-facing parameters; create editor UI for tuning without graph editing
- **Generation Time**: Target <3 seconds for worst-case area; profile with worst-case density settings

## Rendering Optimization Tools

- **Unreal Insights**: GPU/CPU timeline; frame breakdown; identify rendering bottlenecks; marker-based analysis
- **GPU Profiler**: Per-pass timing; shader complexity; texture bandwidth; ALU utilization
- **Stat Commands**: `stat rhi`, `stat unit`, `stat sceneRendering`, `stat shadercompiling` for runtime metrics
- **Visualize Mode**: `visualize shadercomplexity`, `visualize occludedprim`, `visualize instancing` for in-viewport analysis
- **Render Doc Integration**: Frame capture; draw call inspection; shader debugging; resource viewing

### LOD & Culling

- **Nanite Configuration**: Auto-generated LODs for eligible meshes; manual override for non-eligible; triangle count thresholds
- **Manual LOD Chains**: For skeletal, spline, procedural meshes; LOD0 → LOD1 → LOD2 → LOD3; screen size transitions
- **HLOD (Hierarchical LOD)**: Cluster rendering for distant objects; proxy mesh generation; World Partition integration
- **Cull Distance Volumes**: Per-actor class culling distances; distance-based visibility; prioritize distant culling
- **Occlusion Culling**: Precomputed occlusion for static geometry; dynamic occlusion for movable objects; configuration in world settings

## Custom Shaders & Render Passes

- **Custom Shader Models**: Extend shading models via module; implement custom lighting models; integrate with material editor
- **Render Passes**: `FRenderPass` implementation; render target allocation; queue management; blend state configuration
- **Compute Shaders**: DispatchCompute; UAV buffers; thread group sizing; synchronization; async compute integration
- **Custom Render Features**: `IRendererModule` extensions; pass injection points; camera/scene-specific effects
- **Post-Process Materials**: Full-screen material passes; blendable stack integration; custom shader implementations

## Python & Automation

- **Unreal Python API**: Editor scripting; asset batch processing; material validation; Niagara system audits
- **Material Batch Operations**: Mass parameter updates; material interface compliance checks; shader variant analysis
- **Niagara Validation Scripts**: Particle count audits; scalability preset verification; performance regression detection
- **PCG Automation**: Batch graph parameter setting; generation validation; performance benchmarking across parameter sets
- **Performance CI/CD**: Automated profiling runs; regression detection; report generation from headless builds

## Integration Recommendations

- Use para-memory-files for Material Function specs, Niagara scalability configs, PCG parameter docs, performance benchmarks
- Employ paperclip to coordinate with Material Artists, VFX Artists, Environment Artists on system handoffs and training
- Reference HEARTBEAT.md for daily performance triage: check material stats, VFX scalability, PCG generation times
- Activate tdd-guide agent before implementing complex PCG graphs or custom render passes to establish test criteria
- Maintain a "Material Permutation Budget" document; track each Static Switch's impact on shader combinations
- Build Niagara Scalability presets concurrently with the main effect; never add scalability as an afterthought
- For PCG, always expose density and distribution parameters; designers must be able to tune without graph editing
- Profile using Unreal Insights in actual gameplay; editor viewport metrics are misleading for runtime performance
- Use Material Functions aggressively — duplicated node clusters become technical debt immediately
- Validate Nanite eligibility on all static meshes; non-eligible assets need LOD chains and culling strategies
- Keep a "Shader Instruction Budget" spreadsheet per platform; enforce sign-off before milestone lock
- Document all performance assumptions: "this effect assumes max 5 concurrent systems on mobile" — verify in testing