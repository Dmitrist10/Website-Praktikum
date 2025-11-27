# DarkSecret Design System Guide

This guide documents the CSS classes and components available in the new design system.

## Themes

The design system supports three themes, applied via the `data-theme` attribute on the `<body>` tag:

- **Core** (`data-theme="core"`): Light, clean, minimalist. Used for the main company pages.
- **Gaming** (`data-theme="gaming"`): Dark, neon pink accents, glassmorphism. Used for VoxelGames.
- **Engine** (`data-theme="engine"`): Dark, neon blue accents, technical feel. Used for VoxelEngine.

## Layout

### Container
Centers content with a max-width of 1200px.
```html
<div class="container">
    <!-- Content -->
</div>
```

### Grid
Responsive grid system.
```html
<div class="grid grid-2"> <!-- 2 columns on desktop -->
    <div>Item 1</div>
    <div>Item 2</div>
</div>

<div class="grid grid-3"> <!-- 3 columns on desktop -->
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

### Flex Utilities
```html
<div class="flex justify-between items-center gap-md">
    <!-- Flex content -->
</div>
```
- `.flex`: `display: flex`
- `.flex-col`: `flex-direction: column`
- `.justify-between`: `justify-content: space-between`
- `.justify-center`: `justify-content: center`
- `.items-center`: `align-items: center`
- `.gap-sm`, `.gap-md`: Spacing gaps.

### Section
Adds standard vertical padding.
```html
<section class="section">
    <!-- Section content -->
</section>
```

## Components

### Buttons
```html
<a href="#" class="btn btn-primary">Primary Action</a>
<a href="#" class="btn btn-secondary">Secondary Action</a>
<a href="#" class="btn btn-outline">Outline Action</a>
```

### Cards
Cards automatically adapt to the theme (solid on Core, glassmorphism on Gaming/Engine).
```html
<div class="card">
    <h3>Card Title</h3>
    <p>Card content goes here.</p>
</div>
```

### Badges
Small labels for categories or status.
```html
<span class="badge">NEW</span>
```

### Hero Section
Standard hero layout.
```html
<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">Big Title</h1>
            <p class="hero-subtitle">Subtitle text.</p>
            <div class="flex gap-md">
                <a href="#" class="btn btn-primary">Action</a>
            </div>
        </div>
    </div>
</section>
```

## Typography

- **Headings**: Use `<h1>` to `<h6>`. They use the 'Outfit' font.
- **Body**: Uses 'Inter'.
- **Text Utilities**:
    - `.text-center`, `.text-left`, `.text-right`
    - `.text-muted`: Lighter text color.

## Forms

```html
<div class="form-group">
    <label>Email</label>
    <input type="email" class="input" placeholder="you@example.com">
</div>
```
