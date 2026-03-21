# TOOLS.md -- Unity Multiplayer Engineer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Netcode for GameObjects (NGO)

- **NetworkVariable**: Persistent state replication with read/write permissions; dirty checking; change events
- **RPC Types**: ServerRpc (client → server with validation), ClientRpc (server → all clients), RpcTarget.Single/Owner/All
- **NetworkObject**: Spawn/despawn lifecycle; scene vs. dynamic; prefab registration in NetworkPrefabs
- **NetworkManager**: Connection management; hosting modes (Host, Server, Client); transport configuration
- **NetworkBehaviour**: IsOwner, IsServer, IsClient checks; networked field serialization; OnNetworkSpawn/Spawn/Despawn callbacks
- **Rpcs**: `[ServerRpc(RequireOwnership = true)]`, `[ClientRpc(excludeOwner = false)]` — ownership and delivery control

### Unity Transport & Simulation

- **UnityTransport**: Low-level UDP/RLNE transport; server binding, client connection; timeouts and reconnection
- **Network Simulator**: Inject artificial latency (100ms-400ms), packet loss (0-10%), jitter for testing
- **Bandwidth Throttling**: Simulate constrained network conditions for mobile/consoles
- **Connection Events**: Client connected/disconnected callbacks; graceful disconnect handling

### Unity Gaming Services (UGS)

- **RelayService**: Allocation creation, join code generation, player-to-player NAT traversal without direct IP
- **LobbyService**: Create/query/join lobbies; lobby data schema (public/member/private fields); heartbeat maintenance
- **AuthenticationService**: Anonymous, platform (Steam, Xbox Live, PSN); player identity persistence
- **Cloud Code**: Server-side functions hosted on UGS; validation logic outside game client
- **Distributed Authority**: Multi-player authoritative state using UGS components

### Client-Side Prediction Techniques

- **Input Prediction**: Local movement updates based on input buffer; immediate feedback
- **Server Reconciliation**: Buffer inputs, receive server state, resimulate to correct divergence
- **Move History**: Queue of recent inputs with timestamps for rollback; bounded memory
- **Threshold-Based Correction**: Only reconcile when position error > threshold; avoid small corrections every frame
- **Lag Compensation**: Design mechanics with 200ms+ in mind; avoid twitch reflex gates; telegraph attacks

### Snapshot Interpolation & Smoothing

- **Snapshot Buffering**: Store 2–3 latest server state updates; interpolate between them for remote players
- **Dead Reckoning**: Predict movement between snapshots using velocity/angular velocity; reduce network update frequency
- **Extrapolation**: Predict beyond latest snapshot with caution; correct on next snapshot arrival
- **Smoothing Factors**: Adjust interpolation delay to balance smoothness vs. input lag

### Anti-Cheat Architecture

- **Server-Side Validation**: All ServerRpc inputs validated with physics/capsule checks; never trust client position/health
- **Rate Limiting**: Track RPC call counts per player per second; disconnect exceed threshold
- **Movement Validation**: Velocity caps, teleport detection (distance > maxSpeed * timeSinceLastUpdate), wallhack detection (raycasts)
- **Hit Detection**: Server-authoritative raycasts; clients request, server validates and broadcasts
- **Audit Logs**: Structured logs of all game state changes with player ID, timestamp, RPC name, input values
- **Determinism**: Fixed timestep simulation; avoid `Random.Range` without seeding; physics determinism checks

### Bandwidth Optimization

- **Dirty Checking**: `NetworkVariable` only updates on value change (or via `NetworkVariableWritePermission.Owner` control)
- **Delta Compression**: Built-in delta compression for numeric types; custom delta logic for complex structs
- **Update Frequency Capping**: Separate update budgets per variable type; critical (60Hz), non-critical (10Hz)
- **Binary Serialization**: `INetworkSerializable.Write/Read` for custom efficient packing vs. reflection overhead
- **Object Pooling**: Reuse NetworkObjects to avoid spawn/despawn overhead and GC pressure

### NGO Advanced Patterns

- **Custom NetworkTransform**: Dead reckoning with configurable interpolation; reduce update frequency for distant objects
- **Scene Management**: Multiple scene loading with NetworkSceneManager; scene transition synchronization
- **Rollback Netcode**: Deterministic lockstep approach for fighting games; input delay and rollback on mismatch
- **Server Migration**: Host migration via new server host election; state transfer mechanisms
- **Client Pawn System**: Clients own only their pawn; server owns all world state; clean authority boundaries

### Testing & Debugging Tools

- **Network Simulation UI**: Runtime latency/packet loss adjustment; hot-reload without restart
- **Network Profiler**: NGO built-in bandwidth view per client/object; filter by NetworkVariable/RPC type
- **Dedicated Server Builds**: Headless mode testing; simulate multiple clients in one process for stress tests
- **Automated Lag Tests**: Scripted gameplay with varying simulated ping; verify prediction correctness
- **Packet Inspection**: Wireshark capture analysis; verify UDP traffic patterns and payload sizes

### Server Architecture

- **Headless Server**: Disable graphics/audio/input; compile with server scripting define; memory and CPU optimization
- **Docker Containerization**: Unity server build in Docker image; environment variables for config; health check endpoint
- **Server Orchestration**: Integration with GameLift, Multiplay, or custom Kubernetes for auto-scaling and matchmaking
- **Metrics Collection**: Player count, tick rate, bandwidth per instance; logging to Prometheus/CloudWatch
- **Session Management**: Graceful shutdown with session suspend/resume; allow reconnection within timeout

## Integration Recommendations

- Use para-memory-files for network architecture records, bandwidth budget sheets, and latency test reports
- Employ paperclip to coordinate multiplayer testing events and stress test scheduling
- Reference HEARTBEAT.md for daily network health check (desync incidents, bandwidth spikes, lag simulation outcomes)
- Activate tdd-guide agent when implementing new networked gameplay mechanics — validation logic must be proven
- Maintain a "Network Security Checklist" for every ServerRpc: validation rules, rate limits, logging coverage
- Say "no" to client-side authority; if the designer wants the client to decide, convert to "client requests, server validates"
- Test at 200ms from the first prototype — good LAN behavior is not good enough for internet play
- Set bandwidth targets early (e.g., 5 KB/s steady-state, 20 KB/s burst) and measure religiously
- Automate lag simulation in CI: run core gameplay loops at 100/200/400ms and assert no prediction failures
- Keep a desync incident log: track what failed, root cause, and how it was fixed to prevent reoccurrence
- Use NGO network profiler in every QA test session; watch for unexpected bandwidth growth from code changes