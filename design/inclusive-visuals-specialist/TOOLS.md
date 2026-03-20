---
updated: 2026-03-20 | 22:03
created: 2026-03-20 | 22:03
---
# TOOLS.md -- Inclusive Visuals Specialist

## Core Skills

- `para-memory-files` - Memory operations and inclusive asset repository
- `bias-mitigation-prompting` - AI model bias countermeasures in prompt engineering
- `cultural-competence` - Global cultures, authentic representation, intersectionality
- `ethical-ai-governance` - Ethical frameworks, guidelines, standards development
- `community-validation` - Perception testing, real-world feedback gathering

## AI Image Generation Expertise

### Platform-Specific Prompting

#### Midjourney
- **Bias Countermeasures**: `--no stereotype, clone face, generic smile, exaggerated features`
- **Cultural Specificity**: Use geographic regions, not broad continents
- **Negative Prompts**: `--no text, symbols, futuristic, sci-fi, exotic lighting`
- **Version Differences**: v5 vs v6 bias patterns and improvements

#### DALL-E (OpenAI)
- **Natural Language**: Detailed descriptive constraints in prompt body
- **Content Moderation**: Navigate content policies for authentic representation
- **Style Control**: Photorealism vs illustration bias considerations
- **Negative Prompts**: "no stereotypical, no exaggerated features, no text"

#### Stable Diffusion
- **Negative Embeddings**: `bad-hands-5, EasyNegative, bad_prompt` for artifacts
- **Model Selection**: Community checkpoints vary in bias intensity
- **Token Weighting**: `(cultural accuracy:1.3)` for emphasis
- **LoRA Integration**: Cultural accuracy LoRAs when available

#### Flux / Other Models
- **Platform-Specific Syntax**: Learn each model's constraint language
- **Bias Documentation**: Track model-specific failure modes
- **Prompt Optimization**: Continuous refinement based on outputs

### Video Generation

#### Sora
- **Temporal Consistency**: Define physics explicitly ("movement smooth and deliberate")
- **Mobility Aids**: "Wheelchair wheels maintain consistent contact with pavement"
- **Cultural Motion**: "Natural body language, not stereotypical gestures"
- **Lighting Consistency**: "Lighting remains consistent throughout scene"

#### Runway Gen-3
- **Motion Description**: "Natural, realistic movement without physics errors"
- **Clothing Physics**: "Fabric drapes naturally, respects body movement"
- **Hair Dynamics**: "Hair movement realistic for hair type and environment"

## Cultural Competence Frameworks

### Geographic & Cultural Specificity

#### Avoid Broad Categories
- ❌ "African person" → ✅ "Nigerian Yoruba person, Ibadan"
- ❌ "Asian person" → ✅ "Korean person, Seoul, Gangnam district"
- ❌ "Middle Eastern" → ✅ "Lebanese person, Beirut, Mar Mikhael"
- ❌ "Latino/Hispanic" → ✅ "Colombian person, Medellín, Comuna 13"

#### Architectural Accuracy
- Research authentic architecture for locations
- Avoid generic "local" structures that don't exist
- Include culturally-specific environmental details
- Consider urban/rural/suburban accurately

#### Clothing & Adornment
- Accurate traditional clothing for occasions
- Modern clothing with cultural specificity
- Proper fit and styling (not "costume-like")
- Regional variations within cultures respected

### Intersectionality Framework

#### Identity Dimensions to Capture
- **Race/Ethnicity**: With geographic/cultural specificity
- **Age**: Specific decade, not "young/old"
- **Gender Identity**: Precise terminology, avoid assumptions
- **Disability**: Assistive devices visible and functional
- **Socioeconomic Status**: Environment, clothing, context indicators
- **Body Type**: Diverse body shapes and sizes (not default thin/toned)
- **Religious Identity**: Accurate symbols, practices, attire when relevant

#### Variation in Groups
When depicting multiple people:
- **Age Distribution**: Mix of ages, not all same generation
- **Body Types**: Various sizes, not homogenized
- **Facial Structures**: Distinct bone structure, not identical faces
- **Attire**: Different clothing styles within cultural context
- **Abilities**: Mix of visible/invisible disabilities if appropriate

## Negative Constraint Library

### Universal Exclusions
```
- No clone faces
- No exaggerated stereotypical features
- No generic stock-photo smiles
- No text, logos, symbols, signage (unless specific and accurate)
- No gibberish characters in non-Latin scripts
- No hyper-saturated artificial lighting on dark skin tones
- No futuristic/sci-fi tropes in realistic scenes
- No hero-symbol compositions (oversized cultural symbols)
- No cultural appropriation aesthetics
- No harmful stereotypes or tropes
```

### Context-Specific Exclusions

#### Professional Settings
```
- No white savior narratives
- No "only woman in room" tokenism
- No hacker-in-hoodie stereotypes
- No CEO always white/male/older
```

#### Cultural/Religious
```
- No exoticizing lighting or composition
- No inaccurate cultural artifacts
- No religious symbols used decoratively/incorrectly
- No sacred elements as aesthetic backdrop
```

#### Family/Community
```
- No dysfunctional minority family tropes
- No poverty tourism
- No monolithic community representation
- No stereotype-conforming family structures only
```

## Validation Frameworks

### 7-Point QA Checklist Recap
1. **Facial Diversity**: All faces distinct, ages varied
2. **Cultural Accuracy**: Context matches real-world authenticity
3. **Physical Reality**: Natural movement, physics, lighting
4. **No Gibberish**: Text/symbols accurate or absent
5. **Human Subject**: People not overshadowed by symbols
6. **Intersectionality**: Multiple identity dimensions
7. **Community Perception**: Authentic to represented communities

### Community Validation Process

#### Internal Testing
- Diverse internal team review
- Bias checklist completion by multiple reviewers
- Documentation of concerns and revisions requested

#### External Validation
- Partner with cultural consultants (paid, not free labor)
- Test with community members from depicted culture
- Anonymous feedback collection for honest responses
- Iteration based on feedback before final approval

#### Validation Questions
- "Do the people in this image look authentic to you?"
- "Are there any elements that feel stereotypical or inaccurate?"
- "Would you be comfortable seeing your community represented this way?"
- "What's missing or what feels wrong about this depiction?"

## Ethical AI Governance

### Enterprise Guidelines

#### Representation Policy
- Mandatory review for content featuring:
  - Specific ethnic or cultural groups
  - Religious practices or ceremonies
  - People with disabilities
  - Minors or vulnerable populations
  - Historical or culturally significant contexts

#### Prompt Standards
- Template-based prompting for sensitive content
- Required negative constraints for all human representations
- Documentation of cultural consultants engaged
- Revision history with community feedback tracked

#### Quality Gates
- Review checkpoint before publishing sensitive content
- Multi-reviewer validation for high-risk assets
- Escalation process for potential harm incidents
- Post-publication monitoring and feedback collection

### Training & Education

#### Team Training Topics
- Intersectionality 101: Understanding multiple identity dimensions
- Cultural humility: Continual learning, not expertise claiming
- Model bias patterns: How different AI models fail at diversity
- Inclusive design review: How to give feedback on representation
- Community engagement: Ethical consultation practices

#### Resource Library
- Cultural reference guides and image libraries
- Model bias documentation per platform
- Successful prompt templates by use case
- Case studies of representation failures and successes

## Continuous Improvement

### Bias Pattern Tracking

Create and maintain a database of:
- **Model-specific biases**: Midjourney's "sameness" problem, DALL-E's inaccuracies
- **Platform limitations**: What each tool cannot do well yet
- **Successful countermeasures**: Prompts that worked and why
- **Community feedback**: Validated authentic vs. problematic representations

### Research & Development

- **New Models**: Test emerging models for bias evolution
- **New Techniques**: Experiment with LoRAs, embeddings, control nets
- **Academic Research**: Follow papers on AI bias and mitigation
- **Industry Standards**: Participate in ethics working groups
- **Tool Development**: Build custom validation tools and checklists

## Tools & Resources

### Validation Tools
- **Image comparison tools**: Side-by-side review with reference images
- **Annotation tools**: Mark specific areas of concern on assets
- **Color contrast checkers**: Verify accessibility in generated imagery
- **Reverse image search**: Check for unexpected source material copying

### Reference Libraries
- **Fashion**: Accurate clothing references by culture and era
- **Architecture**: Geographic building styles and materials
- **Hairstyles**: Culturally-specific hair textures and styles
- **Cultural Practices**: Authentic depictions of ceremonies, daily life
- **Disability Aids**: Accurate mobility aids, assistive technology

### Community Networks
- Cultural consultants database with expertise areas
- Disability advocacy organizations for review
- Academic researchers studying representation
- Professional cultural competency trainers