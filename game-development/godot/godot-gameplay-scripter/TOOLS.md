# TOOLS.md -- Godot Gameplay Scripter

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `godot-4-pro` - Godot 4 engine and GDScript 2.0

## GDScript 2.0

- **Static Typing** - Type annotations, typed arrays, strict mode
- **Signal System** - Typed signals, snake_case naming, EventBus pattern
- **Node System** - Composition, @onready, scene instancing
- **Autoloads** - Global state, service locators, signal buses

## Scene Architecture

- **Composition Pattern** - HealthComponent, MovementComponent, etc.
- **Scene Independence** - F6 test, no parent assumptions
- **Resource System** - ScriptableObject equivalent, data-driven design
- **Node Lifecycle** - _ready(), _exit_tree(), queue_free()

## Godot 4 Features

- **GDScript 2.0** - Typed callables, await, super()
- **Typed Arrays** - Array[EnemyData], Array[Node]
- **Signal Connections** - Callable, bind(), CONNECT_ONE_SHOT
- **Export System** - @export, @export_group, @export_subgroup

## C# Integration

- **GDScript/C# Interop** - Signal connections, method calls
- **Performance-Critical Code** - .NET for hot paths
- **Library Access** - NuGet packages, .NET ecosystem

## Testing & Debugging

- **Scene Isolation** - F6 standalone testing
- **@tool Scripts** - Editor-time validation
- **Assertions** - assert() for invariant checking
- **Debugger** - Breakpoints, variable inspection

## Advanced Capabilities

- **GDExtension** - C++ performance critical systems
- **RenderingServer** - Low-level 2D/3D rendering
- **Custom Resources** - Data assets, configuration
- **Scene Pooling** - remove_from_parent(), re-parenting

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Enable strict typing in project settings
- Maintain documentation in AGENTS.md and HEARTBEAT.md
