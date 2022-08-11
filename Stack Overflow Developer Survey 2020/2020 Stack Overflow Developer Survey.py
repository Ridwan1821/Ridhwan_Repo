import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('survey_results_public.csv')
print(df.head())
print('\n')


schema = pd.read_csv('survey_results_schema.csv')
print(schema.head())
print('\n')

print(df.info())
print('\n')

print(df.describe())
print('\n')

df1 = df['Respondent']
print('A total of ' + str(df1.count()) + ' developers participated in this survey.')
print('\n')

df2 = df.Country.value_counts()
print('The top 10 countries participating developers came from are:')
print(df2.head(10))
Top_Countries = pd.DataFrame(df2.head(10))
Top_Countries.reset_index(inplace=True)
Top_Countries.columns = ['Country', 'No of developers']
sns.catplot(x='Country', y='No of developers', data = Top_Countries, kind='bar')
plt.title('The top 10 countries participating developers are from')
plt.xlabel('Country')
plt.ylabel('No of developers')
#plt.show()


print('\n')

df3 = df[df['Country'] == 'Nigeria']
df4 = df3['Country']
print(str(df4.count()) + ' developers from Nigeria participated in this survey.')
print('\n')

df5 = df3['Age1stCode']
df6 = pd.to_numeric(df5, errors='coerce')
print('The average age the Nigerian developers wrote their first code is ' + str(df6.mean()) + '.')
print('\n')

df7 = df3['Age']
print('The average age of the Nigerian developers is ' + str(df7.mean()) + '.')
print('\n')

df8 = df3['Employment']
print('The kinds of employments of the Nigerian developers that participated in this survey are:')
print(df8.value_counts())
Employment = pd.DataFrame(df8.value_counts())
Employment.reset_index(inplace=True)
Employment.columns = ['Employment Status', 'Count']
sns.catplot(x='Count', y='Employment Status', data = Employment, kind='bar')
plt.title('Kind of Employment of Nigerian developers')
plt.xlabel('No of developers')
plt.ylabel('Employment Status')
#plt.show()
print('\n')

df9 = df3['Gender']
print('The gender distribution of the Nigerian developers that participated in this survey is:')
#df9[df3['Gender'] == 'Man'] = 'Man'
#df9[df3['Gender'] == 'Woman'] = 'Woman'
#df9[df3['Gender'] == 'Woman;Man'] = 'Woman;Man'
df9[df3['Gender'] == 'Non-binary, genderqueer, or gender non-conforming'] = 'Non-Binary/Genderqueer'
df9[df3['Gender'].isnull()==True] = 'None'
print(df9.value_counts())
print('\n')

Gender = pd.DataFrame(df9.value_counts())
Gender.reset_index(inplace=True)
Gender.columns = ['Gender', 'Count']

Gender = pd.DataFrame(df9.value_counts())
Gender.reset_index(inplace=True)
Gender.columns = ['Gender', 'Count']
print(Gender)

Gender.groupby(['Gender']).sum().plot(kind='pie', y='Count', autopct='%1.5f%%')


df10 = pd.Series(df3['UndergradMajor'].dropna(), dtype=str)
print('The undergraduate major of the Nigerian developers that participated in this survey are:')
print(df10.value_counts())
Undergrad_major = pd.DataFrame(df10.value_counts())
Undergrad_major.reset_index(inplace=True)
Undergrad_major.columns = ['Undergrad major', 'Count']
sns.catplot(x='Count', y='Undergrad major', data = Undergrad_major, kind='bar')
plt.title('Undergraduate major of the Nigerian developers')
plt.xlabel('No of developers')
plt.ylabel('Undergraduate major')
#plt.show()


print('\n')

df11 = df3['LanguageWorkedWith']

print('The Languages Nigerian developers that participated in this survey have worked with are:')
'''df12 = df11.value_counts()
df13 = pd.DataFrame(df12)
df13.reset_index(inplace=True)
df13.columns = ['Language', 'Count']'''

df12 = df11.str.split(';',expand=True,)
#df14 = df13.Language.str.split(';',expand=True,)

df13 = df12[0].append([df12[1], df12[2], df12[3], df12[4], df12[5], df12[6], df12[7], df12[8], df12[9], df12[10], df12[11], df12[12], df12[13], df12[14], df12[15], df12[16]], ignore_index=True)
print(df13.value_counts())

LanguageWorkedWith = pd.DataFrame(df13.value_counts())
LanguageWorkedWith.reset_index(inplace=True)
LanguageWorkedWith.columns = ['Language', 'Count']
sns.catplot(x='Count', y='Language', data = LanguageWorkedWith, kind='bar')
plt.title('Languages the Nigerian developers have worked with')
plt.xlabel('No of developers')
plt.ylabel('Language')
#plt.show()
print('\n')

df14 = df13.value_counts()
print('The average number of languages Nigerian developers have worked with is ' + str(round(df14.sum()/df4.count())) + '.')
print('\n')

df15 = df3['YearsCodePro']
df16 = df15.replace('Less than 1 year', 1)
df17 = pd.to_numeric(df16, errors='coerce')
print('The average number of years of experience of the Nigerian developers that participated in this survey is ' + str(df17.mean()) + 'years.')
print('\n')

#Kicker
df18 = df3[df3['MainBranch'] == 'I am a developer by profession']
df19 = df18[df3['Age'] < 25]
df20 = df19[df3['Gender'] == 'Woman']


print('Of the participants of this survey, only ' + str(df20['Respondent'].count()) + ' woman is below 25 years of age and is earning her living as a developer.')
print('\n')

df21 = pd.DataFrame(df14)
df21.reset_index(inplace=True)
df21.columns = ['Language', 'Count']
print('The ten most popular languages among Nigerian developers are:')
print(df21.head(10))
Popular_Language = df21.head(10)
sns.catplot(x='Language', y='Count', data = Popular_Language, kind='bar')
plt.title('Top 10 most popular languages among Nigerian developers')
plt.xlabel('Language')
plt.ylabel('No of developers')
#plt.show()



