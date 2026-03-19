import pandas as pd

data = {
    'Name': ['alice', 'bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}


df = pd.DataFrame(data)
print(f"Data Frame:\n{df}\n-------")
print(f"Age column:\n{df['Age']}\n-------")
print(f"Row at index 1:\n{df.iloc[1]}")
