marks =[85, 92, 78, 96, 88]
print(" Marks:", marks)

#append a new mark to the list
marks.append(90)
print(" After appending a new marks:", marks)

#insert a new mark at index 2
marks.insert(2,95)
print(" After inserting a new mark at inset index 2:", marks)

#remove a mark from the list
marks.remove(78)
print(" After removing a mark:", marks)

#sort the marks in asending order
marks.sort()
print(" After sorting the marks in asending order:", marks)

print(" the highest mark is:", max(marks))
print(" the lowest mark is:", min(marks))

print(" Total students:", len(marks))

#check existing mark
search= int(input(" Entrer a mark to search:"))

found =int(False)
for mark in marks:
    if mark == search:
        found = True
        
if found:
    print(" Mark found in the list.")
else:
    print(" Mark not found in the list.")
            
