#count the sum of number of null from the list?
#Using Python list (None values)

data = [1, None, 5, None, 8, None]

null_count = data.count(None)
print(null_count)


#Using Pandas list (counting None + NaN)
import pandas as pd
import numpy as np

data = [1, None, 5, np.nan, 8, None]

null_count = pd.Series(data).isna().sum()
print(null_count)


#Count nulls inside a list of dictionaries
data = [
    {"a": 1, "b": None},
    {"a": None, "b": 3},
    {"a": 4, "b": None}
]

null_count = sum(v is None for row in data for v in row.values())
print(null_count)
