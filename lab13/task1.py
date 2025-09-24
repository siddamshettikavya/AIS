from math import pi


def _area_rectangle(length, width):
    return length * width


def _area_square(side):
    return side * side


def _area_circle(radius):
    return pi * radius * radius


def calculate_area(shape, *args):
    shape_name = shape.lower() if isinstance(shape, str) else ""

    required_arg_counts = {
        "rectangle": 2,
        "square": 1,
        "circle": 1,
    }

    calculators = {
        "rectangle": lambda: _area_rectangle(*args),
        "square": lambda: _area_square(*args),
        "circle": lambda: _area_circle(*args),
    }

    if shape_name not in required_arg_counts:
        return "Unknown shape"

    expected = required_arg_counts[shape_name]
    if len(args) != expected:
        if shape_name == "rectangle":
            return "Rectangle requires 2 arguments (length, width)"
        if shape_name == "square":
            return "Square requires 1 argument (side length)"
        if shape_name == "circle":
            return "Circle requires 1 argument (radius)"

    return calculators[shape_name]()


if __name__ == "__main__":
    print("Area of rectangle (5, 10):", calculate_area("rectangle", 5, 10))
    print("Area of square (4):", calculate_area("square", 4))
    print("Area of circle (3):", calculate_area("circle", 3))
    print("Area of unknown shape:", calculate_area("triangle", 5, 10))      