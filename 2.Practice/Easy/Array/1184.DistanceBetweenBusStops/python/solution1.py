class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cw = 0
        i = start

        while i != destination:
            cw += distance[i]

            i = (i + 1) % len(distance)

        ccw = 0
        i = start

        while i != destination:
            print(distance[-1])
            i = (i - 1) % len(distance)

            ccw += distance[i]

        return min(cw, ccw)