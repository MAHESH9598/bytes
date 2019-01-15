"""---> byte is one of the class treated as a datatype
--> This data type is used for storing range of values 0 to 256
--> immutable
--> To convert specified range of values into bytes datatype we use a predifined function called bytes()   """

a=[10,20,30,40,255]
print(a)
print(type(a))

bv=bytes(a)
print(bv)
print(type(bv))

for x in bv:
    print(x)


