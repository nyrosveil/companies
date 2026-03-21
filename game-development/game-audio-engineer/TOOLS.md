# TOOLS.md -- Game Audio Engineer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## Middleware & Engines

- **FMOD Studio**: Event-based audio, parameter-driven music, DSP effects, voice management
- **Wwise**: Interactive audio, sound structuring, motion-to-sound, profiling tools
- **Unity Audio**: Native AudioSource, AudioMixer, AudioReactive properties; FMOD integration
- **Unreal Engine**: AudioComponent, SoundCues, MetaSounds, FMOD/Wwise integrations
- **Godot**: AudioStreamPlayer, AudioBus, AudioReverb, custom GDScript audio controllers

## Audio Implementation Patterns

- **Event-Driven Architecture**: All gameplay audio triggered via named events, not direct playback
- **Parameter-Driven Systems**: Gameplay state (health, intensity, speed) modulates audio parameters in real-time
- **Audio State Machine**: Global audio mode (exploration, combat, cinematic) with transition rules
- **Singleton Audio Manager**: Centralized playback control, parameter setting, event registration
- **Voice Pooling & Stealing**: Priority-based voice limit management with configurable steal modes

## Adaptive Music Systems

- **Music States**: Exploration, combat, stealth, cinematic, victory, death
- **Transition Management**: Tempo-synced crossfades, beat-locked changes, no mid-bar cuts
- **Parameter Mapping**: Intensity, tension, time-of-day, player health drive music layers
- **Horizontal Re-sequencing**: Stem-based arrangement changes; different sections play based on state
- **Vertical Layering**: Additive tracks (drums, bass, strings) enter/exit based on parameters
- **Stems & Mixes**: Pre-mixed layer files vs. live mixing; trade-offs in memory vs. flexibility

### Spatial Audio & 3D Sound

- **3D Spatialization**: Distance attenuation curves, directional spread, doppler effects
- **Occlusion & Obstruction**: Raycast-based parameter modulation; low-pass filtering through walls
- **Reverb Zones**: Environment-matched presets (outdoor, indoor, cave, metal) with reverb buses
- **Ambisonics**: First-order ambisonics (FOA) for VR; binaural decoding for headphones
- **HRTF Processing**: Head-related transfer functions for elevation cues in 3D audio
- **Sound Propagation**: Multi-bounce reverb, early reflections, occlusion modeling

### Performance & Budgeting

- **Voice Count Budgets**: Per-platform max simultaneous voices (PC: 64, Console: 48, Mobile: 24)
- **Virtual Voice System**: Voice promotion/demotion for efficient playback
- **Memory Budgeting**:
  - SFX Pool: ≤ 32 MB, ADPCM, decompress to RAM
  - Music: ≤ 8 MB, Vorbis, stream from storage
  - Ambience: ≤ 12 MB, Vorbis, stream
  - VO: ≤ 4 MB, Vorbis, stream
- **CPU Profiling**: DSP cost ≤ 1.5ms/frame on lowest target; spatial audio raycasts ≤ 4/frame
- **Compression Formats**: Vorbis (music/ambience), ADPCM (short SFX), PCM (UI), Ogg Vorbis for mobile

### Event Architecture & Standards

- **Naming Conventions**: `event:/Category/Subcategory/EventName` (e.g., `event:/SFX/Player/Footstep_Concrete`)
- **Hierarchical Organization**: SFX, Music, Ambience, VO, UI top-level categories
- **Event Reference Caching**: Store event references in code, avoid string lookup every play
- **One-Shot vs. Persistent**: One-shot SFX; persistent music/ambience instances with parameter control
- **Event Parameterization**: Expose parameters (intensity, wetness, pitch) for runtime modulation

### Audio Quality Assurance

- **Automated Regression**: CI pipeline runs audio event validation; check parameter existence, voice limits
- **Performance Baselines**: Compare voice count, CPU usage, memory against baseline per build
- **Platform Certification**: Loudness (LUFS), channel layout, PCM format requirements per platform
- **Diagnostic Overlays**: Developer HUD showing active voices, current parameters, reverb zones
- **Audio Mix Validation**: Ensure no clipping, proper bus hierarchy, VCAs functional

### Advanced Capabilities

#### Procedural & Generative Audio
- **Synthesis-Based SFX**: Oscillators + filters for engine sounds, UI blips; reduces memory footprint
- **Parameter-Driven Sound Design**: Footstep material/speed/wetness modulate synthesis parameters
- **Granular Synthesis**: Ambient textures that never loop; grain density, pitch, duration modulation
- **Pitch-Shifted Harmonic Layering**: Same sample transposed creates different emotional register

#### Platform-Specific Audio
- **Mobile Optimization**: ADPCM compression, reduced voice count, simpler DSP chains
- **Console Certification**: Dolby Atmos, DTS:X object audio; TV speaker bass management
- **PC Scalability**: User audio settings mapped to quality presets (low/med/high/ultra)
- **VR Audio**: Ambisonics for 3D, HRTF processing, head-locked vs. world-locked sound decisions

#### Tool Development
- **DCC Scripts**: Blender/Maya Python scripts for audio asset batch processing (normalize, convert format)
- **Editor Extensions**: Unity Editor windows for FMOD event browsing, parameter debugging
- **Audio CI/CD**: Automated audio regression tests, build-time audio asset validation
- **Runtime Debugging**: In-game audio visualization (3D sound spheres, parameter graphs)

#### Composition & Implementation Workflow
- **Audio Design Document**: Sonic identity adjectives, gameplay-audio mapping, parameter definitions
- **MiddleWare Project Setup**: Event hierarchy, bus structure, platform overrides before asset import
- **Randomization**: Pitch, volume, multi-shot randomization; no two identical playback events
- **Mix Bus Effects**: Per-bus EQ, compression, reverb; global mix bus mastering

### Integration Recommendations

- Use para-memory-files for all audio budgets, middleware configuration backups, and parameter mappings
- Employ paperclip to coordinate sound design deliveries with implementation milestones
- Reference HEARTBEAT.md for daily audio performance triage
- Activate tdd-guide agent before implementing new audio architecture or middleware integration
- Keep a "parameter flow" diagram linking gameplay systems to audio parameters
- Say "no" to hardcoded audio playback — every SFX must go through an event
- Profile on target hardware daily; audio performance varies wildly across mobile/console/PC
- Automate voice limit validation in CI; catch budget violations before they reach QA
- Test adaptive music transitions at all state change boundaries; tempo sync is non-negotiable
- Document every audio system with a block diagram: triggers → parameters → middleware logic → output buses