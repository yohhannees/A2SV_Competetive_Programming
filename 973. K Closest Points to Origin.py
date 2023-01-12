class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_dist = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            points_with_dist.append([dist, x, y])
        points_with_dist.sort(key=lambda x: x[0])
        for i in range(k):
            res.append([points_with_dist[i][1], points_with_dist[i][2]])
        return (res)
