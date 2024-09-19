#def named(**anyword):
   # print(anyword)


#named(name="Bob", age = 25)

#def named(name, age):
#    print(name, age)

#details = {"name": "Bob", "age": 25}
#named(**details)

#def named(**whatever):
    #print(whatever)
    
#def print_nicely(**whatever):
    #named(**whatever)
    #for arg, value in whatever.items():
        #print(f"{arg}: {value}")

#print_nicely(name= "Bob", age=25)

#def both(*args, **kwargs):
  #  print(args)
 #   print(kwargs)
#both (1, 3, 5, name= "Bob", age=25)


#def post(url, data=None, json=None, *kwargs):
    #return request('post', url, data= data, json=json, **kwargs)

def myfunction(**kwargs):
    print(kwargs)

#myfunction(**Bob) #Error, must be mapping
#myfunction(**None) #Error. Not a dictionary