## importing entire built-in package
import math 

math.sqrt(16)
math.pow(2,5)

## another method is to import only specific function from the package like this
from math import sqrt,pow

sqrt(16)
pow(2,5)

# Import entire module
import random

# Use module functions
print(random.randint(1,10))
print(random.choice(["apple", "banana", "orange"]))

# Date and time
import datetime
print(datetime.date.today())
print(datetime.datetime.now())

from datetime import datetime, timedelta
print(datetime.now())
print(datetime.now()-timedelta(days=7))

# Operating system
import os
current_dir=os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)


# Import with alias
import pandas as pd
df = pd.DataFrame(data)


# Web requests
import requests

response = requests.get("https://api.sampleapis.com/coffee/hot")
data = response.json()
print(data[0])
# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)