def even_odd(*args):
   command = args[-1]
   result = []
   if command == 'even':
       result = [x for x in args[0:-1] if x % 2 == 0]
   else:
       result = [y for y in args[0:-1] if y % 2 != 0]

   return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
