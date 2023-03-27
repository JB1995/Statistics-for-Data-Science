# Question 2: Print all the teams which have started playing between 1930-1980.
import pandas as pd
class Solution2:
    def __init__(self, data):
        self.data = data
    
    def startedPlaying(self):
        self.data['Debut'] = self.data['Debut'].str[:4]
        started = self.data[(self.data['Debut']>='1930') & (self.data['Debut']<='1980')].sort_values(by='Debut', ascending=True)
        print('Solution 2:')
        print(started)
        return self.data