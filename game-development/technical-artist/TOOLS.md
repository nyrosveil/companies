# TOOLS.md -- Technical Artist

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Shader & Rendering

- **HLSL/GLSL**: Low-level shader programming for custom effects
- **Shader Graph (Unity)**: Visual shader authoring with code export for optimization
- **Material Editor (Unreal)**: Node-based material creation with custom HLSL integration
- **Visual Shader (Godot)**: Graph-based shader authoring for Godot rendering pipelines
- **Shader Complexity Visualizer**: Built-in engine tools to identify expensive pixel operations
- **RenderDoc / PIX / Nsight**: GPU debugging and profiling tools

## Visual Effects Systems

- **Niagara (Unreal)**: Advanced particle system with compute shader support
- **VFX Graph (Unity)**: GPU-powered particle effects with Shader Graph integration
- **GPUParticles3D (Godot)**: GPU particle system with threading support
- **Particle Overdraw Analysis**: Visualize additive/transparent layer counts
- **Particle Budgeting**: Max simultaneous particles, texture atlasing, LOD systems

## Asset Pipeline & Optimization

- **LOD Generation**: Automated mesh simplification tools (Simplygon, InstaLOD, custom scripts)
- **Texture Compression**: BC7 (PC), ASTC (mobile), ETC2, PVRTC; format selection per platform
- **Texture Atlasing**: Batch packing tools; draw call reduction strategies
- **Normal Map Generation**: From height maps; ensuring correct tangent space
- **Mipmap Configuration**: Per-texture settings; bias control for distant objects
- **Mesh Validation**: UV layout checking, non-manifold geometry detection, pivot correction

## Tool Development

- **Python for DCC Tools**: Maya, Blender, 3ds Max scripting for validation and batch processing
- **Unity Editor Tools**: Editor windows, asset processors, importers, custom inspectors
- **Unreal Editor Utilities**: Python scripting, editor mode tools, asset factories
- **Godot Editor Plugins**: GDScript/C++ plugins for pipeline automation
- **CI/CD Integration**: Jenkins, GitHub Actions, GitLab CI for automated asset validation
- **Batch Processing Scripts**: Texture conversion, LOD generation, lightmap baking automation

## Performance Profiling

- **GPU Profilers**: RenderDoc, Nvidia Nsight, AMD Radeon GPU Profiler, Intel GPA
- **Frame Debuggers**: Unity Profiler, Unreal Insights, Godot Profiler
- **Memory Analysis**: Texture memory, shader memory, mesh memory tracking
- **Draw Call Optimization**: Static batching, dynamic batching, GPU instancing, SRP Batcher
- **Overdraw Visualization**: Engine tools to visualize transparent pixel fill rate
- **Shader Complexity Maps**: Color-coded visualizations of pixel/vertex shader cost

## Advanced Capabilities

### Real-Time Ray Tracing Integration
- **RT Feature Evaluation**: Cost-per-effect analysis (reflections, shadows, AO, GI)
- **Hybrid Rendering**: RT + fallback techniques (SSR, shadow maps) based on quality thresholds
- **Denoising Implementation**: DLSS RR, XeSS, FSR integration for noise reduction with fewer rays
- **Material RT Optimization**: Roughness map accuracy > albedo; metallic/roughness PBR workflow

### AI/ML-Enhanced Pipelines
- **Super-Resolution Upscaling**: ESRGAN, Waifu2x for legacy asset quality uplift
- **AI Denoising**: Lightmap baking acceleration; path tracing noise reduction
- **DLSS/FSR/XeSS Implementation**: Upscaling as quality-tier feature, not afterthought
- **Normal Map Generation**: AI-assisted height-to-normal conversion for terrain/details

### Post-Processing Architecture
- **Modular Stack Design**: Independent passes (bloom, CA, vignette, color grading) with toggles
- **LUT Creation & Import**: DaVinci Resolve/Photoshop → 3D LUT → game engine pipeline
- **Platform-Specific Profiles**: Tiered settings (consoles: heavy effects; mobile: minimal)
- **TAA with Sharpening**: Combat ghosting while preserving detail on fast motion

### Cross-Platform Rendering Strategies
- **Scalable Quality Settings**: Geometry detail, shadow resolution, effect density per platform
- **Mobile Optimization**: Reducing overdraw, vertex count, texture size; ASTC compression
- **Console Optimization**: Leveraging hardware features (RT cores, mesh shaders, variable rate shading)
- **PC Scalability**: User-facing quality sliders mapped to underlying budget adjustments

### Toolchain Automation
- **Import Validation Pipelines**: Pre-commit hooks, CI checks, automated artifact linting
- **Batch Asset Processing**: Mass texture conversion, LOD generation, normal map baking
- **Live Editor Tools**: Real-time budget display as artists work; auto-suggest optimizations
- **Performance Regression Detection**: Automated benchmark scenes; alert on budget violations

## Integration Recommendations

- Use para-memory-files for all pipeline knowledge and tool documentation
- Employ paperclip to coordinate asset review schedules and budget sign-offs
- Reference HEARTBEAT.md for daily performance triage rhythm
- Activate tdd-guide agent before implementing major rendering changes
- Keep a master spec sheet per platform — refer to it constantly in reviews
- Say "no" with numbers: "That texture is 4096×4096, budget is 2048 — here's the 2048 version"
- Always profile on target hardware, not editor viewport
- Automate every repetitive validation; if you see the same issue twice, write a tool
- Build shader variants from a single source graph (shader graph → code) to avoid divergence
- Maintain a "performance wins" log — share before/after metrics to build team awareness