## 2. Authenticating with the API ##

# Create a dictionary with two keys, "Authorization" and "User-Agent", and corresponding values
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", 
           "User-Agent": "Dataquest/1.0"}

# Create a dictionary with one key, "t", and its corresponding value, "day"
params = {"t": "day"}

# Send a GET request to the specified URL, with the headers and parameters specified
response = requests.get(
                        "https://oauth.reddit.com/r/python/top", 
                        headers=headers, 
                        params=params
                       )

# Parse the JSON response into a Python dictionary and assign it to the variable 'python_top'
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

## 4. Getting Post Comments ##

# Create a dictionary with two keys, "Authorization" and "User-Agent", and corresponding values
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", 
           "User-Agent": "Dataquest/1.0"}

# Send a GET request to the specified URL, with the headers specified
response = requests.get(
                        "https://oauth.reddit.com/r/python/comments/4b7w9u", 
                        headers=headers
                       )

# Parse the JSON response into a Python dictionary and assign it to the variable 'comments'
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

# Extract the list of comments from the "children" key of the "data" dictionary in the second item of the "comments" dictionary.
comments_list = comments[1]["data"]["children"]

# Initialize variables for the most upvoted comment ID and the number of upvotes it received.
most_upvoted_comment = ""
most_upvotes_comment = 0

# Iterate through each comment in the list of comments.
for comment in comments_list:
    # Extract the "data" dictionary from the current comment.
    co = comment["data"]
    
    # Check if the number of upvotes for the current comment is greater than or equal to the current highest number of upvotes.
    if co["ups"] >= most_upvotes_comment:
        # If so, update the most upvoted comment ID and the highest number of upvotes to the current comment's values.
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]

## 6. Upvoting a Comment ##

# Create a dictionary 'payload' with two keys, "dir" and "id", and their corresponding values.
payload = {"dir": 1, "id": "d16y4ry"}

# Create a dictionary 'headers' with two keys, "Authorization" and "User-Agent", and their corresponding values.
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

# Send a POST request to the specified URL "https://oauth.reddit.com/api/vote" with the payload and headers specified.
response = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)

# Get the status code from the response and assign it to the variable 'status'.
status = response.status_code