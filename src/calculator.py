import math
from models import CircleInput, ShapeProperties

def calculate_properties(data: CircleInput, center: dict) -> ShapeProperties:
    """
    Calculates the area and perimeter of a circle.

    Args:
        data: A CircleInput object containing the radius.
        center: A dict containing the x,y coordinates of the center.

    Returns:
        A ShapeProperties object with the calculated area and perimeter.
    """
    area = math.pi * (data.radius ** 2)
    perimeter = 2 * math.pi * data.radius

    return ShapeProperties(
        area=round(area, 2),
        perimeter=round(perimeter, 2),
        center=center
    )