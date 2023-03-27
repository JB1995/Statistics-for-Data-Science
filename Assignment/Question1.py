# Question 1: Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data.
import pandas as pd
class Solution1:
    def getdata(self):
        data = pd.read_csv('Laliga.csv', header=None)
        data.dropna(axis=0, how='all', inplace=True)
        data.columns=data.iloc[0]
        data.drop(index=1, inplace=True)
        data.replace('-', 0, inplace=True)
        print('Solution 1:')
        print(data)
        return data