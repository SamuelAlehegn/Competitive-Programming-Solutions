from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            distance_list.append([distance, point])

        distance_list.sort()

        return [distance_list[i][1] for i in range(k)]
