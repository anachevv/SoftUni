pen_package = 5.8
marker_package = 7.2
detergent_liter = 1.2
pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())
price = (pens * pen_package) + (markers * marker_package) + (detergent * detergent_liter)
total = price - (price * (discount / 100))
print(total)
