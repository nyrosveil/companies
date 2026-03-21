# TOOLS.md -- Unity Shader Graph Artist

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Shader Graph & Visual Authoring

- **Node-Based Shader Authoring**: URP/HDRP Shader Graph with custom function nodes, sub-graphs, and master stacks
- **Sub-Graph Design**: Reusable encapsulated logic (Fresnel, dissolve, triplanar mapping, noise functions)
- **Blackboard Management**: Parameter organization, tooltips, grouping, and artist-facing exposure control
- **Graph Optimization**: Node simplification; branch removal; texture sample minimization; precision control
- **Custom Function Nodes**: Inline HLSL snippets within Shader Graph for performance-critical or unsupported operations

## HLSL & Low-Level Shading

- **ShaderLab Wrapper**: `.shader` files with proper Pass/SubShader structure; compatible with URP/HDRP SRP
- **SRP Includes**: `Core.hlsl`, `Lighting.hlsl`, `ShaderVariables.hlsl` from Universal/HDRP packages
- **CBUFFER Macros**: `CBUFFER_START/END(UnityPerMaterial)` for material constant buffers; SRP batcher compatibility
- **Texture/Sampler Macros**: `TEXTURE2D`, `SAMPLER`, `LOAD_TEXTURE2D` for SRP-compatible texture sampling
- **Vertex/Fragment Structs**: Attributes → Varyings → SV_Position/SV_Target with proper semantic compatibility
- **PBR Functions**: `UniversalFragmentPBR`, `BlinnPhongHighlight`, `GGX` for physically-based rendering integration

## Custom Render Pipelines (URP)

- **ScriptableRendererFeature**: Create full-screen or camera-specific render passes; register with renderer
- **ScriptableRenderPass**: Implement `Execute` method with CommandBuffer and RenderingData; control `renderPassEvent`
- **RTHandle Management**: Allocate temporary vs. persistent `RTHandle`s for intermediate textures; release correctly
- **Renderer Configuration**: Modify URP asset settings; add renderer features per-camera via `ScriptableRendererData`
- **Render State Overrides**: Override render queue, stencil, culling per-pass; blend mode control
- **Integration with Stack**: Insert passes before/after specific URP passes (AfterRenderingOpaques, BeforePostProcess)

## Custom Render Pipelines (HDRP)

- **CustomPassVolume**: Global or volume-linked custom passes; injection points (BeforeTransparent, AfterPostProcess)
- **CustomPass**: Full-screen, draw objects, draw renderer, or custom GPU compute; `Execute` method implementation
- **HDRP UI Integration**: Volume component authors; custom pass inspector with target selection
- **Render Pipeline Resources**: Custom shaders, materials, and settings in HDRP asset; proper SRP Batcher setup
- **Ray Tracing Integration**: Add custom passes with ray tracing effects (reflections, shadows) when RTX available

## Performance Profiling Tools

- **Unity Frame Debugger**: Step through each draw call; inspect shader properties, render states, texture bindings
- **Unity Profiler GPU Module**: Capture GPU timeline; per-pass timing; identify bottleneck (vertex vs. fragment)
- **Shader Graph Stats Panel**: Node count, instruction count, texture sample count before compilation
- **RenderDoc Integration**: Deep shader debugging; inspect intermediate values; register-level analysis
- **Mobile GPU Profilers**: Mali/Adreno/Apple GPU tools for device-specific performance analysis
- **Overdraw Visualization**: Use Unity's overdraw view mode to identify transparency hot spots

### Advanced Shader Optimization Patterns

- **Texture Atlasing**: Blend multiple materials into atlas to reduce draw calls and sampler slots
- **DXT/BC Compression Awareness**: Normal map compression (BC5), HDR textures (BC6H/BC7), mobile (ASTC) — know the quality/size tradeoffs
- **ALU Reduction**: Combine operations; use `mad` (multiply-add) patterns; minimize `sqrt`, `pow`, `trig` calls
- **Precision Control**: `half` vs. `float` precision on mobile; use `min16float` where supported; avoid over-precision
- **Branch Divergence**: Minimize `if` in fragment shaders; use `step`, `smoothstep`, `lerp` for GPU-friendly control flow
- **Derivative Issues**: Avoid `ddx/ddy` on tile-based deferred GPUs (mobile); use `fwidth` carefully
- **Vertex vs. Fragment Push**: Move non-pixel-dependent calculations to vertex shader; varyings to fragment

### Compute Shaders & GPU Compute

- **Compute Shader Authoring**: `#pragma kernel CSMain`; `[numthreads]` block sizing; thread group sizing considerations
- **Dispatch Patterns**: Indirect vs. direct dispatch; `ComputeBuffer` for arguments; `AsyncGPUReadback` for results
- **UAV & RWTexture**: Unordered access views for read/write textures/buffers; atomic operations for synchronization
- **GPU-Driven Rendering**: Indirect draw calls from compute shader; `Graphics.DrawProcedural` for massive instancing
- **Compute Debugging**: GPU debuggers for compute kernels; thread inspection; memory barrier placement

### Procedural Content Generation

- **Noise Functions**: Worley, Simplex, Perlin, FBM — implement in shader or compute; tileability considerations
- **Splat Mapping**: Terrain texture blending from height/slope/normal; weighted blending; texture array usage
- **Dynamic Textures**: RenderTexture allocation and lifetime; RT release; `AsyncGPUReadback` to read back to CPU
- **Atlas Generation**: Combine dynamic elements at runtime (minimap markers, UI backgrounds) into texture atlases

## Integration Recommendations

- Use para-memory-files for shader library specs, performance benchmarks, and platform compatibility matrices
- Employ paperclip to coordinate shader development with art asset production timelines
- Reference HEARTBEAT.md for daily shader complexity audit and profiling checklist
- Activate the tdd-guide agent before implementing complex custom render passes to establish test targets
- Maintain a "Shader Performance Baseline" document: per-platform budgets; reference shader costs; optimization checklists
- Say "no" to unprofiled shaders; every new shader must pass Frame Debugger and GPU Profiler before QA
- Keep a "Sub-Graph Library" — any logic used in >1 shader becomes a Sub-Graph; enforce this as a quality gate
- Use RenderDoc extensively — it shows you what the GPU actually sees; trust it over Shader Graph preview
- Profile on device, not editor; mobile GPUs behave differently than desktop GPUs even with same shader
- For custom compute shaders, start with small thread group sizes; scale up; measure occupancy; optimize register pressure
- Document all material parameters with clear slider ranges and visual descriptions — artists need to know what "0.5" looks like
- Version control `.shadergraph` and `.hlsl` files together; maintain `#define` compatibility across Unity versions