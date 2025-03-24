from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    try:
        temp = psutil.sensors_temperatures()
        cpu_temp = temp['coretemp'][0].current if 'coretemp' in temp else None
    except:
        cpu_temp = None

    try:
        fans = psutil.sensors_fans()
        fan_speed = fans['cpu_fan'][0].current if 'cpu_fan' in fans else None
    except:
        fan_speed = None

    try:
        battery = psutil.sensors_battery()
        power_plugged = battery.power_plugged if battery else None
        battery_percent = battery.percent if battery else None
    except:
        power_plugged = None
        battery_percent = None

    return jsonify({
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
        "cpu_temp": cpu_temp,
        "fan_speed": fan_speed,
        "power_plugged": power_plugged,
        "battery_percent": battery_percent
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
