import paho.mqtt.client as mqtt
import json
from SensorData import SensorData
import mysql.connector as mysql

## mqtt psw: NNSXS.DTT4HTNBXEQDZ4QYU6SG73Q2OXCERCZ6574RVXI.CQE6IG6FYNJOO2MOFMXZVWZE4GXTCC2YXNQNFDLQL4APZMWU6ZGA
## mqtt username: project-software-engineering@ttn


## DB query template
mySql_insert_query = """INSERT INTO transaction (city,date,temperature,light,pressure,humidity) 
                           VALUES 
                           (%s,%s,%s,%s,%s,%s)"""


connection = mysql.connect(host="localhost",
                           database="weather-db",
                           user="root",
                           password="Lololo123")


def mqtt_aunth():
    """
    @brief Function to ask username and password to establish a connection in mqtt protocol.
    """
    print('Enter MQTT username:')
    username = input()
    print('Enter MQTT psw:')
    password = input()
    client.username_pw_set(username=username, password=password)


def on_connect(client, userdata, flags, rc):
    """
    @brief The callback for when the client receives a CONNACK response from the server.
    @param client: the client instance for this callback
    @param userdata: the private user data as set in Client() or user_data_set()
    @param flags: response flags sent by the broker
    @param rc: rc (return code) is used for checking that the connection was established. (see below).
    """
    print("Connected with result code " + str(rc))
    ## Subscribe the client to one or more topics.
    client.subscribe("#")


def on_message(client, userdata, msg):
    """
    @brief The callback for when a PUBLISH message is received from the server.
    @param client: the client instance for this callback
    @param userdata: the private user data as set in Client() or user_data_set()
    @param msg: message received by mqtt protocol
    """
    ## Data is SensorData class object
    data = SensorData()
    ## converting to json format
    to_string = json.loads(msg.payload)
    print(to_string)
    ## calling SensorData member function for parsing data and assigning class variables
    data.parse(to_string)
    ##  array with SensorData variables, previusly assigned dy parse() function.
    db_values = (data.device_id, data.datetime, data.temperature, data.light, data.pressure, data.humidity)
    ## cursor is Mysql object to manipulate with DB
    cursor = connection.cursor()
    ## pushing to db
    cursor.execute(mySql_insert_query, db_values)
    ## destroying SensorClass object
    del data
    ## sends a commit statement to the MySQL server, committing the current transaction.
    connection.commit()
    ## Closing cursor.
    cursor.close()


## creating mqtt client object
client = mqtt.Client()
## Define the connect callback implementation.
client.on_connect = on_connect
## Define the message callback implementation.
client.on_message = on_message
## user/passwd ask function.
mqtt_aunth()
## Establish mqtt connection.
client.connect("eu1.cloud.thethings.network", 1883, 60)
## endless loop
client.loop_forever()
