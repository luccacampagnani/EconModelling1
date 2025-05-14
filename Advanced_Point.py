from color_point import ColorPoint, PointException  # importing base class and custom exception

class AdvancedPoint(ColorPoint):  # basic placeholder for extending ColorPoint
    pass

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "green", "blue", "yellow", "black", "magenta"]  # allowed colors

    def __init__(self, x, y, color):  # fixed typo: __int__ → __init__
        """
        Create an AdvancedPoint with x, y coordinates and a valid color
        :param x: horizontal coordinate
        :param y: vertical coordinate
        :param color: must be in allowed COLORS
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Get the x value of the point
        :return: x coordinate
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Set a new x value for the point
        :param value: new x coordinate
        """
        self._x = value

    @property
    def y(self):
        """
        Get the y value of the point
        :return: y coordinate
        """
        return self._y

    @property
    def color(self):
        """
        Get the color of the point
        :return: color as string
        """
        return self._color

    @classmethod
    def add_colors(cls, color):
        """
        Add a new color to the allowed COLORS list
        :param color: new color to add
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create a new AdvancedPoint from a (x, y) tuple
        :param coordinate: tuple with (x, y) values
        :param color: optional color (default is "red")
        :return: AdvancedPoint object
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate the distance between two points
        :param p1: first point
        :param p2: second point
        :return: distance as float
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculate the distance from this point to another point
        :param p: other point
        :return: distance as float
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Add a new color to the allowed list
AdvancedPoint.add_colors("rojo")

# Create a new point with the new color
p = AdvancedPoint(1, 2, "rojo")
print(p.x)  # print x value
print(p)  # print point using __str__
print(p.distance_origin())  # print distance from origin

# Create a new point using a tuple
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
# Calculate and print distance between p and p2 using class method
print(AdvancedPoint.distance_2_points(p, p2))
# Calculate and print distance using instance method
print(p.distance_to_other(p2))
