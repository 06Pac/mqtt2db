import json


class SensorData:
    """
        Documentation for a SensorData class.
    """

    def __init__(self):
        """
            @brief Class has 6 variables
            @var device_id: represents City where sensor is located and type of the sensor.
            @var temperature: represents detected temperature.
            @var light: represents amount of light measured by sensor.
            @var pressure: represents current pressure level.
            @var humidity: represents current humidity level.
            @var datetime: represents current timestamp.
        """
        self.device_id = None
        self.temperature = None
        self.light = None
        self.pressure = None
        self.humidity = None
        self.datetime = None
        self.battery_voltage = None
        self.battery_status = None
        self.latitude = None
        self.longitude = None

    def weather_data_parse(self, msg_string):
        """
            @brief Function for parsing data and assigning class variables.
            @param msg_string: takes string of data in json format.
        """
        self.device_id = msg_string['end_device_ids']['device_id']
        if self.device_id == 'py-saxion':
            self.temperature = msg_string['uplink_message']['decoded_payload']['temperature']
            self.light = msg_string['uplink_message']['decoded_payload']['light']
            self.pressure = msg_string['uplink_message']['decoded_payload']['pressure']
            self.humidity = None
            self.datetime = msg_string['uplink_message']['rx_metadata'][0]['time']
            self.battery_status = None
            self.battery_voltage = None
            self.latitude = msg_string['uplink_message']['rx_metadata'][0]['location']['latitude']
            self.longitude = msg_string['uplink_message']['rx_metadata'][0]['location']['longitude']
        elif self.device_id == 'lht-wierden' or self.device_id == 'lht-gronau':
            self.temperature = msg_string['uplink_message']['decoded_payload']['TempC_SHT']
            self.humidity = msg_string['uplink_message']['decoded_payload']['Hum_SHT']
            self.light = None
            self.pressure = None
            self.datetime = msg_string['uplink_message']['rx_metadata'][0]['time']
            self.battery_status = msg_string['uplink_message']['decoded_payload']['Bat_status']
            self.battery_voltage = msg_string['uplink_message']['decoded_payload']['BatV']
            self.latitude = msg_string['uplink_message']['rx_metadata'][0]['location']['latitude']
            self.longitude = msg_string['uplink_message']['rx_metadata'][0]['location']['longitude']
        elif self.device_id == 'lht-saxion':
            self.temperature = msg_string['uplink_message']['decoded_payload']['TempC_SHT']
            self.humidity = msg_string['uplink_message']['decoded_payload']['Hum_SHT']
            self.light = None
            self.pressure = None
            self.datetime = msg_string['uplink_message']['rx_metadata'][0]['time']
            self.battery_status = msg_string['uplink_message']['decoded_payload']['Bat_status']
            self.battery_voltage = msg_string['uplink_message']['decoded_payload']['BatV']
            self.latitude = msg_string['uplink_message']['rx_metadata'][0]['location']['latitude']
            self.longitude = msg_string['uplink_message']['rx_metadata'][0]['location']['longitude']
        elif self.device_id == 'py-wierden':
            self.temperature = msg_string['uplink_message']['decoded_payload']['temperature']
            self.light = msg_string['uplink_message']['decoded_payload']['light']
            self.pressure = msg_string['uplink_message']['decoded_payload']['pressure']
            self.humidity = None
            self.datetime = msg_string['uplink_message']['rx_metadata'][0]['time']
            self.battery_status = msg_string['uplink_message']['decoded_payload']['Bat_status']
            self.battery_voltage = msg_string['uplink_message']['decoded_payload']['BatV']
            self.latitude = msg_string['uplink_message']['rx_metadata'][0]['location']['latitude']
            self.longitude = msg_string['uplink_message']['rx_metadata'][0]['location']['longitude']
