# TOOLS.md -- Godot Shader Developer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `godot-4-pro` - Godot 4 rendering and shaders

## Godot Shading Language

- **Shader Types** - canvas_item, spatial, particles, sky
- **Built-in Variables** - TEXTURE, UV, COLOR, FRAGCOORD
- **Uniforms** - Exposed parameters, hints, source_color
- **Output Variables** - ALBEDO, METALLIC, ROUGHNESS, NORMAL_MAP

## Renderers

- **Forward+** - Full feature access, high-end target
- **Mobile** - Performance optimized, some limitations
- **Compatibility** - Broad support, no compute, limited features

## 2D Shaders (CanvasItem)

- **Sprite Effects** - Outline, dissolve, flash, hit effects
- **UI Shaders** - Transitions, hover states
- **Post-Processing** - SCREEN_TEXTURE effects
- **World Shaders** - Backgrounds, parallax

## 3D Shaders (Spatial)

- **Surface Materials** - PBR, custom lighting, toon shaders
- **World Effects** - Water, fog, atmosphere
- **Vertex Shaders** - Displacement, deformation
- **Fragment Shaders** - Texture blending, detail mapping

## VisualShader

- **Node-Based Graphs** - Artist-accessible materials
- **Custom Nodes** - VisualShaderNodeCustom
- **Subgraphs** - Reusable node groups, .res files
- **Comment Nodes** - Organization, documentation

## Performance

- **Texture Sampling** - Count samples, mobile budgets
- **SCREEN_TEXTURE** - Framebuffer copy cost
- **discard vs Alpha Scissor** - Mobile performance
- **Dynamic Loops** - Avoid on mobile, use fixed counts

## Advanced Capabilities

- **RenderingDevice** - Compute shaders, direct GPU access
- **CompositorEffect** - Full-screen post-processing
- **RDShaderFile** - GLSL compute, SPIR-V
- **Volumetric Effects** - fog_density, light_volume

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Document renderer requirements in shader headers
- Maintain documentation in AGENTS.md and HEARTBEAT.md
