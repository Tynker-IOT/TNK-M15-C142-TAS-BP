from flask import Flask, render_template, request, jsonify
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

app = Flask(__name__)

sensorData = {
              "/Temperature" : 0,
              "/Humidity" : 0
              }

#  Create a mqtt_broker_ip to hold the broker IP


# Define callback function on_message() for handling incoming MQTT messages with three parameter client, userdata, msg

    # Print the msg and topic
    
    
# Create an MQTT client instance

# Set the callback function for incoming messages

# Connect to the MQTT broker

# Subscribe to the desired MQTT topics


# Start the MQTT loop to listen for incoming messages



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lightControl', methods=['POST'])
def lightControl():
    print("/lightControl is called")

@app.route("/getSensorData", methods=['POST'])
def getSensorData():
    return jsonify(sensorData)


if __name__ == '__main__':
    app.run(debug=True)
