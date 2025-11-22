my_vehicle = {
    
    "model": "Ford",
    "make": "Explporer",
    "year": 2018,
    "milage": 40000
}
for key, value in my_vehicle.items():
    print(f"Keys -> {key}, Value -> {value}")
    
    
vehicle2 = my_vehicle.copy()
vehicle2["number of tires"] = 4
vehicle2.pop("milage")


for key in vehicle2:
    print(f"Key -> {key}")


