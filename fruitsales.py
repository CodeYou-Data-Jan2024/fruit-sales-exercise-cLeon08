#importing pandas library
import pandas as pd

#creating a pandas dataframe to represen data given and storing in a variable
fruits = pd.DataFrame({'Apples':[35,41], 'Bananas':[21,34]},
                      index=['2017 Sales','2018 Sales'])

#writing the dataframe to the csv file
fruits.to_csv("fruit.csv")