laser_range = [0.1, 0.2, 0.3, 0.4, 0.5]

import numpy as np

laser_arr = np.array(laser_range)
print(np.count_nonzero(laser_arr>=0.2))

import math
conv_radian = math.radians(90)
con_degree = math.degrees(conv_radian)
print(conv_radian, ',', con_degree)
