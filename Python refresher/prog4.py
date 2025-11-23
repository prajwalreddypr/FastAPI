# Functions Assignment
# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values

def user_details(firstname, lastname, age):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
             
             }

user = user_details(firstname = "Prajwal", lastname = "Reddy", age = 25)

print(user)
