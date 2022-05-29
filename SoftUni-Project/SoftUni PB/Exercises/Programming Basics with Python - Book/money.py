bitcoins = int(input())
yuans = float(input())
commission = float(input()) / 100

bitcoins_to_leva = bitcoins * 1168
yuans_to_dollars = yuans * 0.15
dollars_to_leva = yuans_to_dollars * 1.76
euro = ((bitcoins * 1168) + (yuans * 0.15 * 1.76)
        / 1.95 - (commission * (bitcoins * 1168)) +
        (yuans * 0.15 * 1.76) / 1.95)

print(round(euro, 2))
# Not done!
