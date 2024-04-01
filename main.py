# import requests
# # from PIL import Image
# city = input("Enter The Name of the city :")

# url = f"https://api.weatherapi.com/v1/current.json?key=7f54ab742dec4cd6bad93735240104&q={city}"
# response  = requests.get(url)
# response = response.json()
# # print(response)

# if "location" in response:
#     print(response["location"])
#     print("\t\tWeather Information\t\t")
#     print(f"city name : {response["location"]["name"]}")
#     print(f"Temprature : {response["current"]["temp_c"]C}")    

# if "current" in response:
#     print("Hey")
#     img_url=response["current"]["condition"]["icon"]
#     print(img_url)
#     # img = Image.open()
#     # img.show()


import requests

city = input("Enter the Name of the city: ")  # Capitalize "Name" for clarity

# Replace with your actual API key (https://www.weatherapi.com/)
api_key = "7f54ab742dec4cd6bad93735240104"  # Placeholder for actual key

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Process successful response
    data = response.json()

    if "location" in data:
        # print(data["location"])
        print("\t\tWeather Information\t\t")
        print(f"City Name: {data['location']['name']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Weather Condition: {data['current']['condition']['text']}")

    else:
        print("Error: Location information not found in the response.")

except requests.exceptions.RequestException as e:
    print(f"Error retrieving weather data: {e}")
