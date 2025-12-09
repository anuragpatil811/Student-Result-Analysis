import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("C:/Users/Admin/Downloads/Expanded_data_with_more_features.csv/student_scores.csv")
#print(df.head())
#print(df.describe())
#print(df.info())
#print(df.isnull().sum())

#**Drop Unnamed Column**
df = df.drop("Unnamed: 0", axis = 1)
#print(df.head())

#**Change weekly study hours column**
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")
#print(df.head())


#**Gender Distribution**
#plt.figure(figsize=(5, 5))
ax=sns.countplot(data=df, x="Gender")
ax.bar_label(ax.containers[0])
#plt.title("Gender Distribution")
#plt.show()  
"""""
from the above chart we have analyzed that
 the number of females in the data is more than the number of males
"""


#**Impact of Parent's education on Student's scores**
gb = df.groupby("ParentEduc").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
#print(gb)
#plt.figure(figsize=(4, 4))
#plt.title("Relationshp between parent's education and student's scores")
#sns.heatmap(gb, annot=True)
#plt.show()
"""""
from the above heatmap we can analyze that the education of the parents have a good impact
on the student's scores
"""

#**Impact of Parent's Marital Status on Student's scores**
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean', "ReadingScore": "mean", "WritingScore": "mean"})
#print(gb1)
#plt.figure(figsize=(4, 4))
#plt.title("Relationshp between parent's marital status and student's scores")
#sns.heatmap(gb1, annot=True)
#plt.show()
"""""
from the above chart we have concluded that there is no /negligible impact on the student's
 score due to marital status of parents
"""

#Outliers = values that are outside the range
sns.boxplot(data=df, x = "MathScore")
#plt.show()
#print(df["EthnicGroup"].unique())

#**Distribution of Ethnic Groups
groupA = df.loc[(df['EthnicGroup']=="group A")].count()
groupB = df.loc[(df['EthnicGroup']=="group B")].count()
groupC = df.loc[(df['EthnicGroup']=="group C")].count()
groupD = df.loc[(df['EthnicGroup']=="group D")].count()
groupE = df.loc[(df['EthnicGroup']=="group E")].count()
#print(groupA["EthnicGroup"])
l = ["group A", "group B", "group C", "group D", "group E"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
#plt.pie(mlist, labels=l)
#plt.title("Distribution of Groups")
#plt.show()
ax = sns.countplot(data=df, x="EthnicGroup")
ax.bar_label(ax.containers[0])