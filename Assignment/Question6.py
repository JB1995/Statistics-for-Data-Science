# Question 6: Group teams based on their “Best position” and print the sum of their points for all positions
class Solution6:
    def __init__(self, data):
        self.data = data
    def groupByBestPosition(self):
        self.data['BestPosition'] = self.data['BestPosition'].astype(int)
        bestpos = self.data.groupby('BestPosition').sum().sort_values(by='BestPosition', ascending=True)['Points']
        print('Solution 6:')
        print(bestpos)
        return self.data