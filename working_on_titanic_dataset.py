import pandas as pd
shaurya = pd.read_csv('./Datasets/amazon_fires.csv', encoding = 'ISO-8859-1')
print(shaurya)

#Write a query to retrieve all passengers who embarked from southampton (Embarked = 'S')
print(shaurya[shaurya['embarked'] == 'S'])