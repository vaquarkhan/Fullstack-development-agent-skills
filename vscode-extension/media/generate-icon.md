# Generate icon.png

The VS Code Marketplace requires a PNG icon (128x128 minimum).

## Option 1: Convert SVG to PNG online
1. Open `icon.svg` in a browser
2. Use https://svgtopng.com/ or https://cloudconvert.com/svg-to-png
3. Save as `icon.png` (128x128 or 256x256)

## Option 2: Use ImageMagick
```bash
magick convert icon.svg -resize 128x128 icon.png
```

## Option 3: Use Inkscape
```bash
inkscape icon.svg --export-type=png --export-filename=icon.png -w 128 -h 128
```
