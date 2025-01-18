import requests

def get_geolocation(ip_address):
    try:
        # Use the ipapi service for geolocation
        url = f"http://ipapi.co/{ip_address}/json/"
        response = requests.get(url)
        
        # Raise exception if the request was not successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        if "error" in data:
            return f"Error: {data.get('reason', 'Unknown error')}"
        
        # Extract relevant information
        geolocation = {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country_name"),
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "ISP": data.get("org")
        }
        return geolocation
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Example usage
if __name__ == "__main__":
    ip = "8.8.8.8"  # Replace with the desired IP address
    location = get_geolocation(ip)
    print(location)
