# name="   dAyanand"
# print(name)

# name="Dayanand Kumar"
# print(name)
# print(len(name))

#text= "PYTHON"
# print(text[0])
# print(text[1])
# print(text[-3])

#string slicing
#print(text[2:5])

#last three char
#print(text[3:])

#complete string
#print(text[:])

# name="Dayanand"
# print(name)
# print(len(name))
# print(name[0])
# print(name[4])
# print(name[2])
# print(name[5])
# print(name[-1])
# print(name[-4])
# print(name[-3])
# print(name[-2])

# print(name[1:4])
# print(name[:])

# name=" DaYaNaNd KuMAR "
# clean_name= name.strip()
# print(clean_name)

# text=" hello daya  "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# #case convesion
# text =" python Programming"
# print(text.upper())
# print(text.lower())
# #print(text.capitalize()) that only here 1st latter

# #replace
# text=" I like python"
# text1=" I like game"
# new_text= text.replace("python", "Java")
# new_text1=text1.replace("game", "cricket")
# print(new_text)
# print(new_text1)

#text cleaner and analyzer

text=input(" Enter a sentence")
print(text)

#clean and normalize
clean_text=text.strip()
normalize_text= clean_text.lower()

#after cleaning
charecter_cout=len(clean_text)



print(clean_text)
print(normalize_text)