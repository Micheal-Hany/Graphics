# SVG to Turtle Drawing with Fancy Effects

This project parses an SVG file to extract geometric shapes, normalizes their coordinates, and then uses Python's `turtle` graphics module to draw them with fancy effects. The project is aimed at visualizing SVG data in a more natural and artistic way using turtle graphics.

## Features

- **SVG Parsing**: Extracts sub-geometric shapes (polygons, paths) from an SVG file.
- **Coordinate Normalization**: Normalizes extracted coordinates to fit within a specified canvas size.
- **Randomized Effects**: Adds random colors and varying pen sizes for each shape to create a more artistic visualization.
- **Smooth Animation**: Implements smooth drawing with gradual transitions between points for a dynamic experience.
- **Fancy Filling**: Uses Turtle's fill function to fill shapes with random colors.

## Requirements

- Python 3.x
- Required Libraries:
  - `svg.path`: For parsing SVG paths and extracting the shape coordinates.
  - `turtle`: For drawing the shapes on the screen.
  - `xml.etree.ElementTree`: For parsing the SVG XML structure.
  - `random`: For generating random colors and pen sizes.

To install the required libraries, use the following commands:

```bash
pip install svg.path
