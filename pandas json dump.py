import pandas as pd

# Create a sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'Department': ['HR', 'Marketing', 'Finance', 'IT', 'Sales']
}

df = pd.DataFrame(data)
print(df)
from json import loads, dumps
json_output = df.to_json(orient="table")
parsed = loads(json_output)
dumps(json_output) 