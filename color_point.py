from point import Point  # import the Point class from another file
import random

class PointException(Exception):  # custom exception if needed later
    pass

class ColorPoint(Point):  # inherits from Point and adds a color
    def __init__(self, x, y, color):
        """
        Create a colored point with x, y coordinates
        and a color label
        :param x: horizontal position (must be number)
        :param y: vertical position (must be number)
        :param color: string that represents the color
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")  # make sure x is numeric
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an number")  # make sure y is numeric

        super().__init__(x, y)  # call parent constructor
        self.color = color  # add color attribute

    def __str__(self):
        """
        Called when you print the object
        :return: string like <color: x, y>
        """
        return f"<{self.color}: {self.x}, {self.y}>"

#p = ColorPoint(1, 2, "red")
#print(p)
#colors = ["red", "green", "blue", "yellow", "black", "magenta"]

#color_point = []
#for i in range(10):
#    color_point.append(
#        ColorPoint(random.randint(-10, 10),
#                   random.randint(-10, 10),
#                   random.choice(colors)))

#print(color_point)
#color_point.sort()
#print(color_point)

if __name__ =="__main__":  # only runs if this file is executed directly
    p = ColorPoint(1, 2, "red")  # create a colored point
    print(p.distance_origin())  # call method from parent class
    print(p)  # show string representation
