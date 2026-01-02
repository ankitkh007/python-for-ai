import os
import pandas as pd

# try:
#     df=pd.read_csv("sales-analysi/data/sales.csv")
#     print(df['product'])
# except FileNotFoundError:
#     print("could not find the file.")


try:
    with open('data/kolkata.csv', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")

numbers=[1,2,3]
# Check length first
if len(numbers) > 5:
    print(numbers[5])
# Handle the error
try:
    print(numbers[5])
except IndexError:
    print("List too short")