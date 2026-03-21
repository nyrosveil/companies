# TOOLS.md -- Unreal World Builder

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `unreal-pro` - Unreal Engine environment and level design

## World Building

- **World Partition** - Grid configuration, cell sizing, streaming sources
- **Landscape System** - Heightmaps, layer blending, Runtime Virtual Texturing
- **HLOD (Hierarchical LOD)** - Generation, validation, visual quality
- **Procedural Content Generation (PCG)** - Graphs, surface sampling, distribution
- **Foliage Systems** - Instance budgets, Nanite integration, exclusion zones

## Performance & Optimization

- **Streaming Performance** - Cell size optimization, loading range tuning
- **Draw Call Budgets** - HLOD coverage, instance count management
- **Memory Management** - Texture streaming, landscape LOD
- **Unreal Insights** - Streaming profiling, hitch detection

## Environment Design

- **Landscape Materials** - Multi-layer blending, auto-slope/height rules
- **Biome Systems** - Procedural placement, density control
- **Large World Coordinates (LWC)** - Worlds >2km precision handling
- **One File Per Actor (OFPA)** - Multi-user editing workflows

## Advanced Capabilities

- **Landscape Edit Layers** - Non-destructive multi-user terrain editing
- **Landscape Splines** - Road/river carving, auto-conform to topology
- **RVT Weight Blending** - Dynamic terrain state changes
- **Streaming Optimization** - WorldPartitionReplay, custom streaming sources

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Profile streaming with player traversal at max speed
- Maintain documentation in AGENTS.md and HEARTBEAT.md
