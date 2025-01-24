import requests
import dotenv
import os

dotenv.load_dotenv()

api_token = os.environ['AIRQ_API_TOKEN']

url = 'http://api.waqi.info/feed/#city#/?token=#token#'

requests_url = url.replace('#token#', api_token)
requests_url = requests_url.replace('#city#', 'Bangkok')
print(requests_url)

response = requests.get(requests_url)
json_data = response.json()['data']

print(f'{json_data['city']['name']} has current ollution level: {json_data['aqi']}')

# End of file
