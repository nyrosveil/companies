# TOOLS.md -- Unity Editor Tool Developer

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `paperclip-create-agent` - Hiring and creating new agents
- `internal-comms` - Internal communications and updates

## EditorWindow Development

- **UI Toolkit (UIElements)**: Modern XML/USS-based editor UI with data binding and responsive design
- **IMGUI (Immediate Mode GUI)**: Traditional OnGUI-based windows; familiar but less performant for complex UI
- **Custom VisualElements**: Reusable editor widgets (graph views, tree views, progress dashboards) with USS styling
- **State Persistence**: Window field serialization or EditorPrefs for persistence across script reloads
- **Progress Feedback**: EditorUtility.DisplayProgressBar for long operations; cancelation support
- **Undo Integration**: RecordObject calls for all editable changes; group correlated changes with Undo.SetCurrentGroupName

## PropertyDrawer & CustomEditor

- **Inspector Customization**: Type-custom drawers for Vector2, MinMaxRange, LayerMask, Tag fields
- **Composite Data Editing**: Multi-field structs (FloatRange, Vector2IntRange) with custom visual treatment
- **Prefab Overrides**: BeginProperty/EndProperty compliance for clean prefab workflow integration
- **Conditional Drawing**: Show/hide fields based on enum selection or boolean flags
- **Validation Decorators**: Inline warnings/errors for out-of-bounds values or missing references
- **Performance Drawing**: Height caching, off-main-thread calculation, efficient repaint paths

## AssetPostprocessor & Import Automation

- **Import Settings Enforcers**: Texture format, mesh compression, animation rigidity per folder/path pattern
- **Naming Convention Validators**: ScriptableObject creation from naming, component attachment based on filename
- **Auto-Configuration**: Animation controller state setup, material property naming, shader assignment
- **Format Conversion**: PSD to PNG/TGA, FBX import settings, audio compression selection
- **Budget Enforcement**: Max polygon count warnings, texture resolution limits, audio sample rate caps
- **Platform Overrides**: Per-platform compression, resolution, sampling rate for optimized builds

## Build Validation & Pipeline

- **Pre-Build Validators**: IPreprocessBuildWithReport for asset quality, scene setup, shader issues
- **Post-Build Auditors**: IPostprocessBuildWithReport for output verification and external integration
- **Custom Build Tasks**: Scriptable Build Pipeline (SBP) implementations for granular build control
- **Content Packaging**: Automated asset bundle creation with dependency tracking and versioning
- **Build Performance**: Incremental build caching, parallel asset processing, variant deduplication
- **Platform Customization**: Parameterized build pipelines with platform-specific configurations

## Menu & Context Integration

- **Top Bar Menus**: MenuItem in "Tools/" for project-wide operations and configuration panels
- **Right-Click Context**: ContextMenu on Components or Assets for targeted quick actions
- **Project Browser Enhancements**: AssetModificationProcessor for VCS support and metadata preservation
- **Scene View Gizmos**: Handles and GUI in SceneView for in-world editing controls
- **Hierarchy Additions**: GameObjectMenu for custom creation flows with preset components
- **Inspector Header Actions**: DecoratorDrawers for adding buttons or status icons to component headers

## Advanced Capabilities

### Assembly Definition Architecture
- **Domain Separation**: Gameplay, editor-tools, tests, shared libraries via .asmdef files
- **Compile-Time Enforcement**: Editor assemblies reference gameplay; never backward
- **Testable Interfaces**: Public API exposure through asmdefs to enforce testability via reference boundaries
- **Compilation Optimization**: Small targeted assemblies reduce full recompilation time

### CI/CD Editor Automation
- **Headless Editor Validation**: Batchmode execution of full project audits and asset validation
- **Edit Mode Testing**: Unit/integration tests for editor tools via Unity Test Runner
- **Automated Reporting**: CSV/text reports of asset violations, build times, memory usage
- **Scripted Submission Checks**: VCS pre-submit hooks checking for common asset/content issues

### Scriptable Build Pipeline Integration
- **Build Content Control**: Asset inclusion/exclusion, compression strategy, build target variants
- **Shader Optimization**: Automatic shader variant collection pruning, platform-sensitive compilation
- **Incremental Bundling**: Smart bundle regeneration based on asset dependency change tracking
- **Progress Monitoring**: Per-task duration tracking to identify optimization opportunities

### UI Toolkit Advanced Patterns
- **Responsive Layouts**: USS-based UI that adapts to window size and editor theme (dark/light)
- **Data Binding Systems**: Direct UI-from-serialized-data without manual refresh/update logic
- **Custom Control Libraries**: Reusable editor-specific variants (color pickers, icon selectors, tiled previews)
- **Theme Support**: StyleSheet variables for consistent styling across dark/light editor modes

### External Tool Integration
- **File Watchers**: Asset creation/modification hooks for Photoshop/Maya/etc completion synchronization
- **Process Communication**: Bridge to external build systems, art asset generators, data pipeline tools
- **Metadata Preservation**: GUID and reference retention during external asset refresh flows
- **Conflict Mediation**: Simultaneous editor/external modification handling with sensible merge strategies

## Integration Recommendations

- Use para-memory-files for tool specifications, user adoption tracking, and time savings documentation
- Employ paperclip to coordinate tool development with actual end users through iterative feedback loops
- Reference HEARTBEAT.md for daily build and import validation checklist execution
- Activate tdd-guide agent before implementing editors that will support ongoing project evolution
- Always prototype rapidly with end users — don't guess what they want; show them and adapt
- Prioritize imperative metrics: "saving X minutes per Y action" over speculative feature landscapes
- Build tool changelogs as inline comments at the top of files — nobody reads separate docs that get forgotten
- Structure every editor extension with Undo support as base requirement — anything else is hostile to users
- Enforce tool visual responsiveness: >0.5s operations must show progress or move to background thread
- Design all AssetPostprocessor rules as idempotent transforms — same input must always produce same output