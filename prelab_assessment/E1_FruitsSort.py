#exercise 1: sort the fruits and veggies by string size
import pandas as pd
from pathlib import Path

#file path to the fruits txt file
HERE = Path(__file__).parent #tells me to go to the directory where this file is located (and look at everything in the parent folder)
#fruits_csv = ('C:/Users/taylo/github/bme547/prelab_assessment/fruits.txt') #old absolute path
fruits_csv = HERE / 'fruits.txt' #find fruits.txt in that parent folder

fruits_df = pd.read_csv(fruits_csv, header=None)
fruits_list = fruits_df.iloc[0].str.strip().tolist()
print("whole list", fruits_list)

#max character length of the strings
max_length = 5

short_list = [fruit for fruit in fruits_list if len(fruit) <= max_length]
long_list = [fruit for fruit in fruits_list if len(fruit) > max_length]

print("short list", short_list)
print("long list", long_list)