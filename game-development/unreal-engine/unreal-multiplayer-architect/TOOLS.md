# TOOLS.md -- Unreal Multiplayer Architect

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Unreal Replication System

- **Replicated Properties**: `UPROPERTY(Replicated)`; `ReplicatedUsing` for change notifications; `GetLifetimeReplicatedProps` override
- **Conditional Replication**: `DOREPLIFETIME_CONDITION` with `COND_OwnerOnly`, `COND_SimulatedOnly`, `COND_SkipOwner`, `COND_InitialOnly`
- **Network Priority**: Override `GetNetPriority()`; influence replication frequency based on relevance to client
- **Update Frequency**: `NetUpdateFrequency` and `MinNetUpdateFrequency` per actor class; avoid default 100Hz for most actors
- **Lifetime Properties**: `DOREPLIFETIME`, `DOREPLIFETIME_CONDITION`; proper registration in `GetLifetimeReplicatedProps`
- **Rep Notify**: `UFUNCTION()` with `ReplicatedUsing`; client-side reaction to state changes; avoid heavy work in RepNotifies

## RPC & Authority Patterns

- **Server RPC**: `UFUNCTION(Server, Reliable)` or `(Unreliable)`; mandatory `WithValidation` tag for gameplay-affecting
- **Validation Functions**: `ServerRPC_Validate(parameters)` return bool; reject invalid inputs before `_Implementation`
- **Client RPC**: `UFUNCTION(Client, Reliable)` or `(Unreliable)`; executed on client; use for updates, not requests
- **NetMulticast**: `UFUNCTION(NetMulticast, Unreliable)` for cosmetic effects to all clients and server
- **Reliability**: `Reliable` for guaranteed order; `Unreliable` for frequent/visual data; never mix in same logical flow
- **RPC Ownership**: Server RPCs can require caller ownership (`RequireAuthority = true`); prevents unauthorized calls

## Network Architecture Components

- **GameMode**: Server-only; never replicated; spawn logic, rule arbitration, win conditions
- **GameState**: Replicated to all; shared world state (timer, scores, game phase)
- **PlayerState**: Replicated to all; per-player public data (name, ping, kills, team)
- **PlayerController**: Replicated to owning client only; input handling, camera, HUD
- **Pawn/Character**: Replicated to all; gameplay state (health, position, status)
- **Authority Checks**: `HasAuthority()`, `IsLocallyControlled()`, `IsPlayerControlled()`; use correctly in gameplay code

## Performance Optimization

- **Replication Frequency**: Set `NetUpdateFrequency` per actor: fast-moving (60–100Hz), normal (20–30Hz), static (2–5Hz)
- **Conditional Replication**: Use `COND_OwnerOnly` for private state; `COND_SimulatedOnly` for cosmetic updates; reduces bandwidth
- **Property Filtering**: Only replicate what all/some clients need; avoid replicating transient or local-only state
- **Network Priority**: Override `GetNetPriority` for relevance-based frequency; closer/higher priority actors replicate more often
- **Replication Graph**: Enable plugin for spatial partitioning; reduces bandwidth in large worlds with many players
- **Bandwidth Budgeting**: Target <15 KB/s per player steady-state; use `stat net` and Network Profiler to measure

## GAS (Gameplay Ability System)

- **ASC Replication**: `UAbilitySystemComponent` must be configured correctly: `SetReplicationMode(EAGReplicationMode::Mixed)` for hybrid authority
- **Dual Init Pattern**: Server: `PossessedBy(AController*)` calls `InitAbilityActorInfo`; Client: `OnRep_PlayerState()` calls same
- **Attribute Sets**: `UAttributeSet` subclasses; replicated properties automatically; configure `ReplicatedUsing` if needed
- **Prediction Keys**: `FPredictionKey` scopes predicted ability activations; server confirms or rejects via RPC
- **GameplayEffectContext**: Carry hit results, ability source, custom data through GAS pipeline; replicate via `FGameplayTag`
- **GAS Performance**: Monitor replicated attribute count; minimize `GameplayEffect` payload size; use `PredictionKey` correctly to avoid desync

## Server Configuration

- **Dedicated Server Build**: `RunUAT.bat BuildCookRun -server -platform=Linux -serverconfig=Shipping`
- **Network Settings**: `TotalNetBandwidth=32000` (bits/sec), `MaxDynamicBandwidth=7000`, `MinDynamicBandwidth=4000`
- **Beacon System**: `AOnlineBeaconHost` for server discovery; `AOnlineBeaconClient` for client connection; lightweight pre-session queries
- **Server Optimization**: Disable rendering (`-nographics`), audio (`-nosound`), input; headless mode for production
- **Server Clustering**: `UGameInstance` subsystem for registration with matchmaking; health check endpoints; graceful migration

## Debugging & Profiling Tools

- **Network Profiler**: `stat net`, `netstats`, `net.RepGraph`; per-actor bandwidth; RPC counts; replication frames
- **Replication Visualization**: `p.NetShowCorrections 1` shows prediction corrections; `p.NetDebug` for detailed logs
- **Lag Simulation**: `p.NetPktLag=200`, `p.NetPktLoss=5` inject latency/packet loss; test prediction and reconciliation
- **Replication Graph Debug**: `net.RepGraph.PrintAllNodes` prints spatial node distribution; identify hotspot cells
- **Server Logs**: `-log` for net logging; filter `LogNet` category; `LogNetPlayer` for player-specific events
- **Unreal Insights**: Trace sessions; network events timeline; correlate with gameplay and rendering

## Anti-Cheat Implementation

- **RPC Validation**: Mandatory `_Validate` on all Server RPCs; reject out-of-range values; rate limit per-player; timestamp checks
- **Movement Validation**: Server-authoritative movement; velocity caps; teleport detection (`Distance > MaxSpeed * DeltaTime * Tolerance`)
- **Cheat Detection Logging**: Audit log for game-affecting actions: player ID, RPC name, input values, timestamp, results
- **Server Authority Enforcement**: No client-owned damage, score, inventory; server owns all truth; clients only request
- **Input Sanitization**: Clamp values; check feasibility; validate against game state (distance, cooldowns, resources)
- **Replay System**: Record authoritative game state; allow replay of suspicious matches for forensic analysis

## Advanced Patterns

### Network Prediction Framework
- **Prediction Proxy**: `FNetworkPredictionStateBase` subclasses for movement, abilities, interactions
- **Prediction Key Management**: Scope predicts to server confirmation; rollback on correction; reuse keys after resolution
- **Authority Correction**: Use framework's built-in correction path; avoid custom position resets; integrate with `APawn::ServerMove`
- **Performance**: Measure rollback frequency; minimize prediction scope; profile simulation cost under latency

### Replication Graph Strategies
- **Spatial Partitioning**: `UReplicationGraphNode_GridSpatialization2D` for open worlds; cell-based relevancy
- **Dormancy Optimization**: Actors with no nearby players go dormant; minimal replication; wake on proximity
- **Custom Nodes**: Implement `UReplicationGraphNode` for special relevancy rules (team-only, quest-specific)
- **Bandwidth Savings**: Replication Graph can reduce bandwidth by 40–60% in large worlds with sparse player distribution

### Dedicated Server Infrastructure
- **Beacon Architecture**: `AOnlineBeaconHost` for session info without full game; lightweight player discovery
- **Cluster Management**: Custom `UGameInstance` subsystem registers with matchmaking service; heartbeats; capacity reporting
- **Session Migration**: Transfer `SaveGame` and critical state when host disconnects; allow reconnection within timeout
- **Health Monitoring**: Metrics endpoints (Prometheus format); player count, tick rate, bandwidth; alert on anomalies

### Advanced GAS
- **Prediction Keys Granularity**: One key per ability activation or combo; scope predictions correctly to avoid cross-ability rollbacks
- **GameplayEffectContext Customization**: Subclass `FGameplayEffectContext` to carry additional data (hit location, ability source, custom tags)
- **Server-Authoritative Abilities**: Client predicts ability start; server validates activation conditions; applies effects; sends confirmation
- **Montage Replication**: `UAnimMontage` replication via ASC; prediction key scoping for montage timing correction

## Integration Recommendations

- Use para-memory-files for replication architecture records, bandwidth budget sheets (per actor class), GAS config schemas, server deployment manifests
- Employ paperclip to coordinate multiplayer testing events, lag simulation campaigns, and cheat vector security reviews
- Reference HEARTBEAT.md for daily network health checklist (replication stats, bandwidth compliance, validation coverage)
- Activate tdd-guide agent when implementing new Server RPCs to test validation logic and rollback behavior
- Maintain a "Network Performance Baseline" document: per-actor bandwidth targets, tick rate requirements, player count caps
- Build automated regression tests for network code: use `PNetDriver` to simulate clients, test RPC validation, measure bandwidth changes
- Say "no" to any feature request that adds unvalidated Server RPCs or replicated properties without bandwidth analysis
- Use Replication Graphs for any game with >50 simultaneous actors and multiple players in proximity
- Profile on dedicated server hardware, not listen server in editor — CPU and network behavior differs significantly
- Create a "Server RPC Audit Spreadsheet" tracking all Server RPCs, their validation logic, bandwidth cost, and cheat risk
- Implement server-side cheat detection from day one; retrofitting security after launch is nearly impossible
- Test at 200ms simulated latency continuously; what feels good on LAN will break on internet