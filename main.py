print("Treasure Map")
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row_position = int(position[0])
column_position = int(position[1])

map[column_position - 1][row_position - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")