---
updated: 2026-03-20 | 22:03
created: 2026-03-20 | 22:03
---
# TOOLS.md -- UI Designer

## Core Skills

- `para-memory-files` - Memory operations and design system management
- `design-systems` - Component libraries, design tokens, pattern catalogs
- `visual-design-principles` - Typography, color theory, composition
- `responsive-design-frameworks` - Mobile-first, breakpoints, fluid layouts
- `accessibility-compliance` - WCAG 2.1 AA, color contrast, focus management

## Design Tools

### UI/UX Design
- **Figma**: Component systems, auto-layout, design tokens, prototyping
- **Sketch**: Symbols, libraries, mirror, prototyping
- **Adobe XD**: Components, repeat grids, voice prototyping
- **Penpot**: Open-source alternative, vector design, prototyping

### Design System Management
- **Storybook**: Component documentation, interactive examples
- **Zeroheight**: Design system documentation, style guides
- **Supernova**: Documentation, developer handoff, versioning
- **Abstract**: Version control for design files

### Prototyping
- **Figma Prototyping**: Interactive flows, micro-interactions, animations
- **Principle**: Advanced animations, micro-interactions, scroll effects
- **Framer**: React-based prototyping, code components, advanced interactions
- **Protopie**: High-fidelity interactions, conditional logic, sensors

### Color & Typography
- **Coolors**: Color palette generation, contrast checking
- **Colorable**: Color contrast ratio testing
- **Google Fonts**: Web font selection and testing
- **Font Pair**: Typography pairing recommendations

## Component Design Patterns

### Base Components
- **Buttons**: Primary, secondary, tertiary variants; sizes; icon buttons
- **Form Elements**: Inputs, selects, checkboxes, radios, textareas
- **Feedback**: Alerts, toasts, modals, tooltips, popovers
- **Navigation**: Menus, breadcrumbs, pagination, tabs
- **Data Display**: Cards, tables, lists, badges, avatars

### Composite Components
- **Headers**: Navigation, search, user menu, theme toggle
- **Cards**: Content containers with media, actions, metadata
- **Forms**: Grouped inputs with validation and submission
- **Lists**: Item groups, virtualized lists, infinite scroll
- **Modals**: Dialogs with overlays, actions, close behaviors

### Interactive States
- **Default**: Initial state, ready for interaction
- **Hover**: Pointer over element, visual indication
- **Focus**: Keyboard navigation, visible focus ring
- **Active/Selected**: Current selection, pressed state
- **Disabled**: Non-interactive, reduced opacity
- **Loading**: Spinners, skeleton loaders, progress indicators
- **Error**: Validation failures, error states with guidance

## Design Token Systems

### Token Categories
- **Colors**: Semantic (primary, secondary, success, warning, error) + neutral scale
- **Typography**: Font families, sizes, weights, line heights, letter spacing
- **Spacing**: Scale (4px base), margin/padding tokens, gap tokens
- **Shadows**: Elevation levels, softness, spread, color
- **Border**: Widths, radii, styles, colors
- **Transition**: Durations, easing functions, delay values
- **Z-Index**: Layering order for overlapping elements

### Token Naming Conventions
- **Semantic**: `color-primary-500`, `spacing-md`, `shadow-lg`
- **Component-scoped**: `btn-primary-bg`, `input-border-color`
- **Utility**: `text-center`, `flex`, `grid` (utility-first approach)

## Accessibility Implementation

### Color Contrast
- **Normal Text**: 4.5:1 minimum ratio (AA level)
- **Large Text**: 3:1 minimum ratio (AA level)
- **Graphics/UI**: 3:1 minimum ratio for interactive elements
- **Testing Tools**: Contrast checker, Colorable, Stark plugin

### Focus Management
- **Focus Indicators**: Visible outline or ring on all interactive elements
- **Focus Order**: Logical sequential navigation (DOM order)
- **Skip Links**: Skip to main content, skip navigation
- **Focus Trap**: Modals and dialogs trap focus within

### Screen Reader Support
- **Semantic HTML**: Proper element usage (button, nav, main)
- **ARIA Labels**: Descriptive names for interactive elements
- **Live Regions**: Dynamic content announcements
- **Alt Text**: Descriptive alternatives for images
- **Headings**: Proper hierarchy (h1 → h2 → h3)

### Motion & Animation
- **Reduced Motion**: Respect `prefers-reduced-motion` setting
- **Duration**: Keep animations under 300ms for interactions
- **Purpose**: Only animate for meaningful feedback or transitions
- **Non-Flashing**: Avoid rapid flashes (>3 per second)

## Responsive Design Strategy

### Breakpoint Strategy
- **Mobile**: 320px - 639px (base, mobile-first)
- **Tablet (Small)**: 640px - 767px
- **Tablet (Medium)**: 768px - 1023px
- **Desktop**: 1024px - 1279px
- **Large Desktop**: 1280px+

### Layout Adaptation
- **Grid Systems**: 1-column mobile → 2-4 columns desktop
- **Navigation**: Hamburger menu → full navigation bar
- **Cards**: Single column → multi-column grid layouts
- **Forms**: Stacked → inline layouts for larger screens
- **Touch Targets**: Increase size for mobile (minimum 44×44px)

### Fluid Typography
- **Clamp Function**: `font-size: clamp(1rem, 2.5vw, 1.5rem)`
- **Fluid Spacing**: Scale spacing with viewport width
- **Container Queries**: Adapt components to container size (modern browsers)

## Design Handoff Best Practices

### Annotations
- **Measurements**: Exact pixel values for spacing, sizing
- **Colors**: Hex/RGB/HSL with contrast ratios noted
- **Typography**: Font family, weight, size, line-height, letter-spacing
- **States**: All hover, active, focus, disabled variations shown
- **Responsive**: Behavior at each breakpoint with breakpoint markers
- **Interaction**: Notes on animations, transitions, timing functions

### Asset Exports
- **Icons**: SVG format preferred, multiple sizes (16, 24, 32, 48px)
- **Images**: Optimized PNG/JPEG with appropriate compression
- **Logos**: SVG for scalability, PNG fallbacks
- **Export Naming**: Clear, descriptive names with size/variant indicators

### Developer Support
- **Component API**: Props/attributes documentation with examples
- **Usage Examples**: Code snippets demonstrating implementation
- **Variants**: All component variations documented
- **Accessibility**: ARIA attributes, keyboard interactions, screen reader notes

## Design Quality Checklist

### Before Handoff
- [ ] All interactive states designed (default, hover, active, focus, disabled)
- [ ] Responsive behavior defined at all breakpoints
- [ ] Accessibility verified (contrast ratios, focus states, semantic structure)
- [ ] Design tokens used consistently throughout
- [ ] Brand compliance confirmed
- [ ] Developer annotations complete with measurements
- [ ] Assets exported in appropriate formats
- [ ] Interactions and animations documented with timing
- [ ] Edge cases considered (error states, empty states, loading)
- [ ] Cross-browser visual consistency planned

### Component Documentation Template
```markdown
## [Component Name]

### Overview
Brief description of component purpose and usage.

### Variants
- **Default**: Primary usage pattern
- **Secondary**: Alternative style or purpose
- **[Other]**: Specialized variations

### States
- Default: [visual description]
- Hover: [visual description]
- Active/Pressed: [visual description]
- Focus: [visual description]
- Disabled: [visual description]
- Error: [visual description]
- Loading: [visual description]

### Anatomy
[Labeled diagram showing component parts]

### Spacing
[Spacing specifications with tokens]

### Color
[Color values for each state and element]

### Typography
[Text styles used in component]

### Responsive Behavior
[Mobile → tablet → desktop changes]

### Accessibility
- Keyboard interactions: [tab order, shortcuts]
- Screen reader: [ARIA labels, live regions]
- Focus management: [focus trap, restoration]
- Color contrast: [ratios for each state]

### Code Examples
```html
<!-- Example usage -->
<button class="btn btn-primary">Click me</button>
```
```