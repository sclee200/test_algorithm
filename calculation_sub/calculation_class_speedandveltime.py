
# global weight
# weight =999
from calculation_sub02.calculation_class_speedandveltime02 import speedVelTime02

class speedVelTime():
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

    def printOther02Class(self):
        inst = speedVelTime02(1000, 200, 5)
        inst.printAll()
        # speedVelTime02.printAll()

if __name__ == '__main__':
     
    inst = speedVelTime(10000,20,5)
    print(inst.getDistance())
    print(inst.getTime())
    # print(inst.printDistanceAndTime())
    inst.printDistanceAndTime()
    inst.printOther02Class()
    
    
    # pass

