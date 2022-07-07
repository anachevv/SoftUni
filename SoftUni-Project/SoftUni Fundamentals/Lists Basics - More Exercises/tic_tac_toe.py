first_line = input().split()
second_line = input().split()
third_line = input().split()

lst = [[int(i) for i in first_line], [int(x) for x in second_line], [int(y) for y in third_line]]

"""

[   [2, 0, 1], 
     [0, 1, 0], 
     [1, 0, 2]
]

2 0 1
0 1 0
1 0 2

"""

first_player_rows = (lst[0] == [1, 1, 1] or lst[1] == [1, 1, 1] or lst[2] == [1, 1, 1])
first_player_columns = ((lst[0][0] == lst[1][0] == lst[2][0] == 1) or (lst[0][1] == lst[1][1] == lst[2][1] == 1) or
                        (lst[0][2] == lst[1][2] == lst[2][2] == 1))
first_player_diagonals = ((lst[0][0] == lst[1][1] == lst[2][2] == 1) or lst[0][2] == lst[1][1] == lst[2][0] == 1)

first_player_win = first_player_rows or first_player_columns or first_player_diagonals

second_player_rows = (lst[0] == [2, 2, 2] or lst[1] == [2, 2, 2] or lst[2] == [2, 2, 2])
second_player_columns = ((lst[0][0] == lst[1][0] == lst[2][0] == 2) or (lst[0][1] == lst[1][1] == lst[2][1] == 2)
                         or (lst[0][2] == lst[1][2] == lst[2][2] == 2))
second_player_diagonals = ((lst[0][0] == lst[1][1] == lst[2][2] == 2) or lst[0][2] == lst[1][1] == lst[2][0] == 2)

second_player_win = second_player_rows or second_player_columns or second_player_diagonals

if first_player_win:
    print('First player won')
elif second_player_win:
    print('Second player won')
else:
    print('Draw!')


# Using a function


# def tic_tac_toe(first, second, third):
#     lst = [[int(i) for i in first], [int(x) for x in second], [int(y) for y in third]]
#
#     """
#
#     [   [2, 0, 1],
#          [0, 1, 0],
#          [1, 0, 2]
#     ]
#
#     2 0 1
#     0 1 0
#     1 0 2
#
#     """
#
#     first_player_rows = (lst[0] == [1, 1, 1] or lst[1] == [1, 1, 1] or lst[2] == [1, 1, 1])
#     first_player_columns = ((lst[0][0] == lst[1][0] == lst[2][0] == 1) or (lst[0][1] == lst[1][1] == lst[2][1] == 1) or
#                             (lst[0][2] == lst[1][2] == lst[2][2] == 1))
#     first_player_diagonals = ((lst[0][0] == lst[1][1] == lst[2][2] == 1) or lst[0][2] == lst[1][1] == lst[2][0] == 1)
#
#     first_player_win = first_player_rows or first_player_columns or first_player_diagonals
#
#     second_player_rows = (lst[0] == [2, 2, 2] or lst[1] == [2, 2, 2] or lst[2] == [2, 2, 2])
#     second_player_columns = ((lst[0][0] == lst[1][0] == lst[2][0] == 2) or (lst[0][1] == lst[1][1] == lst[2][1] == 2)
#                              or (lst[0][2] == lst[1][2] == lst[2][2] == 2))
#     second_player_diagonals = ((lst[0][0] == lst[1][1] == lst[2][2] == 2) or lst[0][2] == lst[1][1] == lst[2][0] == 2)
#
#     second_player_win = second_player_rows or second_player_columns or second_player_diagonals
#
#     if first_player_win:
#         return 'First player won'
#     elif second_player_win:
#         return 'Second player won'
#     return 'Draw!'
#
#
# first_line = input().split()
# second_line = input().split()
# third_line = input().split()
#
# print(tic_tac_toe(first_line, second_line, third_line))
