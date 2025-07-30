class vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class bus:
    pass
schoolbus=bus("volvo",180,12)
print("vehicle name",schoolbus.name,"max speed",schoolbus.max_speed,"milage",schoolbus.milage)