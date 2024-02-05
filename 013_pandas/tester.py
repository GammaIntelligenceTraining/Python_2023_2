import pandas as pd

df = pd.read_csv('csv_files/2019.csv')
pd.set_option('display.max_columns', 10)
# pd.set_option('display.max_rows', 160)

# print(df)
# print(df.head(3))
# print(df.tail(10))

# print(df.iloc[54])  # SERIES OBJECT
# print(df.iloc[54:58])  # DATAFRAME OBJECT
# print(df.iloc[[0, 72, 54, 13]])  # DATAFRAME OBJECT

# print(df.iloc[54:60, 1:3])
# print(df.loc[54:60, ['Country or region', 'Social support']])
# print(df['Country or region'].value_counts())

# data = df.loc[2:6]
# print(data['Country or region'])

# print(df.loc[df['Country or region'] == 'Estonia'])
# print(df.loc[df['GDP per capita'] == 1.452])
# print(df.loc[df['GDP per capita'] > 1, ['Country or region', 'GDP per capita']])

# print(df.describe())
# print(df.memory_usage(deep=True))
# print(df.sort_values('GDP per capita', ascending=False).head(10))
# print(df.sort_values(['Country or region', 'Perceptions of corruption'], ascending=[True, False]))

# df['Total'] = df['GDP per capita'] + df['Score']
# df.insert(loc=3, column='Total', value=(df['GDP per capita'] + df['Score']))
# print(df)
# df = df.drop(columns=['Total'])
# print(df)

# print(df.dtypes)

# print(df.loc[df['Country or region'].str.contains('on|an')])

# print(df.groupby('Country or region').count())

# print(df.nlargest(10, 'GDP per capita'))
# print(df.nsmallest(10, 'GDP per capita'))

import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='sakila'
)

df = pd.read_sql_query('SELECT * FROM actor;', conn)
print(df)

df.to_excel('output.xlsx')