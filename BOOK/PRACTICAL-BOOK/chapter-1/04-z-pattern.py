
for row in range(0,9):
  for column in range(0,9):
    if row == 0 or row == 9-1 or row + column + 1 == 9:
       print('*',end=" ")
    else:
       print(' ',end=" ")
  print("\n")