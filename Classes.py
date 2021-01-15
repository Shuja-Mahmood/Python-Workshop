# Classes

PI = 3.141592

class Vector:
    
    # initializer
    # called after object creation
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    # public function
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    # public function with parameter
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
    
    # operator overloading for =
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    
    # operator overloading for >
    def __gt__(self, other):
        return (self.magnitude() > other.magnitude())
    
    # operator overloading for <
    def __lt__(self, other):
        return (self.magnitude() < other.magnitude())
    
    # operator overloading for multiplication from left side
    def __mul__(self, other):
        
        # If integer or float
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        
        else:
            raise TypeError
    
    # operator overloading for multiplication from left side
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        
        else:
            raise TypeError
    
    # convert to string so we can easily use print function
    def __str__(self):
        return "{0}, {1}, {2}".format(self.x, self.y, self.z)

class Object:
    
    # Initializer
    def __init__(self, position=Vector(), rotation=Vector(), scale=Vector(1, 1, 1)):
        # Private variables
        self.__position = position
        self.__rotation = rotation
        self.__scale = scale

    # Getters
    def get_position(self):
        return self.__position
    
    def get_rotation(self):
        return self.__rotation
    
    def get_scale(self):
        return self.__scale
    
    # Setters
    def set_position(self, new_position):
        if isinstance(new_position, Vector):
            self.__position = new_position
        else:
            raise TypeError
    
    def set_rotation(self, new_rotation):
        if isinstance(new_rotation, Vector):
            self.__rotation = new_rotation
        else:
            raise TypeError
        
    def set_scale(self, new_scale):
        if isinstance(new_scale, Vector):
            self.__scale = new_scale
        else:
            raise TypeError


class Material:
    
    # Initializer
    def __init__(self, color=Vector(), reflection=0):
        self.__color = color
        
        if reflection > 1:
            self.__reflection = 1
        elif reflection < 0:
            self.__reflection = 0
        else:
            self.__reflection = reflection

    # Getters
    def get_color(self):
        return self.__color
    def get_reflection(self):
        return self.__reflection

    # Setters
    def set_color(self, new_color):
        if isinstance(new_color, Vector):
            self.__color = new_color
        else:
            raise TypeError
        
    def set_reflection(self, new_reflection):
        if new_reflection > 1:
            self.__reflection = 1
        elif new_reflection < 1:
            self.__reflection = 0
        else:
            self.__reflection = new_reflection
    
# Multiple Inheritence
class Sphere(Object, Material):
    
    # Initilizer
    def __init__(self, position=Vector(), rotation=Vector(), scale=Vector(1,1,1), radius=1, color=Vector(), reflection=0):
        # Initialize the Parent class
        Object.__init__(self, position, rotation, scale)
        Material.__init__(self, color, reflection)
        
        # Private variable
        self.__radius = radius
    
    # Getter
    def get_radius(self):
        return self.__radius

    # Setter
    def set_radius(self, new_radius):
        if isinstance(new_radius, (int, float)):
            self.__radius = new_radius

    # Funtion
    def volume(self):
        return 4/3 * PI * self.__radius ** 3

    # Function
    def surface_area(self):
        return 4 * PI * self.__radius ** 2

s = Sphere()

s.set_position(Vector(2, 5, 80))
s.set_reflection(2.3)
print(s.get_position(), s.volume(), s.get_reflection())

# u = Vector(2,2,3)
# v = Vector(2,1,3)
# w = Vector(2,1,3)

# print(u * v)
# print(v * u)
# print(u * -1)
# print(2.5 * u)
