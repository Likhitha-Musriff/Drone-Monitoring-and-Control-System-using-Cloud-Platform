import requests
import random
import time

# Cloud API URL to send data
cloud_api_url = "http://yourcloudapi.com/upload_drone_data"

# Simulate real-time drone sensor data
def get_drone_data():
    gps_coordinates = {
        "latitude": random.uniform(37.7749, 37.8049),  # Simulate latitude
        "longitude": random.uniform(-122.4194, -122.3894)  # Simulate longitude
    }
    battery_level = random.randint(10, 100)  # Simulate battery level
    altitude = random.randint(10, 1000)  # Simulate altitude
    camera_status = random.choice(["on", "off"])  # Simulate camera status

    return {
        "gps_coordinates": gps_coordinates,
        "battery_level": battery_level,
        "altitude": altitude,
        "camera_status": camera_status
    }

# Function to send data to cloud
def send_to_cloud(drone_data):
    response = requests.post(cloud_api_url, json=drone_data)
    if response.status_code == 200:
        print("Data successfully sent to cloud.")
    else:
        print("Failed to send data to cloud.")

# Real-time monitoring of drone
def real_time_monitoring():
    while True:
        drone_data = get_drone_data()
        print(f"GPS Coordinates: {drone_data['gps_coordinates']}")
        print(f"Battery Level: {drone_data['battery_level']}%")
        print(f"Altitude: {drone_data['altitude']} meters")
        print(f"Camera Status: {drone_data['camera_status']}")

        # Send data to the cloud
        send_to_cloud(drone_data)

        # Wait for 1 second before sending next data
        time.sleep(1)

if __name__ == "__main__":
    real_time_monitoring()
