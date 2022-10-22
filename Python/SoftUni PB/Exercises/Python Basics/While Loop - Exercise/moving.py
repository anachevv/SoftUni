width = int(input())
length = int(input())
height = int(input())

max_boxes = width * length * height

boxes = input()

while boxes != "Done":

    if boxes == "Done":
        break

    elif boxes != "Done":
        max_boxes -= int(boxes)

    if max_boxes < 0:
        break

    boxes = input()

if boxes == "Done":
    print(f"{max_boxes} Cubic meters left.")
elif max_boxes < int(boxes):
    print(f"No more free space! You need {abs(max_boxes)} Cubic meters more.")
