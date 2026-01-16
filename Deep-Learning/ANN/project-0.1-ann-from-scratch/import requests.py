import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response)

data = response.json()

print(type(data))
print(data[0])

print(len(data))

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
df["title"].head()

params = {"userId": 3}
response = requests.get(url, params=params)
df = pd.DataFrame(response.json())

print(df["userId"].unique())
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

all_data = []

for page in range(1, 4):
    params = {"_page": page, "_limit": 10}
    response = requests.get(url, params=params)
    all_data.extend(response.json())

df = pd.DataFrame(all_data)
print(df.shape)

# while more_data:
#     request page
#     save data

# import requests
# import pandas as pd

# url = "https://api.example.com/data"

# headers = {
#     "Authorization": "Bearer YOUR_API_KEY"
# }

# response = requests.get(url, headers=headers)

data = response.json()
df = pd.DataFrame(data)

data = {
    "id": 1,
    "user": {
        "name": "Ashir",
        "email": "ashir@email.com"
    }
}

print(data["user"]["name"])

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

data = response.json()

print(data[0])

df = pd.json_normalize(data)
print(df.head())


print(df[["name", "email", "address_city", "company_name"]])

