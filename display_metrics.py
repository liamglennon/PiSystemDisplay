import requests
import time

WINDOWS_IP = "149.157.142.143"  # Replace with your Windows PC's IP
METRICS_URL = f"http://{WINDOWS_IP}:5000/metrics"

GREEN = "\033[92m"
RESET = "\033[0m"

while True:
    try:
        response = requests.get(METRICS_URL, timeout=2)
        if response.status_code == 200:
            data = response.json()
            print(GREEN + f"\nCPU: {data['cpu']}% | Memory: {data['memory']}% | Disk: {data['disk']}%" + RESET)

            print(GREEN + f"Battery: {data['battery_percent']}% | Plugged In: {data['power_plugged']}" + RESET)
        else:
            print(GREEN + "Error fetching data" + RESET)
    except Exception as e:
        print(GREEN + "Connection error: " + str(e) + RESET)

    time.sleep(5)
