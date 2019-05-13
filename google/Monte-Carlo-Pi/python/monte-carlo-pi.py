from typing import List
import random

def monte_carlo_pi(interval: int) -> float:
    '''
    We assume that the central point of the circle is at the origin point
    (0,0) of the 2D coordinates. it's radius equals 1. Also, it 
    circumscribeds a 2x2 square
    '''
    R:int = 1
    point_in_square:int = 0
    point_in_cicle:int = 0

    for i in range(interval):
        point_in_square += 1
        x:float = round(random.uniform(-R,R), 3)
        y:float = round(random.uniform(-R,R), 3)
        if pow(x,2) + pow(y,2) <= pow(R,2):
            point_in_cicle += 1

    return round(4*(point_in_cicle / point_in_square),3)

if __name__ == "__main__":
    print(monte_carlo_pi(1200))