#def multiply(*args): 
   # print(args) 
    #total = 1
    #for arg in args:
       # total = total * arg

   # return total
#print(multiply(1, 3, 5))


#def add(x, y):
    #return x + y

#nums= [3, 5]
#print(add(*nums))


#nums= [3, 5]
#print(add(x=3, y= 5))


#print(add(x= nums["x"], y= nums["y"]))

#nums= {"x":15, "y": 25}
#print(add(**nums))

def multiply(*args): 
    print(args) 
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to aply()."
    
print(apply(1, 3, 6, 7, operator="*"))

    
