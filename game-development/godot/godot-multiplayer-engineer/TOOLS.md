# TOOLS.md -- Godot Multiplayer Engineer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `godot-4-pro` - Godot 4 multiplayer and networking

## MultiplayerAPI

- **ENetMultiplayerPeer** - Dedicated servers, LAN
- **WebRTCMultiplayerPeer** - Browser-based multiplayer
- **MultiplayerSpawner** - Dynamic networked node spawning
- **MultiplayerSynchronizer** - Property replication, visibility

## Authority Model

- **set_multiplayer_authority()** - Node ownership assignment
- **is_multiplayer_authority()** - Authority validation guards
- **Server Authority** - Peer ID 1 owns gameplay state
- **Client Input** - Requests via RPC, server decides

## RPC System

- **@rpc Decorator** - any_peer, authority, call_local modes
- **RPC Security** - Sender validation, input plausibility
- **RPC Modes** - reliable, unreliable, ordered
- **InvokeServer** - With timeout handling
- **InvokeClient** - Never use from server

## Scene Replication

- **MultiplayerSpawner** - Registered scenes, spawn_path
- **MultiplayerSynchronizer** - Property paths, replication config
- **ReplicationConfig** - ALWAYS, ON_CHANGE, NEVER modes
- **Visibility** - Who receives updates

## Network Architecture

- **Client-Server** - Peer 1 as dedicated/host server
- **P2P Topologies** - Each peer authority of own entities
- **WebRTC Signaling** - STUN/TURN, signaling server
- **NAT Traversal** - Connection establishment

## Testing & Debugging

- **Latency Simulation** - 100ms, 200ms testing
- **Network Profiler** - Bandwidth, packet loss
- **Authority Debugging** - get_multiplayer_authority() prints
- **Connection Lifecycle** - Connect, disconnect, reconnect

## Advanced Capabilities

- **Nakama Integration** - Matchmaking, lobbies, leaderboards
- **Custom Protocols** - PackedByteArray, delta compression
- **Lag Compensation** - Server-side snapshots, rollback
- **Relay Servers** - Packet forwarding, room routing

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Test at 150ms latency before shipping
- Maintain documentation in AGENTS.md and HEARTBEAT.md
