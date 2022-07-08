n_snowballs = int(input())
the_highest_value = 0
top_weight = 0
top_hit_time = 0
top_quality = 0

for snowball in range(n_snowballs):
    weight = int(input())
    hit_time = int(input())
    quality = int(input())

    formula = (weight / hit_time) ** quality

    if formula > the_highest_value:
        the_highest_value = formula
        top_weight = weight
        top_hit_time = hit_time
        top_quality = quality

print(f"{top_weight} : {top_hit_time} = {int(the_highest_value)} ({top_quality})")
