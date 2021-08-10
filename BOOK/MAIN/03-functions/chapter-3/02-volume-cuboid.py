#calculate volume of a box with appropriate default values for its parameters.
#function should have the following input parameters:
#(a) length of box 
#(b) width of box 
#(c) height of box.


def volumeOfCuboid(length=1,breadth=1,height=1):
    volume = length * breadth * height

    return volume

#__main__
print("Volume with default values of length breadth and height: ")
print(volumeOfCuboid())

length = float(input("Enter the length of cuboid: "))
breadth = float(input("Enter the breadth of cuboid: "))
height= float(input("Enter the height of cuboid: "))

print("Volume with provided values of length, breadth and height: ")

print(volumeOfCuboid(length,breadth,height))