# TOOLS.md -- Blender Add-on Engineer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `blender-python` - bpy API and Blender scripting

## Blender Python (bpy)

- **bpy.data** - Data API access, context-independent operations
- **bpy.ops** - Operator calls (use sparingly, prefer data API)
- **bpy.types** - Custom operators, panels, property groups
- **bpy.props** - Property definitions, type hints

## Add-on Architecture

- **Registration** - Class registration, reload support
- **AddonPreferences** - Persistent settings storage
- **Property Groups** - Scene/object data, UI properties
- **Operators** - Execute functions, modal operators
- **Panels** - UI layout, VIEW_3D integration

## Pipeline Tools

- **Asset Validators** - Naming, transforms, material slots
- **Export Presets** - FBX, glTF, USD automation
- **Batch Processing** - Multi-object operations, progress reporting
- **Collection Management** - Export inclusion/exclusion rules

## Engine Handoff

- **FBX Export** - Unreal, Unity compatibility
- **glTF Export** - Web, Godot, standard PBR
- **USD Export** - High-end pipelines, interchange
- **Validation Reports** - Error checking, suggested fixes

## UI/UX Design

- **Panel Layout** - VIEW_3D > Pipeline category
- **Progress Bars** - Long operations, cancellable tasks
- **Dry-Run Modes** - Preview changes before applying
- **Logging** - Batch operation tracking, undo support

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Prefer bpy.data over bpy.ops for reliability
- Maintain documentation in AGENTS.md and HEARTBEAT.md
