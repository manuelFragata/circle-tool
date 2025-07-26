from dataclasses import dataclass, asdict

@dataclass
class CircleInput:
    """Input data contract for circle calculations."""
    radius: float

@dataclass
class ShapeProperties:
    """Output data contract for shape properties."""
    area: float
    perimeter: float
    # The actual center is calculated and managed by the frontend,
    # but we include it here to demonstrate passing complex data.
    center: dict[str, float]

    def to_json(self):
        """Converts the dataclass instance to a dictionary."""
        return asdict(self)