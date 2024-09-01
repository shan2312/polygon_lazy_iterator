## Overview

This project provides a Python implementation of a `Polygon` class and a `Polygons` iterable class. The `Polygon` class represents a regular polygon with a specified number of vertices and a circumradius, while the `Polygons` class generates a sequence of polygons starting from a triangle (3 sides) up to a polygon with a specified maximum number of sides. The `PolygonsIterator` class is also included to enable iteration over the sequence of polygons.

## Classes

### 1. Polygon

The `Polygon` class represents a regular polygon characterized by:
- `n`: Number of vertices (or edges).
- `R`: Circumradius, which is the radius of the circumscribing circle.

#### Properties

- `count_vertices`: Returns the number of vertices of the polygon.
- `count_edges`: Returns the number of edges, which is equal to the number of vertices.
- `circumradius`: Returns the circumradius of the polygon.
- `interior_angle`: Calculates and returns the interior angle of the polygon.
- `side_length`: Calculates and returns the length of each side of the polygon.
- `apothem`: Calculates and returns the apothem, which is the distance from the center to the midpoint of a side.
- `area`: Calculates and returns the area of the polygon.
- `perimeter`: Calculates and returns the perimeter of the polygon.

#### Methods

- `__eq__(self, other)`: Checks if two polygons are equal based on the number of edges and circumradius.
- `__gt__(self, other)`: Compares two polygons based on the number of vertices.

### 2. PolygonsIterator

The `PolygonsIterator` class is an iterator that generates a sequence of polygons, starting from a triangle (3 sides) up to a polygon with a specified maximum number of sides.

#### Methods

- `__iter__(self)`: Returns the iterator object.
- `__next__(self)`: Returns the next polygon in the sequence. Raises `StopIteration` when the end of the sequence is reached.

### 3. Polygons

The `Polygons` class represents a sequence of polygons, starting from a triangle (3 sides) up to a polygon with `m` sides.

#### Properties

- `max_efficiency_polygon`: Returns the polygon with the maximum area-to-perimeter ratio from the sequence.

#### Methods

- `__iter__(self)`: Returns an iterator for the sequence of polygons.

## Usage

### Example

```python
# Create a polygon with 5 vertices and a circumradius of 10
polygon = Polygon(5, 10)
print(polygon.interior_angle)  # Output: 108.0
print(polygon.area)  # Output: area of the polygon
print(polygon.perimeter)  # Output: perimeter of the polygon

# Create a sequence of polygons from triangle to 6-sided polygon
polygons = Polygons(6, 10)
for p in polygons:
    print(p)

# Find the polygon with the maximum efficiency (area/perimeter ratio)
max_efficiency_polygon = polygons.max_efficiency_polygon
print(max_efficiency_polygon)
```

## Installation

No special installation is required for this code. Simply include the provided Python code in your project and import the necessary classes.

## Requirements

- Python 3.x

## Author

This code was written by Sachin Sharma. Feel free to reach out for any questions or collaboration opportunities.

