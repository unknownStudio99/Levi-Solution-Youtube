import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def scrollUp(repeat, deviceIds, ws_url):
    for _ in range(repeat):
        sendExecuteAutox(deviceIds, "Scripts/scrollUp.js", ws_url)

