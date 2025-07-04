import random

class Point: # You have to use capital letter for it to be a class
    def __init__(self, x, y): # you can change the name of self to whatever u want
        """
        Create a point with x and y coordinates
        :param x: horizontal position
        :param y: vertical position
        """
        self.x = x # define x attribute via self.x and the assign the value of x to it
        self.y = y

    def __str__(self):
        """
        Called when you print the object
        :return: string like <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #use same way of printing as str

    def distance_origin(self):
        """
        Calculate how far the point is from (0, 0)
        :return: distance value
        """
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x

    def __gt__(self, other):
        """
        Compare two points by their distance from the origin
        :param other: another Point object
        :return: True if self is farther than other
        """
        my_distance = self.distance_origin()
        other_distance = other.distance_origin()
        return my_distance > other_distance
# if __name__ == "__main__"



# now we need to instantiate it
p = Point(1, 2)  # p is an instance of 1 and 2
print(f"p.x={p.x} and p.y={p.y}")

p.x=29
print(f"p.x={p.x} and p.y={p.y}")
print(p)

#create a list of 5 random point
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), # x value
                        random.randint(-10, 10))) # y value

print("i got these 5 random points: ")
for p in points:
    print(p)


# the final porpuse is to sort the list of random points
print(points)

p= Point(3, 4)
print(p.distance_origin()) # expect 5 answer

p2 = Point(1, 1)
print(f"i am comparing p > p2: {p>p2}") # i expect to have true

print("the sorted list of points is: ")
points.sort()
print(points)
