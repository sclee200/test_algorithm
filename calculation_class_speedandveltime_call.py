from calculation_sub.calculation_class_speedandveltime import speedVelTime
 
if __name__ == '__main__':
     
    inst = speedVelTime(10000,20,5)
    print(inst.getDistance())
    print(inst.getTime())
    # print(inst.printDistanceAndTime())
    inst.printDistanceAndTime()
    inst.printOther02Class()
    
    
    # pass

 