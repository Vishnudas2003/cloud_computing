import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index(): 
    cpu_percent = psutil.cpu_percent()  # Call the function here
    mem_percent = psutil.virtual_memory().percent
    message = ""

    if cpu_percent > 80 or mem_percent > 80:
        message = "⚠️ CPU utilization high, please scale up!!!"

    return f"""
        <h2>Cpu Utilization: {cpu_percent}%</h2>
        <h2>Memory Utilization: {mem_percent}%</h2>
        <p>{message}</p>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
