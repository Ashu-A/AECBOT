import streamlit as st
import requests
import time
from datetime import datetime
import pytz

# Adafruit IO credentials
ADAFRUIT_AIO_USERNAME = "ashishranjan"
ADAFRUIT_AIO_KEY = "aio_fCQU275jZVpadhJOIG63HHwUXtxR"

# London timezone
london_tz = pytz.timezone('Europe/London')


# Function to fetch last value from Adafruit IO feed
def fetch_last_value(feed_key):
    url = f"https://io.adafruit.com/api/v2/{ADAFRUIT_AIO_USERNAME}/feeds/{feed_key}/data/last"
    headers = {
        "X-AIO-Key": ADAFRUIT_AIO_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        last_value = data['value']
        recorded_at_utc = data['created_at']
        # Convert UTC timestamp to London timezone
        recorded_at = datetime.strptime(recorded_at_utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc).astimezone(
            london_tz)
        recorded_at_str = recorded_at.strftime('%Y-%m-%d %H:%M:%S')
        return last_value, recorded_at_str
    else:
        st.error(f"Failed to fetch data from feed {feed_key}, status code: {response.status_code}")
        return None, None


# Define feed keys and names
feeds = [
    {"name": "humidity", "key": "humidity"},
    {"name": "pressure", "key": "pressure"},
    {"name": "raindrop", "key": "raindrop"},
    {"name": "soil-moisture", "key": "soil-moisture"},
    {"name": "sound", "key": "sound"},
    {"name": "temperature", "key": "temperature"}
]


# Function to periodically update data
def update_data():
    updated_data = []
    for feed in feeds:
        last_value, recorded_at = fetch_last_value(feed['key'])
        updated_data.append({
            "Feed Name": feed['name'],
            "Key": feed['key'],
            "Last value": last_value,
            "Recorded": recorded_at
        })
    return updated_data


# Function to load HTML and CSS files
def load_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Function to generate HTML table rows
def generate_table_rows(data):
    rows_html = ""
    for entry in data:
        rows_html += f"""
            <tr>
                <td>{entry['Feed Name']}</td>
                <td>{entry['Key']}</td>
                <td>{entry['Last value']}</td>
                <td>{entry['Recorded']}</td>
            </tr>
        """
    return rows_html


# Function to generate rain status
def generate_rain_status(raindrop_value):
    if raindrop_value is not None and float(raindrop_value) < 500:
        return '<div id="rain-box" class="rain-box rain-detected">Rain detected</div>'
    else:
        return '<div id="rain-box" class="rain-box no-rain">No rain</div>'


# Function to generate sound status
def generate_sound_status(sound_value):
    if sound_value is not None:
        sound_value = float(sound_value)
        if sound_value < 300:
            return '<div id="sound-box" class="sound-box low-sound">Low sound</div>'
        elif sound_value > 980:
            return '<div id="sound-box" class="sound-box high-sound">High sound</div>'
        else:
            return '<div id="sound-box" class="sound-box normal-sound">Normal sound</div>'
    else:
        return '<div id="sound-box" class="sound-box">No data</div>'


# Function to generate soil moisture status
def generate_soil_moisture_status(moisture_value):
    if moisture_value is not None:
        moisture_value = float(moisture_value)
        if moisture_value > 700:
            return '<div id="soil-box" class="soil-box wet-soil">Lot of water</div>'
        elif moisture_value < 300:
            return '<div id="soil-box" class="soil-box dry-soil">Soil needs water</div>'
        else:
            return '<div id="soil-box" class="soil-box normal-soil">Normal soil moisture</div>'
    else:
        return '<div id="soil-box" class="soil-box">No data</div>'


# Function to display dashboard
def main():
    st.title('Arduino Sensor Data Dashboard')

    # Load HTML and CSS files
    table_html = load_file('dash.html')
    box_html = load_file('dash.html')
    styles_css = load_file('dash.css')
    map_html = load_file('map.html')

    # Create an empty container for the map
    st.markdown(map_html, unsafe_allow_html=True)

    # Create an empty container for the table
    table_container = st.empty()
    # Create an empty container for the rain status
    rain_box_container = st.empty()
    # Create an empty container for the sound status
    sound_box_container = st.empty()
    # Create an empty container for the soil moisture status
    soil_box_container = st.empty()

    # Initial data fetch
    data = update_data()

    # Insert initial data into HTML template
    initial_rows = generate_table_rows(data)
    initial_table = table_html.replace("<!-- Table rows will be dynamically inserted here -->", initial_rows)

    # Extract initial values for rain, sound, and soil moisture
    raindrop_value = next((entry['Last value'] for entry in data if entry['Key'] == 'raindrop'), None)
    sound_value = next((entry['Last value'] for entry in data if entry['Key'] == 'sound'), None)
    soil_moisture_value = next((entry['Last value'] for entry in data if entry['Key'] == 'soil-moisture'), None)

    initial_rain_status = generate_rain_status(raindrop_value)
    initial_sound_status = generate_sound_status(sound_value)
    initial_soil_moisture_status = generate_soil_moisture_status(soil_moisture_value)

    # Display the initial data
    table_container.html(f"<style>{styles_css}</style>{initial_table}")
    rain_box_container.html(f"<style>{styles_css}</style>{initial_rain_status}")
    sound_box_container.html(f"<style>{styles_css}</style>{initial_sound_status}")
    soil_box_container.html(f"<style>{styles_css}</style>{initial_soil_moisture_status}")

    # Periodically update data every 15 seconds
    while True:
        time.sleep(15)
        updated_data = update_data()
        updated_rows = generate_table_rows(updated_data)
        updated_table = table_html.replace("<!-- Table rows will be dynamically inserted here -->", updated_rows)

        # Extract updated values for rain, sound, and soil moisture
        raindrop_value = next((entry['Last value'] for entry in updated_data if entry['Key'] == 'raindrop'), None)
        sound_value = next((entry['Last value'] for entry in updated_data if entry['Key'] == 'sound'), None)
        soil_moisture_value = next((entry['Last value'] for entry in updated_data if entry['Key'] == 'soil-moisture'),
                                   None)

        updated_rain_status = generate_rain_status(raindrop_value)
        updated_sound_status = generate_sound_status(sound_value)
        updated_soil_moisture_status = generate_soil_moisture_status(soil_moisture_value)

        # Update the table, rain status, sound status, and soil moisture status
        table_container.empty()
        table_container.html(f"<style>{styles_css}</style>{updated_table}")

        rain_box_container.empty()
        rain_box_container.html(f"<style>{styles_css}</style>{updated_rain_status}")

        sound_box_container.empty()
        sound_box_container.html(f"<style>{styles_css}</style>{updated_sound_status}")

        soil_box_container.empty()
        soil_box_container.html(f"<style>{styles_css}</style>{updated_soil_moisture_status}")


if __name__ == "__main__":
    main()
