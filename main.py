from svg.path import parse_path
import xml.etree.ElementTree as ET
import turtle
import random


def parse_svg_to_subshapes(file_path):
    """Parse the SVG file and extract sub-geometric shapes as independent objects."""
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {"svg": "http://www.w3.org/2000/svg"}
    sub_shapes = []

    polygons = root.findall(".//svg:polygon", namespace)
    for polygon in polygons:
        points = polygon.attrib.get("points", "")
        if points:
            coords = [tuple(map(float, p.split(","))) for p in points.split()]
            sub_shapes.append(coords)

    paths = root.findall(".//svg:path", namespace)
    for path in paths:
        d = path.attrib.get("d", "")
        if d:
            parsed_path = parse_path(d)
            coords = []
            for segment in parsed_path:
                coords.append((segment.start.real, segment.start.imag))
                coords.append((segment.end.real, segment.end.imag))

            coords = list(dict.fromkeys(coords))
            if len(coords) > 2:
                sub_shapes.append(coords)

    return sub_shapes


def normalize_coordinates(sub_shapes, canvas_width, canvas_height):
    """Normalize the coordinates to fit within the canvas."""
    all_coords = [coord for shape in sub_shapes for coord in shape]
    min_x = min(coord[0] for coord in all_coords)
    max_x = max(coord[0] for coord in all_coords)
    min_y = min(coord[1] for coord in all_coords)
    max_y = max(coord[1] for coord in all_coords)

    width = max_x - min_x
    height = max_y - min_y

    normalized_shapes = []
    for shape in sub_shapes:
        normalized_shape = [
            (
                (coord[0] - min_x) / width * canvas_width - canvas_width / 2,
                (coord[1] - min_y) / height *
                canvas_height - canvas_height / 2,
            )
            for coord in shape
        ]
        normalized_shapes.append(normalized_shape)

    return normalized_shapes


def generate_random_color():
    """Generate a random color in RGB format."""
    return (random.random(), random.random(), random.random())


def draw_shape_with_turtle(sub_shapes):
    """Draw the full shape by partitioning it into sub-shapes with fancy drawing effects."""
    if not sub_shapes:
        print("No sub-shapes found to draw.")
        return

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(3)
    t.width(2)
    t.hideturtle()

    for shape in sub_shapes:
        if not shape:
            continue

        color = "#FFFFFF"
        t.fillcolor(color)

        t.pensize(random.randint(1, 3))

        t.up()
        t.goto(shape[0][0], shape[0][1])
        t.down()

        t.begin_fill()

        for coord in shape[1:]:
            t.goto(coord[0], coord[1])

        t.goto(shape[0][0], shape[0][1])

        t.end_fill()

    turtle.done()


if __name__ == "__main__":
    svg_file = "shape.svg"

    try:

        sub_shapes = parse_svg_to_subshapes(svg_file)

        normalized_shapes = normalize_coordinates(sub_shapes, 600, 400)

        draw_shape_with_turtle(normalized_shapes)
    except Exception as e:
        print(f"An error occurred: {e}")
