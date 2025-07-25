class vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
model=vehicle(240,18)
print("model speed",model.max_speed)
print("model milage",model.milage)