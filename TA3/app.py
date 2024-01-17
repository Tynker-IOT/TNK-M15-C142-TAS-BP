from flask import Flask, render_template, request, jsonify
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

app = Flask(__name__)

sensorData = {
              "/Temperature" : 0,
              "/Humidity" : 0
              }

mqtt_broker_ip = "broker.emqx.io"  

def on_message(client, userdata, msg):
    global sensorData
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    sensorData[topic] = payload
    print("Mqtt Data: ", msg.payload.decode('utf-8'),  msg.topic)

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker_ip, 1883, 60)
mqtt_client.subscribe("/Temperature")
mqtt_client.subscribe("/Humidity")
mqtt_client.loop_start()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lightControl', methods=['POST'])
def lightControl():
    # Get JSON data from the request
    
    # Access the 'color' key in the JSON data
    
    
    # Check color and set the code variable as color code for the color
    
    



    # Publish the code to the /Light/Get path 
    
    print("/lightControl is called")

@app.route("/getSensorData", methods=['POST'])
def getSensorData():
    return jsonify(sensorData)


if __name__ == '__main__':
    app.run(debug=True)
