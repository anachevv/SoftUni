juniors = int(input())
seniors = int(input())
route = input()
juniors_price = 0
seniors_price = 0

if route == "trail":
    juniors_price = 5.5 * juniors
    seniors_price = 7 * seniors
elif route == "cross-country":
    juniors_price = 8 * juniors
    seniors_price = 9.5 * seniors
elif route == "downhill":
    juniors_price = 12.25 * juniors
    seniors_price = 13.75 * seniors
elif route == "road":
    juniors_price = 20 * juniors
    seniors_price = 21.5 * seniors

if juniors + seniors >= 50 and route == "cross-country":
    juniors_price *= 0.75
    seniors_price *= 0.75

total_price = (juniors_price + seniors_price) * 0.95

print(f"{total_price:.2f}")
