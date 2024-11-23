import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def scrollDown(repeat, deviceIds, ws_url):
    for _ in range(repeat):
        sendExecuteAutox(deviceIds, "Scripts/scrollDown.js", ws_url)

