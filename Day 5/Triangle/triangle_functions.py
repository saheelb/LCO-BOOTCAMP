
def trinagle_perimeter(side1, side2, side3):
    return (side1 + side2 + side3)

def triangle_area(side1, side2, side3):
    p = trinagle_perimeter(side1,side2, side3)/2
    area = (p * (p-side1)* (p-side2)* (p-side3)) ** 0.5
    return area


def measure(side1, side2, side3, operation="A"):
    if operation.upper() == "A":
        return round(triangle_area(side1, side2, side3), 2)
    elif operation.upper() == "P":
        return trinagle_perimeter(side1,side2, side3)
    else:
        print("Invalid Operation!")

