#1. K-Closest Points to Origin
#Problem Statement:
#
#Given a list of points on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points is the Euclidean distance.
#
#Requirements:
#
#Implement a solution that efficiently computes the k closest points using a heap.



import math
def KpointsToOrigin(lst: list, count: int) -> list:

    distanceList = []

    for i in range(len(lst)):
        x = lst[i][0]
        y = lst[i][1]

        distance = math.sqrt(x ** 2 + y ** 2)

        distanceList.append(distance)

    distanceList.sort()


    result = []
    for i in range(count):
        result.append(distanceList[i])

    return result

assert KpointsToOrigin([[1,2], [3, 4]], 1) == [[1,2]]
