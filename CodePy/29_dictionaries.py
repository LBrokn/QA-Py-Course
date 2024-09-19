users = [
     (0, "user1", "password"),
     (1, "user2", "123456"),
     (2, "user3", "password1"),
     (3, "username", "password2"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]
if password_input == password:
    print("Your details are correct")
else:
    print("Your details are incorrect.")












#or
#for user in users:
    #if user[1] == "user1"
        #print(user)