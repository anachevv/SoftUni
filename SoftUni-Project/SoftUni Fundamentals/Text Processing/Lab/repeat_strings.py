sequence_of_strings = input().split()
final_string = ""

for string in sequence_of_strings:
    n_times = len(string)
    final_string += (string * n_times)

print(final_string)
