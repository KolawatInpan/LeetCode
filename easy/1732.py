class Solution:
    def largestAltitude(self, gain: list) -> int:
        curr_altitude = 0
        max_altitude = 0
        
        for i in gain:
            curr_altitude += i
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude

print(Solution().largestAltitude([52, -91, 72]))  # 1