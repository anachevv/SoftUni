visitors = int(input())
visitors_training_back = 0
visitors_training_chest = 0
visitors_training_legs = 0
visitors_training_abs = 0

visitors_buying_protein_shake = 0
visitors_buying_protein_bar = 0

for x in range(visitors):
    activity = input()

    if activity == "Back":
        visitors_training_back += 1
    elif activity == "Chest":
        visitors_training_chest += 1
    elif activity == "Legs":
        visitors_training_legs += 1
    elif activity == "Abs":
        visitors_training_abs += 1
    elif activity == "Protein shake":
        visitors_buying_protein_shake += 1
    elif activity == "Protein bar":
        visitors_buying_protein_bar += 1

total_visitors_training = visitors_training_back + visitors_training_chest + visitors_training_legs + \
                          visitors_training_abs
total_visitors_protein = visitors_buying_protein_shake + visitors_buying_protein_bar
print(f"{visitors_training_back} - back")
print(f"{visitors_training_chest} - chest")
print(f"{visitors_training_legs} - legs")
print(f"{visitors_training_abs} - abs")
print(f"{visitors_buying_protein_shake} - protein shake")
print(f"{visitors_buying_protein_bar} - protein bar")
print(f"{total_visitors_training / (total_visitors_training + total_visitors_protein) * 100:.2f}% - work out")
print(f"{total_visitors_protein / (total_visitors_training + total_visitors_protein) * 100:.2f}% - protein")
