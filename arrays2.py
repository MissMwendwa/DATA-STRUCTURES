import array as r
#An array is mutable hence different indices can be changed aslong as there is one data type
#Syntax(demo with the methods)
#Character data types in array use "u" as the datatype identifier, where u stands for unicode

'''array_name = (how you import the array).array("data_type", [])'''


arrayA = r.array("i",[3,8,9,3,5])
# arrayB = r.array("u", ["Faith","Mark","Henry","Lilly"])

var1 = 6
var2 = 0
arrayA.append(var1)
print(arrayA)
# print(arrayB)

#insert()
newarray = r.array("u")
# variables
var3 = "v"
var4 = "k"
var5 = input("Enter a character value: ")
var6 = input("Enter a character value: ")

newarray.insert(0,var3)
newarray.insert(1,var4)
newarray.insert(2,var5)
newarray.insert(3,var6)
print(newarray)
print(newarray[2])
print(newarray[4])



# newarray2 = r.array("f")
# newarray2.insert(0,3.14)
# print(newarray2)