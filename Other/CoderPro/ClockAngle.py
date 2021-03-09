''' Calcualte the angle between the minute and hour hand on a clock face given the time '''

class Solution:
    def calcAngle(self, h, m):
        hour_angle = (360 / (12 * 60.0)) * (h * 60 + m)
        min_angle = 360 / 60.0 * m
        angle = abs(hour_angle - min_angle)
        return min(angle, 360 - angle)

s = Solution()
print(s.calcAngle(11,30))