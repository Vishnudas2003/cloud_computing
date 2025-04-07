import psutil
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            if partition.fstype != '':  # Skip non-formatted drives
                disk_percent = psutil.disk_usage(partition.mountpoint).percent
                break
        else:
            disk_percent = None
    except Exception:
        disk_percent = None

    net_io = psutil.net_io_counters()
    net_sent = round(net_io.bytes_sent / (1024 * 1024), 2)
    net_recv = round(net_io.bytes_recv / (1024 * 1024), 2)

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = str(now - boot_time).split('.')[0]

    num_processes = len(psutil.pids())

    message = ""
    if cpu_percent > 80 or mem_percent > 80:
        message = "⚠️ High resource usage detected. Please investigate."

    return render_template("index.html",
                           cpu_percent=cpu_percent,
                           mem_percent=mem_percent,
                           disk_percent=disk_percent,
                           net_sent=net_sent,
                           net_recv=net_recv,
                           uptime=uptime,
                           num_processes=num_processes,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
