import requests

api_url = "https://api.api-ninjas.com/v1/geocoding"
api_key = "PfT1mGwaFpS+Dv/8fk1I3A==NefKEwmCGJUHKPb7"  # Replace with your actual API key

def load_cities_from_api(city_name):
    """Load city data from the API"""
    response = requests.get(api_url, headers={'X-Api-Key': api_key}, params={'city': city_name})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Test the API with a sample city name
city_name = "San Francisco"
city_data = load_cities_from_api(city_name)
if city_data:
    print(f"City data for {city_name}: {city_data}")
else:
    print(f"Failed to fetch data for {city_name}")