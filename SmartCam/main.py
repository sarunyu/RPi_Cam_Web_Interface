import json
import Adafruit_DHT
import time
#import cronus.beat as beat
#from cronus.timeout import timeout, TimeoutError
import time
import datetime
from influxdb import InfluxDBClient


def send_data():
  humidity, temperature = Adafruit_DHT.read_retry(22, 27)
  if humidity is not None and temperature is not None and humidity < 100 :
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity ))

#    data = {}
#    data['measurement'] = 'temp'
#    data['tags'] = {"host": "pi1"}
#    data['fields'] = {"value": 99};
#    json_data = json.loads(data)
    json_data = [
  {
    "measurement": "Temperature",
    "tags": {
      "host": "pi1"
    },
    "fields": {
      "value":temperature
    }
  },
  {
    "measurement": "Humidity",
    "tags": {
      "host": "pi1"
    },
    "fields": {
      "value": humidity
    }
  }
]


    client = InfluxDBClient('localhost', 8086, '', '', 'data')
    client.write_points(json_data)


    file = open("/var/www/html/FIFO","w")
    file.write('an  T = {0:0.1f}  H = {1:0.1f}%       %D/%M/%Y_%h:%m:%s '.format(temperature, humidity ))
    file.close()
    return(0)

  else:
    print('Failed to get reading. Try again!')

def setup():
   list_cmd  = ['um 3 SendLine.sh','ab 1','an Starting...']
   time.sleep(3)
   for cmd in list_cmd:
     print(cmd)
     file = open("/var/www/html/FIFO","w")
     file.write(cmd)
     file.close()
     time.sleep(1)

if __name__ == "__main__":
    setup()
    time.sleep(1)
    while True:
      send_data()
      time.sleep(10)
