# Create the shopping list
items= ["milk", "bread", "butter",  "apples", "bananas", "oranges"]
print(" Shopping list:",items)

#add tea at the end
items.append("tea")
print(" Shopping list after adding tea", items)

#insert "butter" at indx 1
items.insert(1, "Butter")
print(" Shopping list after inserting butter at index 1", items)

#remove "Bread"
items.remove("bread")
print(" Shopping list after removing bread", items)

# sort the list
items.sort()
print(" Shopping list after sorting", items)

#find the index of "apple"
apple_index = items.index("apples")
print(" Index of apple in the shopping list:", apple_index)

#replace "oranges" with "grapes"
#oranges_index = items.index("oranges")
items[oranges_index] = "grapes"
print(" Shopping list after replacing oranges with grapes", items)
