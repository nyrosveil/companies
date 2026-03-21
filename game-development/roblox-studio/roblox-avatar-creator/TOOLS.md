# TOOLS.md -- Roblox Avatar Creator

## Core Skills

- `para-memory-files` - Memory operations and PARA methodology
- `paperclip` - Paperclip orchestration and agent management
- `roblox-luau` - Roblox scripting for avatar systems

## 3D Asset Creation

- **Blender** - Modeling, rigging, UV unwrapping, texture baking
- **Mesh Specifications** - Triangle budgets (4K accessories, 10K bundles)
- **UV Mapping** - [0,1] space, 2px padding, no overlapping
- **Transform Hygiene** - Applied scale/rotation, origin positioning

## Roblox Avatar System

- **R15 Rig** - Bone structure, weight painting, attachment points
- **Layered Clothing** - Inner/outer cages, deformation setup
- **Accessory Attachment** - Attachment names, body type compatibility
- **HumanoidDescription** - ApplyDescription, GetAppliedDescription

## Creator Marketplace

- **Asset Submission** - FBX/OBJ export, PNG textures, thumbnails
- **Moderation Compliance** - Policy review, content guidelines
- **Pricing Strategy** - Market research, Robux tiers
- **Limited Items** - Eligibility, series design, secondary market

## In-Experience Systems

- **Avatar Customization** - HumanoidDescription API, outfit saving
- **UGC Shops** - MarketplaceService:PromptPurchase
- **Outfit Management** - DataStore persistence, outfit slots
- **Cross-Experience** - Outfit APIs, earned cosmetics

## Testing & Validation

- **Body Type Testing** - Classic, Normal, Rthro Narrow, Rthro Broad
- **Animation Testing** - Idle, walk, run, jump, sit cycles
- **Export Checklists** - Mesh, texture, attachment validation
- **Clipping Detection** - Visual validation across all poses

## Integration Recommendations

- Use para-memory-files for knowledge management
- Leverage Paperclip for agent coordination
- Test on all 5 body types before submission
- Maintain documentation in AGENTS.md and HEARTBEAT.md
