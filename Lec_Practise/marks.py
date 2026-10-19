marks=[85, 92, 78, 96, 88]
marks.index(78)
print("Index of 78 in the marks list:", marks.index(78))

m= marks.index(78)
marks[m]= 80
print("Marks list after replacing 78 with 80:", marks)

marks.sort()
print("Marks list after sorting:", marks)