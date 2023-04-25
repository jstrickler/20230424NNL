"""
Check up on ChatGPT
"""
import requests

URL = 'https://www.python.org/'
response = requests.get(URL)

if response.status_code == 200:
    with open('python_home.html', 'wb') as f:
        f.write(response.content)
    print('Python home page downloaded successfully!')
else:
    print('Failed to download Python home page')
