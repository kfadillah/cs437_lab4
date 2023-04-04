import logging
import platform
import sys
from threading import Timer
import json

import greengrasssdk

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

max_emission = [0,0,0,0,0]

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    
    global max_emission
    
    logger.info(event)
    
    try:
        vid = int(str(event['vid']))
        data = float(str(event['data']))
        max_emission[vid] = max(max_emission[vid], data)
        #publish to cloud
        client.publish(
            topic="emission/all",
            payload=json.dumps(
                {"message": "Emission! , " + str(event['vid']) + " : " + str(event['data']),
                "vehicle0": max_emission[0],
                "vehicle1": max_emission[1],
                "vehicle2": max_emission[2],
                "vehicle3": max_emission[3],
                "vehicle4": max_emission[4]}
            ),
        )
        #publish to device
        client.publish(
            topic="emission/all/vehicle" + str(vid),
            payload=json.dumps({"current max co2 vehicle" + str(vid): max_emission[vid]}),
        )
            
    except Exception as e:
        client.publish(
            topic="emission/all",
            payload=json.dumps(
                {"message": "FAILED: Process Emission! , " + str(event['data']) + " : " + str(event['vid'])},
            ),
        )
    return