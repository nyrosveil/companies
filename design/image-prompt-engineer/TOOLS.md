---
updated: 2026-03-20 | 22:03
created: 2026-03-20 | 22:03
---
# TOOLS.md -- Image Prompt Engineer

## Core Skills

- `para-memory-files` - Memory operations and prompt library management
- `prompt-engineering` - Structured prompt architecture and platform optimization
- `photography-technical` - Camera specs, lighting, composition, depth of field
- `platform-specific-ai` - Midjourney, DALL-E, Stable Diffusion, Flux optimization
- `iterative-refinement` - Output analysis and prompt improvement cycles
- `aesthetic-direction` - Style guidance, brand alignment, visual consistency
- `photography-reference` - Photographer styles, film stocks, artistic movements
- `image-quality-assessment` - Artifact detection, technical flaw identification

## AI Image Generation Platforms

### Midjourney
- **Interface**: Discord-based, `/imagine` command
- **Strengths**: Artistic interpretation, style variety, strong composition
- **Weaknesses**: Inconsistent photorealism, hand/face artifacts
- **Parameters**: `--ar` (aspect ratio), `--v` (version), `--style`, `--chaos`, `--s` (stylization)
- **Weights**: `::` syntax (e.g., `cinematic lighting::2`)
- **Negative**: `--no` parameter for exclusions
- **Use Cases**: Concept art, creative exploration, stylistic imagery

### DALL-E (OpenAI)
- **Interface**: API, ChatGPT, Bing Image Creator
- **Strengths**: Text rendering, prompt adherence, safety filtering
- **Weaknesses**: Less artistic control, limited fine-tuning
- **Parameters**: `quality` (hd/standard), `size`, `style` (vivid/natural)
- **Weights**: Natural language emphasis ("very", "extremely")
- **Negative**: Include in prompt text ("no text, no watermark")
- **Use Cases**: Commercial-safe content, text-in-image, safe-for-work

### Stable Diffusion
- **Interface**: Local (Automatic1111, ComfyUI) or cloud (Replicate, RunPod)
- **Strengths**: Maximum control, custom models/LoRAs, unrestricted
- **Weaknesses**: Steeper learning curve, requires technical setup
- **Parameters**: Sampler, steps, CFG scale, seed, negative prompt
- **Weights**: `(keyword:1.3)` or `[keyword:0.8]`
- **Negatives**: Separate negative prompt field, use embeddings
- **Use Cases**: Photorealism, specific styles, full control

### Flux / Emerging Models
- **Interface**: Varies by provider (Replicate, Hugging Face, etc.)
- **Strengths**: Often state-of-art, improved prompt understanding
- **Weaknesses**: Rapidly changing, documentation may lag
- **Parameters**: Platform-specific, often simpler interfaces
- **Use Cases**: Cutting-edge quality, specific niche capabilities

## Prompt Architecture Deep Dive

### The 5-Layer System

#### Layer 1: Subject (Who/What)
- **Identity**: Age, gender, ethnicity, role, species (if non-human)
- **Appearance**: Hair, eyes, clothing, accessories, condition
- **Expression/Emotion**: Happy, contemplative, fierce, serene
- **Action/Pose**: Standing, sitting, jumping, looking, interacting

**Example**: "30-year-old East Asian woman with wavy black hair wearing a cream linen shirt, smiling warmly, looking at camera"

#### Layer 2: Environment (Where)
- **Location**: Studio, urban street, natural landscape, interior
- **Setting Details**: Specific objects, architecture, time of day
- **Atmosphere**: Foggy, sunny, rainy, golden hour, moody
- **Context**: Workplace, home, event, travel destination

**Example**: "Modern minimalist apartment living room with floor-to-ceiling windows overlooking city skyline at golden hour"

#### Layer 3: Lighting (How it Looks)
- **Source**: Natural (sun, window), artificial (studio lights, neon)
- **Direction**: Front, side, back, top, under
- **Quality**: Harsh (high contrast), soft (diffused), directional
- **Character**: Dramatic, even, split lighting, Rembrandt triangle
- **Color Temperature**: Warm (tungsten), cool (daylight), mixed

**Example**: "Soft golden hour side lighting through window creating gentle shadows on face"

#### Layer 4: Technical Camera (How it's Captured)
- **Focal Length**: 24mm (wide), 50mm (standard), 85mm (portrait), 200mm (telephoto)
- **Aperture**: f/1.4 (very shallow DOF), f/2.8 (moderate), f/8-11 (deep)
- **Camera Angle**: Eye level, low angle (heroic), high angle (diminishing), Dutch (tilted)
- **Shot Type**: Close-up, medium, full-body, extreme wide
- **Film/Quality**: 8K resolution, professional photography, cinematic

**Example**: "Shot on Canon EOS R5 with 85mm f/1.2 lens, shallow depth of field, eye-level perspective"

#### Layer 5: Style & Post-Processing
- **Photography Genre**: Portrait, fashion, documentary, commercial, fine art
- **Era/Aesthetic**: Vintage 1950s, contemporary, retro-futuristic
- **Photographer Reference**: "in the style of [photographer name]"
- **Film Stock**: "Kodak Portra 400", "Fuji Velvia 50", "Ilford HP5"
- **Color Grade**: High contrast B&W, muted tones, vibrant saturation, teal & orange
- **Quality Tags**: Professional, editorial, 8k, hyperrealistic, cinematic

**Example**: "Editorial portrait style, inspired by Annie Leibovitz, Kodak Portra 400 aesthetic, natural colors"

### Complete Prompt Example
```
Professional corporate headshot, 40-year-old Black man with short natural hair, wearing navy suit and blue shirt, confident smile, eye contact, modern office with blurred city background through glass windows, soft studio lighting with slight Rembrandt triangle, shot on Canon EOS R5 with 85mm f/1.8 lens, shallow depth of field, eye-level, business portrait style, corporate photography, clean, professional, sharp focus
```

## Genre-Specific Prompt Templates

### 1. Corporate Headshot
```
Corporate headshot, [person description], [attire: suit/business casual],
confident professional expression, eye contact, modern office background
[blurred/clean], soft even lighting, three-quarter view,
Canon 85mm f/1.8, shallow depth of field, corporate photography,
professional, clean background, sharp focus on eyes
```

### 2. E-Commerce Product
```
Product photography, [product description with materials],
on clean white background, studio lighting with softbox overhead,
shot from [angle: eye-level/45-degree/overhead], Canon 100mm macro lens,
product centered, shadow beneath, commercial quality,
white background, sharp focus, product catalog style
```

### 3. Lifestyle/Brand Campaign
```
Lifestyle photograph, [person(s)] [activity], [authentic setting],
natural lighting, candid moment, documentary style,
Leica M6, 35mm lens, available light, authentic, unposed,
brand campaign aesthetic, [brand style: minimal/rustic/urban],
film grain, warm tones, relatable, aspirational
```

### 4. Editorial Fashion
```
Fashion editorial photograph, model wearing [designer/clothing],
[setting: studio/location], dramatic lighting, high fashion styling,
inspired by [photographer: Tim Walker/Annie Leibovitz],
Vogue magazine style, ethereal, dreamlike, surreal elements,
8k resolution, cinematic, conceptual fashion
```

### 5. Architecture/Interior
```
Architecture photograph, [building/interior description],
[time of day: golden hour/blue hour/daylight],
shot from [perspective: wide/detail], architectural digest style,
clean lines, dramatic lighting, geometric composition,
Fujifilm GFX, tilt-shift lens, modernist architecture,
sharp, detailed, magazine quality
```

### 6. Food & Beverage
```
Food photography, [dish description], on [plate/surface],
natural window lighting, shallow depth of field, overhead angle,
Canon 50mm f/2.8, rustic background, steam rising, fresh,
cookbook style, appetizing, rich colors, professional food styling
```

### 7. Portrait (Environmental)
```
Environmental portrait, [person description with occupation],
[workplace/context], natural lighting in environment,
candid moment, documentary style, contextual details showing personality,
35mm film aesthetic, available light, authentic,
National Geographic style, storytelling, character study
```

## Platform Parameter Cheat Sheets

### Midjourney v6 Quick Reference
```
/imagine prompt: [full prompt with layers] --ar 16:9 --v 6 --style raw --chaos 20
```
- `--ar 16:9`: Landscape (use 1:1 square, 9:16 portrait, 2:3 portrait)
- `--v 6`: Version 6 (best for photorealism, prompt understanding)
- `--style raw`: Less artistic, more photographic (remove for artistic)
- `--chaos 0-100`: 0 = consistent, 100 = surprising variations
- Weighting: `keyword::2` for 2x importance, `keyword::0.5` for half

### DALL-E 3 Quick Reference
```
[Natural language prompt, conversational, specific]
```
- Quality: `"hd"` for high-detail (costs 2x credits)
- Size: `1024x1024` (square), `1024x1792` (portrait), `1792x1024` (landscape)
- Style: `"vivid"` (dramatic) or `"natural"` (photorealistic)
- Negative: embed in prompt: "no text, no watermark, professional"

### Stable Diffusion (Auto1111) Quick Reference
```
Positive: [full prompt], masterpiece, best quality, 8k
Negative: (worst quality, low quality, blurry, text, signature, watermark), bad-hands-5, EasyNegative
```
- Sampler: `DPM++ 2M Karras` (good quality, reasonable speed)
- Steps: `20-30` for quality, `30-50` for detailed
- CFG: `7` (balanced), `9` (prompt adherence), `5` (creative)
- Hires. fix: Enable for upscaling with 0.3-0.5 denoise

## Prompt Optimization Techniques

### Weighting & Emphasis
- **Midjourney**: `word::2` (double weight), `word::0.5` (half weight)
- **Stable Diffusion**: `(word:1.3)` increase, `[word:0.8]` decrease
- **General**: Repeat words for emphasis ("very very cinematic")
- **Order**: Earlier terms have more weight in some models

### Style Transfer & Artist References
- Use specific photographer names accurately: "Annie Leibovitz style"
- Film stocks create consistent color: "Kodak Portra 400"
- Movement references: "New Topographics", "Italian Renaissance painting"
- Mix carefully: "cinematic composition meets documentary authenticity"

### Negative Prompts (What to Exclude)
**Universal Negatives**:
```
text, watermark, signature, logo, blurry, low quality, worst quality,
jpeg artifacts, deformed, disfigured, extra fingers, malformed hands,
bad anatomy, mutation, ugly, duplicate, morbid, mutilated
```

**Genre-Specific**:
- **Portrait**: `plastic skin, airbrushed, overly smooth, mannequin`
- **Product**: `reflection, glossy, dust, fingerprints, shadows too harsh`
- **Architecture**: `people, cars, distortion, fish-eye, bent lines`
- **Fashion**: `cheap clothing, wrinkled, unstyled, bad fit`

### Iterative Prompt Refinement

**Cycle 1: Baseline**
Prompt: "A portrait of a businesswoman"
Result: Generic, not specific enough

**Cycle 2: Add Details**
Prompt: "Professional portrait of a businesswoman in office"
Result: Better but still generic lighting and composition

**Cycle 3: Technical Specifications**
Prompt: "Corporate headshot, 35-year-old woman in navy blazer, soft studio lighting, 85mm f/1.8, shallow depth of field"
Result: Much better, getting closer

**Cycle 4: Style & Quality**
Prompt: "Corporate headshot, confident East Asian businesswoman in navy suit, soft Rembrandt lighting, shot on Canon 85mm f/1.2, eye-level, shallow DOF, professional photography, sharp focus, 8k"
Result: **Success** - matches vision with technical precision

**Document Final Success**: Save winning prompt structure for future similar requests

## Quality Assessment Checklist

### Technical Quality
- [ ] Focus: Subject sharp where intended (eyes for portraits)
- [ ] Lighting: Appropriate for subject, no blown highlights or crushed shadows
- [ ] Composition: Framing follows principles (rule of thirds, balance)
- [ ] Perspective: Camera angle appropriate for subject/genre
- [ ] Resolution: Adequate detail, no pixelation at intended size

### AI Artifacts
- [ ] Hands/fingers: Correct count, no extra or fused digits
- [ ] Faces: Symmetry natural, no morphing, eyes properly shaped
- [ ] Text: None (or accurate if intentionally included)
- [ ] Repeated elements: No cloning patterns (identical background elements)
- [ ] Physics: Clothing, hair, objects behave naturally
- [ ] Body proportions: Natural proportions, no distortion

### Aesthetic & Brand
- [ ] Style matches genre expectations (portrait looks like portrait)
- [ ] Mood/Emotion conveyed effectively
- [ ] Color palette appropriate (warm, cool, saturated, muted)
- [ ] Brand alignment (if applicable)
- [ ] Professional quality (suitable for commercial use)

### Content & Ethics
- [ ] No harmful stereotypes or inappropriate content
- [ ] Representations are dignified and respectful
- [ ] No copyright infringement (recognizable characters/art)
- [ ] Legally safe for intended commercial use
- [ ] Culturally appropriate (coordinate with inclusive specialist)

## Photography Reference Library

### Photographer Style Guide
- **Annie Leibovitz**: Environmental portraits, dramatic lighting, rich color, celebrity
- **Peter Lindbergh**: Black & white, natural light, raw beauty, supermodels
- **Richard Avedon**: Minimalist white background, sharp, confrontational
- **Tim Walker**: Whimsical, fantastical, saturated, elaborate sets
- **Helmut Newton**: Bold, provocative, high contrast, strong shadows
- **Ansel Adams**: Landscape, majestic, black & white, Zone System
- **Henri Cartier-Bresson**: Candid, decisive moment, street photography
- **Gregory Crewdson**: Cinematic, elaborate lighting, narrative scenes
- **Mario Testino**: Glamorous, vibrant, fashion editorial
- **Sebastião Salgado**: Social documentary, black & white, epic scale

### Film Stock Characteristics
- **Kodak Portra 400**: Warm skin tones, natural colors, forgiving exposure
- **Kodak Ektar 100**: Ultra-saturated, fine grain, vibrant colors
- **Fuji Velvia 50**: Intense saturation, deep blues/greens, slide film look
- **Ilford HP5 Plus**: Classic B&W, high contrast, grain at 3200+
- **CineStill 800T**: Tungsten balanced, edge glow, cinematic
- **Kodak Tri-X**: Classic B&W, grainier, timeless look

### Lighting Patterns Quick Reference
- **Butterfly**: Light above and in front, shadow under nose like butterfly
- **Rembrandt**: Side light creating triangle of light on cheek
- **Loop**: Slight shadow from nose, doesn't connect to cheek shadow
- **Split**: Light from side, half face lit, half in shadow
- **High Key**: Bright, even lighting, minimal shadows
- **Low Key**: Dark, dramatic, high contrast, selective lighting
- **Broad**: Fill shadow side with reflectors for soft light
- **Short**: Side light with shadow side facing camera (dramatic)

## Continuous Improvement

### Track Success Patterns
- Which prompt structures work best for each genre
- Platform-specific optimizations that move needle
- Photographer references that yield consistent style
- Negative prompts that most effectively prevent artifacts
- Parameter tweaks (CFG, steps, chaos) for different use cases

### Community & Learning
- Follow prompt engineering communities (Midjourney Discord, SD subreddits)
- Share successful prompts in team knowledge base
- Document platform updates and model changes
- Experiment with new platforms and techniques
- Study photography continuously to improve technical vocabulary

## Tools for Reference & Workflow

### Photography References
- **500px**: Professional photography community
- **Behance**: Creative work with style diversity
- **Pinterest**: Visual reference and mood boarding
- **Magnum Photos**: Documentary photography archive
- **Vogue Archive**: Fashion photography history

### Prompt Management
- **Notion/Obsidian**: Personal knowledge base for prompts
- **Airtable**: Searchable prompt library with metadata
- **GitHub Gist**: Version control for prompt templates
- **Plain Text**: Simple files with clear naming conventions

### Organization Structure
```
prompts/
├── portraits/
│   ├── corporate.md
│   ├── environmental.md
│   └── creative.md
├── products/
│   ├── ecommerce.md
│   ├── hero-shot.md
│   └── detail.md
├── brand-[client]/
│   └── style-guide.md
├── platforms/
│   ├── midjourney-templates.md
│   ├── dalle-prompts.md
│   └── stable-diffusion.md
└── successful-generations/
    └── [date]-[project]-[seed].json
```

## Collaboration Guidelines

### With Visual Storyteller
- Provide imagery that supports narrative arcs
- Generate concept art before production
- Create style frames for video/motion projects
- Ensure visual continuity across still and motion assets

### With Brand Guardian
- Review generated images for brand guideline compliance
- Develop brand-specific prompt templates and style keywords
- Maintain brand image library with AI-generated assets
- Coordinate on brand evolution in visual style

### With UI Designer
- Generate placeholder images for prototypes
- Create illustration-style assets for interfaces
- Provide iconography and visual elements
- Ensure generated assets meet technical web requirements (size, format)

### With Inclusive Visuals Specialist
- Apply inclusive representation constraints in prompts
- Review generated images for authentic representation
- Balance aesthetic goals with inclusive standards
- Document successful inclusive prompting techniques

## Success Metrics

- **Prompt Success Rate**: % of generations meeting requirements (target >85%)
- **Iteration Efficiency**: Average generations to satisfactory result (target <5)
- **Platform Mastery**: Can optimize for each platform's unique syntax
- **Template Library**: Maintain 50+ effective prompt templates by genre
- **Brand Consistency**: Generated assets pass brand review on first submission
- **Quality Standards**: <5% of outputs have significant artifacts
- **Knowledge Sharing**: Document learnings for team benefit
- **Speed**: Can produce quality prompt for simple request in <10 minutes

## Professional Development

### Photography Education
- Online courses: Skillshare, Coursera, LinkedIn Learning
- Books: "Understanding Photography" by Bryan Peterson, "Light: Science and Magic"
- Practice: Real photography to improve eye for lighting, composition
- Study: Master photographers' work, understand their techniques

### AI/ML Understanding
- Follow AI image generation research papers
- Understand model limitations and capabilities
- Experiment with control nets, inpainting, outpainting
- Stay current with platform updates and new model releases

### Design & Aesthetics
- Study design principles (color theory, composition, typography)
- Understand brand identity systems and visual language
- Keep up with visual trends while maintaining timeless style
- Develop personal aesthetic sensibility

## Ethical Considerations

- **Copyright**: Don't generate images of living artists' distinctive styles without transformation
- **Consent**: Avoid generating images of real people without permission
- **Misinformation**: Don't create fake documentary-style images of real events
- **Commercial Use**: Understand each platform's commercial usage terms
- **Attribution**: Credit photographer style references when appropriate in documentation
- **Harmful Content**: Never generate hate speech, violence, adult content, etc.