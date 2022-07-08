vowels = ['a', 'o', 'u', 'e', 'i']
new_text = ''.join(c for c in input() if not c.lower() in vowels)
print(new_text)
