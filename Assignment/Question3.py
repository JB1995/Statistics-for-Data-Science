# Question 3: Print the list of teams which came Top 5 in terms of points
class Solution3:
    def __init__(self, data):
        self.data = data
    def top5teams(self):
        self.data['Points'] = self.data['Points'].astype(int)
        top5 = self.data.nlargest(5, 'Points', keep='all')
        print('Solution 3:')
        print(top5)
        return self.data