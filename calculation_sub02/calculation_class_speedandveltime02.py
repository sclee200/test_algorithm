
# global weight
# weight =999


class speedVelTime02():
    def __init__(self, distance, vel, time) -> None:
        self.distance = distance
        self.vel = vel
        self.time= time
    def getDistance(self):         
        self.distance = self.vel*self.time
        return self.distance
    def getTime(self):         
        self.time = self.distance/self.vel
        return self.time
    def printDistanceAndTime(self):
        self.getDistance()
        self.getTime()
        print('distance : ', self.distance, 'time :', self.time)
    def printAll(self):
        print('distance : ', self.distance, 'vel :', self.vel, 'time :', self.time)

if __name__ == '__main__':
     
    inst = speedVelTime02(10000,20,5)
    print(inst.getDistance())
    print(inst.getTime())
    # print(inst.printDistanceAndTime())
    inst.printDistanceAndTime()
    
    
    # pass

