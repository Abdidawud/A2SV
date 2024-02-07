class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum=[0]*n
        for i in bookings:
            prefix_sum[i[0]-1]+=i[2]
            if i[1]<len(prefix_sum):
                prefix_sum[i[1]] -= i[2]
        for i in range(1,len(prefix_sum)):
            prefix_sum[i]+=prefix_sum[i-1]
        return prefix_sum