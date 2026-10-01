length1= float(input(" Enter the length of rectangle 1 :"))
width1= float(input(" Enter the width of rectangle 1:"))

area1 = length1 * width1

length2= float(input("Enter the length of rectangle 2 :"))
width2 = float(input(" Enter the width of rectangle 2 : "))

area2= length2 * width2

if area1> area2:
    print(" Area 1 is greater than Area 2 and its area is = ", area1)
    
elif area1< area2:
    print(" Area 2 is greater than Area 1 and its area is = ", area2)

else:
    print(" Both areas are equal and the area is = ", area1)

