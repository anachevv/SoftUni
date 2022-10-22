def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    def area():
        return f"Rectangle area: {length * width}"
    def perimeter():
        return f"Rectangle perimeter: {2 * (length + width)}"
    
    return area() + '\n' + perimeter()

print(rectangle(2,10))
