# TOOLS.md -- Roblox Systems Scripter

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `roblox-luau` - Luau language and Roblox API expertise

## Luau Programming

- **Static Typing** - Type annotations, type inference, strict mode
- **Module Architecture** - ModuleScript patterns, dependency management
- **Parallel Luau** - task.desynchronize(), Actor model, SharedTable
- **Memory Management** - Instance pooling, :Destroy() vs Parent = nil

## Roblox Networking

- **Client-Server Model** - Authority boundaries, validation patterns
- **RemoteEvents** - FireServer, FireClient, OnServerEvent, OnClientEvent
- **RemoteFunctions** - InvokeServer (sparingly), security considerations
- **Security Best Practices** - Input validation, sender verification

## Data Persistence

- **DataStoreService** - GetAsync, SetAsync, UpdateAsync patterns
- **Retry Logic** - pcall wrapping, exponential backoff
- **Data Versioning** - Schema migration, _version field
- **Session Management** - PlayerRemoving, BindToClose, session locking

## Roblox Services

- **Players** - Player lifecycle, UserId management
- **ReplicatedStorage** - Shared modules, RemoteEvents
- **ServerStorage** - Server-only logic and modules
- **StarterPlayer/StarterGui** - Client initialization

## Advanced Capabilities

- **OrderedDataStore** - Leaderboards, top-N queries
- **MemoryStore** - Temporary data, rate limiting
- **MessagingService** - Cross-server communication
- **HttpService** - External API integration

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Validate all client inputs on server
- Maintain documentation in AGENTS.md and HEARTBEAT.md
