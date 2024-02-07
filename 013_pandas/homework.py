import pandas as pd

'''
Homework:
For the Stack Overflow survey (017_pandas/csv_files/survey_results_public.csv)
Write a program that, based on user choice, does the following:
1. Displays data on the number of programmers who are professionals and how many are hobbyists. (column 'Hobbyist')
2. Displays the average, maximum, and minimum age (column 'Age') of programmers.
3. Displays a table with countries (column 'Country'). Groups them, counts the number, and displays in descending order.
4. Displays a table with currencies (column 'CurrencyDesc'). Groups and displays in ascending order.
'''

survey = pd.read_csv('csv_files/survey_results_public.csv')

# print(survey['Hobbyist'].value_counts())
# print(survey.groupby('Hobbyist').count()['Respondent'])

# print(f'Minimum age is {survey["Age"].min()}')
# print(f'Maximum age is {survey["Age"].max()}')
# print(f'Average age is {survey["Age"].mean()}')

# print(survey['Country'].value_counts(ascending=False))
# print(survey.groupby('Country').count().sort_values('Respondent', ascending=False)['Respondent'])
#
# print(survey[['CurrencyDesc', 'CurrencySymbol']].value_counts(ascending=False))
# print(survey.groupby('CurrencyDesc').count().sort_values('Respondent', ascending=False)['Respondent'])
