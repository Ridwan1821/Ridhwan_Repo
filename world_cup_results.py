import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('world_cup_results.csv')

print(df)
print(df.describe)
print(df.head())
print(df.isnull())
df1 = df.iloc[:, 7:8].values
df2 = df.iloc[:, 8:9].values
df3 = df1 + df2
'''print(df1)
print(df2)'''
print(df3)

df['TotalGoals'] = df3
df.to_csv('Fifa_World_Cup_Results.csv')
df.drop_duplicates()
print(df)
print(df.info())


#Number of games played in each tournament year
Games_per_year = df.Year.value_counts()
print(Games_per_year)

All_Games = pd.DataFrame(Games_per_year)
All_Games.reset_index(inplace=True)
All_Games.columns = ['Year', 'Matches'] 
print(All_Games)

sns.catplot(x='Year', y='Matches', data=All_Games, kind='bar')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.title('Number of Matches Per Year')

#Total Goals scored in each tournament year
df4 = df.pivot_table('TotalGoals', index='Year', aggfunc=sum)
print(df4)

df5 = pd.DataFrame(df4)
df5.reset_index(inplace=True)
df5.columns = ['Year', 'TotalGoals'] #This must be done for the plot to work with df4 as its data
print(df5)

sns.catplot(x='Year', y='TotalGoals', data=df4, kind='bar')
plt.xlabel('Year')
plt.ylabel('Total Goals')
plt.title('Number of Goals Per Tournament Year')
#df5 can also be used for the plot but I decided to use df4 here

#Start comment
sns.catplot(x='Year', y='TotalGoals', data=df5, kind='bar')
plt.xlabel('Year')
plt.ylabel('Total Goals')
plt.title('Number of goals per tournament Year')
#This gives the same plot as the one above, but with df5 as the considered data
#End comment

#Teams and number of times in finals
df6 = df[df['Round']=='Final']
print(df6)
df7 = df6['HomeTeam']
df8 = df6['AwayTeam']
df9 = df7.append(df8)
print(df9)

df10 = df9.value_counts()
print(df10)
Teams_in_final = pd.DataFrame(df10)
Teams_in_final.reset_index(inplace=True)
Teams_in_final.columns = ['Team', 'Number of Times in Finals']
print(Teams_in_final)

sns.catplot(x='Number of Times in Finals', y='Team', data = Teams_in_final, kind = 'bar')
plt.xlabel('Number of Final Games Played')
plt.ylabel('Team')
plt.title('Teams and Number of Times in Finals')
'''
#Start comment
#Another way of getting the above plot is has been given below:
Finalists = Teams_in_final.pivot_table('Number of Times in Finals', index= 'Team', aggfunc=sum)
#print(Finalists)
df11 = pd.DataFrame(Finalists)
df11.reset_index(inplace=True)
df11.columns = ['Team', 'Number of Times in Finals'] #This must be done for the plot to work with Finalists as its data
#print(df11)

sns.catplot(x='Team', y='Number of Times in Finals', data = Finalists, kind = 'bar')
plt.xlabel('Team')
plt.ylabel('Number of Finals played')
#plt.show() #plot was given with Teams in alphabetical order
#End comment
'''
#Teams and number of times in semi finals
df12 = df[df['Round'] == 'Semi-finals']
print(df12)
df13 = df12['HomeTeam']
df14 = df12['AwayTeam']
df15 = df13.append(df14)
print(df15)

df16 = df15.value_counts()
print(df16)

Teams_in_semi_final = pd.DataFrame(df16)
Teams_in_semi_final.reset_index(inplace=True)
Teams_in_semi_final.columns = ['Team', 'Number of Times in Semi-finals']
print(Teams_in_semi_final)

sns.catplot(x='Number of Times in Semi-finals', y='Team', data = Teams_in_semi_final, kind='bar')
plt.xlabel('Number of Semi Final Games Played')
plt.ylabel('Team')
plt.title('Teams and Number of Times in Semi Finals')

#Teams and number of times in quarter finals
df17 = df[df['Round'] == 'Quarter-finals']
print(df17)
df18 = df17['HomeTeam']
df19 = df17['AwayTeam']
df20 = df18.append(df19)
print(df20)

df21 = df20.value_counts()
print(df21)

Teams_in_quarter_final = pd.DataFrame(df21)
Teams_in_quarter_final.reset_index(inplace=True)
Teams_in_quarter_final.columns = ['Team', 'Number of Times in Quarter-finals']
print(Teams_in_quarter_final)

sns.catplot(x='Team', y='Number of Times in Quarter-finals', data = Teams_in_quarter_final, kind='bar')
plt.xlabel('Number of Quarter Final Games Played')
plt.ylabel('Team')
plt.title('Teams and Number of Times in Quarter Finals')
#plt.show()

df22 = df[df['Round'] == 'Quarter-finals']
print(df22)

df23 = df22['TotalGoals']
print(str(df23.sum()) + ' goals were scored in all quarter finals.')
print('An average of ' + str(df23.mean()) + ' goals were scored in each quarter final game.')

df24 = df[df['Round'] == 'Semi-finals']
print(df24)

df25 = df24['TotalGoals']

print(str(df25.sum()) + ' goals were scored in all semi finals.')
print('An average of ' + str(df25.mean()) + ' goals were scored in each semi final game.')

df26 = df[df['Round'] == 'Final']
print(df26)

df27 = df26['TotalGoals']

print(str(df27.sum()) + ' goals were scored in all finals.')
print('An average of ' + str(df27.mean()) + ' goals were scored in each final game.')

df28 = df[df['Round'] == 'Group 1'] 
df29 = df[df['Round'] == 'Group 2']
df30 = df[df['Round'] == 'Group 3']
df31 = df[df['Round'] == 'Group 4']
df32 = df[df['Round'] == 'Group 5']
df33 = df[df['Round'] == 'Group 6']
df34 = df[df['Round'] == 'Group A']
df35 = df[df['Round'] == 'Group B']
df36 = df[df['Round'] == 'Group C']
df37 = df[df['Round'] == 'Group D']
df38 = df[df['Round'] == 'Group E']
df39 = df[df['Round'] == 'Group F']
df40 = df[df['Round'] == 'Group G']
df41 = df[df['Round'] == 'Group H']
df42 = df[df['Round'] == 'Preliminary round']
df43 = df[df['Round'] == 'First round']
df44 = df[df['Round'] == 'Round of 16']
df45 = df28.append([df29, df30, df31, df32, df33, df34, df35, df36, df37, df38, df39, df40, df41, df42, df43, df44], ignore_index=True)
print(df45)

df46 = df45['TotalGoals']

print(str(df46.sum()) + ' goals were scored outside quarter finals and above.')
print('An average of ' + str(df46.mean()) + ' goals were scored in each game outside quarter finals and above.')

df47 = df45['Round']
df48 = df47.count()
print(df48)

print('A total of ' + str(df48.sum()) + ' matches was played outside quarter finals and above.')

'''
df49 = df['Outcome']
#print(df49)

df50 = [outcome for outcome in df49]
df51 = Series(df50)
df52 = df51.replace(['D','A', 'H'], ['Draw', 'AwayTeam wins', 'HomeTeam wins'])
print(df52)

df53 = pd.DataFrame(df52)
df53.columns = ['Outcome']
print(df53)

df54 = pd.concat([df, df53], axis=0, join='outer', ignore_index=False)
print(df54.head(100))

#print(pd.merge(df, df53))
'''










