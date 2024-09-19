a = 1
b = 1


print(id(a))
print(id(b))

a = 2

print(id(a))
print(id(b))



a = "hello"
b = a

print(id(a))
print(id(b))

a = a +"world"