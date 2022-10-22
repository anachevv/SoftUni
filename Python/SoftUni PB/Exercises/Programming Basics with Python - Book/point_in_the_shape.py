h = int(input())
x = int(input())
y = int(input())

outside = (x < 0 or y < 0 or x > h * 3 or y > h * 4 or
           (x < h < y <= h * 4) or (x > h * 2 and h < y <= h * 4))
border = ((0 <= x <= h * 3 and y == 0)
          or (0 <= y <= h and x == 0)
          or (y == h and 0 <= x <= h)
          or (x == h and h <= y <= h * 4)
          or (y == h * 4 and h <= x <= h * 2)
          or (x == h * 2 and h <= y <= h * 4) or
          (y == h and h * 2 <= x <= h * 3) or (x == h * 3 and 0 <= y <= h))


if border:
    print("border")
elif outside:
    print("outside")
else:
    print("inside")