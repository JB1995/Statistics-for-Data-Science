import pandas as pd
class Solution:
    #Question 1
    global data
    data = pd.read_csv('Laliga.csv', header=None)
    data.dropna(axis=0, how='all', inplace=True)
    data.columns=data.iloc[0]
    data.drop(index=1, inplace=True)
    data.replace('-', 0, inplace=True)
    print('Solution 1:')
    print(data)

    # Question 2
    data['Debut'] = data['Debut'].str[:4]
    started = data[(data['Debut']>='1930') & (data['Debut']<='1980')].sort_values(by='Debut', ascending=True)
    print('Solution 2:')
    print(started)

    # Question 3
    data['Points']=data['Points'].astype(int)
    top5 = data.nlargest(5, 'Points', keep='all')
    print('Solution 3:')
    print(top5)

    # Question 4
    # grouped = data.groupby('Team')['Team'].count()
    # grouped2 = data.groupby('Team').size()
    # data = data[data>1]
    def Goal_diff_count():
        data['GoalsFor'] = data['GoalsFor'].astype(int)
        data['GoalsAgainst'] = data['GoalsAgainst'].astype(int)
        data['GoalDiffCount'] = data['GoalsFor'] - data['GoalsAgainst']
        print("Maximum Goal Difference: ", data['GoalDiffCount'].max())
        print("Minimum Goal Difference: ", data['GoalDiffCount'].min())
    print('Solution 4:')
    Goal_diff_count()
    print(data)
    
    # Question 5
    data['GamesWon'] = data['GamesWon'].astype(int)
    data['GamesPlayed'] = data['GamesPlayed'].astype(int)
    data['Winning Percent'] = (data['GamesWon']/data['GamesPlayed']*100).fillna(0)
    top5winning = data.nlargest(5, 'Winning Percent', keep='all')
    print('Solution 5:')
    print(top5winning)

    # Question 6
    data['BestPosition'] = data['BestPosition'].astype(int)
    bestpos = data.groupby('BestPosition').sum().sort_values(by='BestPosition', ascending=True)['Points']
    print('Solution 6:')
    print(bestpos)