
class BMW:
    def fuel_type(self):
        print("Gasoline")
    def max_speed(self):
        print("302 kph")
    
class Ferrari:
    def fuel_type(self):
        print("Premium fuel")
    def max_speed(self):
        print("350 kph")

bmw=BMW()
ferrari=Ferrari()
for car in (bmw,ferrari):
    car.fuel_type()
    car.max_speed()




    

 

    








