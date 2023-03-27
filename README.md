# Statistics-for-Data-Science
`Assignment description`

[`Certificate: Statistics for Data Science`](https://olympus.mygreatlearning.com/courses/11266/certificate)

[`Certificate: Probability and Probability Distributions for Machine Learning`](https://olympus.mygreatlearning.com/courses/34995/certificate)

Dataset: Laliga.csv

Think of yourself, currently working as a Business analyst in one of the top sports company. The senior management team has asked you to come up with metrics with which they can gauge which team will win the upcoming La Liga cup (Football tournament).

The data set contains information on all the teams so far participated in all the past tournaments. It has data about how many goals each team scored, conceded, how many times they came within first 6 positions, how many seasons they have qualified, their best position in the past etc.

You are required to do the following:

1. Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data.
2. Print all the teams which have started playing between 1930-1980.
3. Print the list of teams which came Top 5 in terms of points.
4. Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference.
        `Goal_diff_count = GoalsFor - GoalsAgainst`
 5. Create a new column with name “Winning Percent” and append it to the data set
         `Percentage of Winning = (GamesWon / GamesPlayed)*100`
    If there are any numerical error, replace it with 0%
    
    Print the top 5 teams which has the highest Winning percentage.
 6. Group teams based on their “Best position” and print the sum of their points for all positions.
