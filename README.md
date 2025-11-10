# Unit Circle Animation with Manim

A comprehensive educational animation explaining the unit circle and how sine, cosine, and tangent relate to coordinates and ratios on the circle.

## Features

- **Interactive visualization** of the unit circle with axes and coordinate system
- **Animated point** moving through special angles (0°, 30°, 45°, 60°, 90°, etc.)
- **Right triangle formation** showing:
  - Radius (hypotenuse)
  - X-coordinate (adjacent/cosine)
  - Y-coordinate (opposite/sine)
- **Clear labels** for angles, coordinates, and exact values
- **Formula panel** showing key relationships:
  - x = cos(θ)
  - y = sin(θ)
  - tan(θ) = y/x
  - sin²(θ) + cos²(θ) = 1
- **Special angle emphasis** at 30°, 45°, 60°, 90° with exact values (√2/2, √3/2, etc.)
- **3Blue1Brown inspired** color scheme
- **Bonus visualization**: Sine and cosine waves building as the angle increases
- **All four quadrants** showing how values reflect and repeat

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Additional System Dependencies

Manim requires some system-level dependencies. Install them based on your OS:

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
```

#### macOS:
```bash
brew install cairo pango ffmpeg
```

#### Windows:
Follow the [Manim installation guide](https://docs.manim.community/en/stable/installation/windows.html) for Windows-specific instructions.

## Usage

### Render the Animation

To render the animation in 1080p at 60fps (as requested):

```bash
manim -pqh --fps 60 unit_circle.py UnitCircleExplanation
```

### Command Breakdown:
- `-p`: Preview the animation after rendering
- `-q h`: High quality (1080p)
- `--fps 60`: 60 frames per second for smooth rotation
- `unit_circle.py`: The Python file containing the animation
- `UnitCircleExplanation`: The scene class name

### Alternative Quality Options:

**Low quality (480p) - faster rendering for testing:**
```bash
manim -pql unit_circle.py UnitCircleExplanation
```

**Medium quality (720p):**
```bash
manim -pqm unit_circle.py UnitCircleExplanation
```

**4K quality:**
```bash
manim -pqk --fps 60 unit_circle.py UnitCircleExplanation
```

## Output

The rendered video will be saved in:
```
media/videos/unit_circle/1080p60/UnitCircleExplanation.mp4
```

## Animation Breakdown

### Part 1: Introduction (0-5s)
- Title card
- Axes and unit circle creation

### Part 2: Formula Panel (5-10s)
- Side panel with key formulas appears
- Formulas are explained

### Part 3: Angle Progression (10-40s)
- Point moves through special angles
- Right triangles form at each position
- Coordinates and labels update dynamically
- Special angles are emphasized with longer pauses
- All four quadrants are demonstrated

### Part 4: Wave Formation (40-50s)
- Sine and cosine waves build as point rotates
- Shows connection between circular motion and wave patterns

### Part 5: Conclusion (50-55s)
- Final message summarizing the concept

## Color Scheme

Following 3Blue1Brown's aesthetic:
- **Blue**: Unit circle
- **Yellow**: Highlighted elements (point, angle, emphasis)
- **Red**: Sine (y-coordinate)
- **Green**: Cosine (x-coordinate)
- **Orange**: Tangent values
- **Grey**: Axes and grid

## Educational Goals

This animation demonstrates:
1. **WHY** cosine is the x-coordinate (adjacent side of the triangle)
2. **WHY** sine is the y-coordinate (opposite side of the triangle)
3. **HOW** tangent relates to the ratio of y/x
4. **WHERE** the special angle values come from geometrically
5. **HOW** values repeat and reflect across different quadrants
6. The connection between circular motion and wave patterns

## Customization

You can modify the animation by editing `unit_circle.py`:
- Adjust `special_angles` list to show different angles
- Change colors in the color scheme section
- Modify timing by adjusting `run_time` and `wait()` parameters
- Add or remove sections as needed

## Troubleshooting

**Issue**: "No module named 'manim'"
- **Solution**: Run `pip install manim`

**Issue**: Animation runs too slowly
- **Solution**: Use lower quality settings with `-ql` or `-qm`

**Issue**: FFmpeg errors
- **Solution**: Make sure FFmpeg is properly installed and in your system PATH

**Issue**: LaTeX errors
- **Solution**: Install a LaTeX distribution (TeX Live on Linux, MacTeX on macOS, MiKTeX on Windows)

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Community Examples](https://docs.manim.community/en/stable/examples.html)
- [Unit Circle Reference](https://en.wikipedia.org/wiki/Unit_circle)

## License

MIT License - Feel free to use and modify for educational purposes!
