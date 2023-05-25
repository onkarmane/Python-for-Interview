# import requests
# # https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english


# # Set the model name
# model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# # Set up API endpoint and headers
# api_url = f"https://api-inference.huggingface.co/models/{model_name}"
# headers = {
#     'Authorization': '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',
#     'Content-Type': 'application/json'
# }


# # Prepare input data
# data = {
#     'inputs': 'The movie is good'
# }


# # Make API request
# response = requests.post(api_url, headers=headers, json=data)


# # Process the response
# result = response.json()
# # classification = result['outputs'][0]['label']
# print(result)

import requests

# Get your API token from https://huggingface.co/settings/tokens
api_token = "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"

# Set the model name
model_name = "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2"

# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

# Create the request URL
url = f"https://api-inference.huggingface.co/models/{model_name}"

# Add the API token to the request headers
headers = {"Authorization": f"Bearer {api_token}"}

# Send the request
# Send the request
response = requests.post(url, headers=headers, data={
                         "text": "good is bad ."})
# Get the response data
data = response.json()

# Print the results
print(data)
