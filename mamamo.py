class vehicle(self, plate_number, model):
    def __init__(plate_number, model):
        self.plate_number = plate_number
        self.model = model

class driver(name, assigned_vehicle):
    def __init__(name, assigned_vehicle):
        self.name = name
        self.assigned_vehicle = None

    def assigned_vehicle(self, vehicle):
        self.assigned_vehicle = vehicle

#create vehicle object
vehicle1 = vehicle("ABC1234", "Toyota Vios")

#create driver object
driver1 = driver("Mr. Santos")

#assign the vehicle to the driver
driver1.assigned_vehicle(vehicle1)

print("Driver", driver1)
print("plate number: ", driver1.assigned_vehicle.plate_number)
print("model: ", driver1.assigned_vehicle.model)

