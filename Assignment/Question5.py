# Question 5:
# Create a new column with name “Winning Percent” and append it to the data set
# Percentage of Winning = (GamesWon / GamesPlayed)*100
# If there are any numerical error, replace it with 0%
# Print the top 5 teams which has the highest Winning percentage
class Solution5:
    def __init__(self, data):
        self.data = data
    def top5Winning(self):
        self.data['GamesWon'] = self.data['GamesWon'].astype(int)
        self.data['GamesPlayed'] = self.data['GamesPlayed'].astype(int)
        self.data['Winning Percent'] = (self.data['GamesWon']/self.data['GamesPlayed']*100).fillna(0)
        top5 = self.data.nlargest(5, 'Winning Percent', keep='all')
        print('Solution 5:')
        print(top5)
        return self.data