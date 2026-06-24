import pandas as pd
shaurya = pd.read_csv('./Datasets/amazon_fires.csv', encoding = 'ISO-8859-1')
print(shaurya)

#Write a query to retrieve all passengers who embarked from southampton (Embarked = 'S')
print(shaurya[shaurya['embarked'] == 'S'])


#Filter the dataset to find passengers who paid a fare between 20 and 40 units of currency.
print(shaurya[(shaurya['fare'] >= 20) & (shaurya['fare'] <= 40)])


#Filter the dataset to find passengers whose age is missing (Age = NaN)
print(shaurya[shaurya['age'].isnull()])



#Write a query to retrieve passengers who had siblings or spouses abroad the titanic.
print(shaurya[shaurya['sibsp'] > 0])


#Write a query to find passengers who survived and paid more than median fare.
print(shaurya[(shaurya['survived'] == 1) & (shaurya['fare'] > shaurya['fare'].median())])


#write a query to retrieve passengers who were under tha age 18.
print(shaurya[shaurya['age'] < 18])

#Write a query to retrive only the passengers who were both female and survived.
print(shaurya[(shaurya['survived'] == 1) & (shaurya['sex'] == 'female')])