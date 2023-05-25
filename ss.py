import requests

# Get your API token from https://huggingface.co/settings/tokens
api_token = "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"

# Set the model name
model_name = "sentence-transformers/all-MiniLM-L6-v2"

# Create the request URL
api_url = f"https://api-inference.huggingface.co/models/{model_name}"

# Add the API token to the request headers
headers = {"Authorization": f"Bearer {api_token}"}

# Prepare input data
data = {
    'inputs': {
        'source_sentence': 'India is great.',
        'sentences': ['Tajmahal in India', 'India has 32 states', 'All players are tired']
    }
}

# Make API request
response = requests.post(api_url, headers=headers, json=data)

# Process the response
result = response.json()
print(result)
# similarity_scores = result['scores']

# Print the similarity scores
for i, score in enumerate(result):
    print(f'Similarity Score for Sentence {i+1}: {score}')
