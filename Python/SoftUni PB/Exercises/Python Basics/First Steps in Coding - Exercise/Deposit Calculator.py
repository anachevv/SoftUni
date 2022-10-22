deposit = float(input())
deposit_deadline = int(input())
annual_interest = float(input()) / 100
total = deposit + deposit_deadline * ((deposit * annual_interest) / 12)
print(total)