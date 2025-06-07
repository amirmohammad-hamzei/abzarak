import requests


class Data:
    def SongData(self):
        url = "https://radio.beeptunes.com/api/nowplaying?disCache=1730694472238"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            now_playing = data[1].get("now_playing", {}).get("song", {})
            if not now_playing:
                return None

            text = now_playing.get("text", "Unknown")
            artist = now_playing.get("artist", "Unknown Artist")
            title = now_playing.get("title", "Unknown Title")
            art_url = now_playing.get("art", "")
            duration = data[1].get("now_playing", {}).get("duration", "")
            elapsed = data[1].get("now_playing", {}).get("elapsed", "")

            if art_url:
                image_response = requests.get(art_url, timeout=5)
                image_response.raise_for_status()
                file_path = "images/temp_image.jpg"
                with open(file_path, 'wb') as file:
                    file.write(image_response.content)
            else:
                file_path = "icon/font_awesome/solid/image.png"
                print("Error retrieving artwork, using default image.")

            return {
                "text": text,
                "artist": artist,
                "title": title,
                "art": file_path,
                "elapsed": elapsed,
                "duration": duration
            }

        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching song data: {e}")
            return {
                "text": "Error",
                "artist": "N/A",
                "title": "N/A",
                "art": "icon/font_awesome/solid/image.png",
            }

    '''def get_ip_address(self):
        try:
            url = "https://api.ipify.org"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            ip = response.text
            print(ip)
            return ip
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching IP address: {e}")
            return {"ip": "N/A"}'''

    def get_time(self):
        url = "https://api.keybit.ir/time"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            deta = response.json()

            if not deta.get("date"):
                raise ValueError("Invalid response structure: missing 'date' key")

            timestamp = deta.get("timestamp", {}).get("en", {})
            weekdays = deta.get("date", {}).get("weekday", {}).get("name", {})
            date = deta.get("date", {}).get("full", {}).get("official", {}).get("usual", {}).get("en", {})
            day_events = deta.get("date", {}).get("day", {}).get("events", {})

            if day_events is None:
                day_events = {}

            day_local = day_events.get("local")
            day_holy = day_events.get("holy")
            day_global = day_events.get("global")

            day_local = day_local.get("text", "N/A") if day_local else ""
            day_holy = day_holy.get("text", "N/A") if day_holy else ""
            day_global = day_global.get("text", "N/A") if day_global else ""

            day = day_local + day_global + day_holy

            return {
                "timestamp": timestamp,
                "weekdays": weekdays,
                "date": date,
                "day": day,

            }

        except(requests.RequestException, ValueError) as e:
            print(f"Error fetching time data: {e}")
            return {
                "timestamp": "N/A",
                "weekdays": "N/A",
                "date": "N/A",
                "day": "N/A",
            }

    def weather(self, city):

        url = "http://api.weatherapi.com/v1/forecast.json"
        params = {
            "key": "a21ba69431ea4eca98364014241211",
            "q": f"{city}",
            "days": 3,
            "aqi": "no",
            "alerts": "no"
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()

            location = data.get('location', {})
            name = location.get('name', {})
            region = location.get('region', {})

            current = data.get("current", {})
            temp_c = current.get("temp_c", {})
            condition = current.get("condition", {})
            text = condition.get("text", {})
            icon = "http:" + condition.get("icon", "")

            forecast = data.get("forecast", {})
            forecast_day_0 = forecast.get("forecastday", [])[0]
            day_0_condition = forecast_day_0.get("day", {})
            day_0_maxtemp_c = day_0_condition.get("maxtemp_c", {})
            day_0_condition_text = day_0_condition.get("condition", {}).get("text", "N/A")
            day_0_condition_icon = "http:" + day_0_condition.get("condition", {}).get("icon", "N/A")

            forecast_day_1 = forecast.get("forecastday", [])[1]
            day_1_condition = forecast_day_1.get("day", {})
            day_1_maxtemp_c = day_1_condition.get("maxtemp_c", {})
            day_1_condition_text = day_1_condition.get("condition", {}).get("text", "N/A")
            day_1_condition_icon = "http:" + day_1_condition.get("condition", {}).get("icon", "N/A")

            forecast_day_2 = forecast.get("forecastday", [])[2]
            day_2_condition = forecast_day_2.get("day", {})
            day_2_maxtemp_c = day_2_condition.get("maxtemp_c", {})
            day_2_condition_text = day_2_condition.get("condition", {}).get("text", "N/A")
            day_2_condition_icon = "http:" + day_2_condition.get("condition", {}).get("icon", "N/A")

            image_response = requests.get(icon, timeout=5)
            image_response.raise_for_status()
            icon_path = "images/icon_image.png"
            with open(icon_path, 'wb') as file:
                file.write(image_response.content)

            image_response_0 = requests.get(day_0_condition_icon, timeout=5)
            image_response_0.raise_for_status()
            icon_path_0 = "images/icon_image_0.png"
            with open(icon_path_0, 'wb') as file_0:
                file_0.write(image_response_0.content)

            image_response_1 = requests.get(day_1_condition_icon, timeout=5)
            image_response_1.raise_for_status()
            icon_path_1 = "images/icon_image_1.png"
            with open(icon_path_1, 'wb') as file_1:
                file_1.write(image_response_1.content)

            image_response_2 = requests.get(day_2_condition_icon, timeout=5)
            image_response_2.raise_for_status()
            icon_path_2 = "images/icon_image_2.png"
            with open(icon_path_2, 'wb') as file_2:
                file_2.write(image_response_2.content)

            return {
                "name": name,
                "region": region,
                "temp_c": str(temp_c),
                "text": text,
                "icon": icon_path,
                "day_0_maxtemp_c": str(day_0_maxtemp_c),
                "day_0_condition_text": day_0_condition_text,
                "day_0_condition_icon": icon_path_0,
                "day_1_maxtemp_c": str(day_1_maxtemp_c),
                "day_1_condition_text": day_1_condition_text,
                "day_1_condition_icon": icon_path_1,
                "day_2_maxtemp_c": str(day_2_maxtemp_c),
                "day_2_condition_text": day_2_condition_text,
                "day_2_condition_icon": icon_path_2,
            }

        else:
            print(f"Error: {response.status_code}")

# Example usage:
# data = Data().weather("yazd")
# print(data)
# print(f"Weather in {data['name']}, {data['region']}: {data['temp_c']}°C")
# print(f"Current weather: {data['text']}")
# print(f"Icon: {data['icon']}")
# print(f"Day 0: Max temperature: {data['day_0_maxtemp_c']}°C, Condition: {data['day_0_condition_text']}")
# print(f"Day 1: Max temperature: {data['day_1_maxtemp_c']}°C, Condition: {data['day_1_condition_text']}")
# print(f"Day 2: Max temperature: {data['day_2_maxtemp_c']}°C, Condition: {data['day_2_condition_text']}")
