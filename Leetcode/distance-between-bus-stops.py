class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            clock=sum(distance[destination:start])
        elif start<destination:
            clock=sum(distance[start:destination])
        else:
            clock=0
        
        x=sum(distance)
        anticlock=x-clock
        return min(clock,anticlock)