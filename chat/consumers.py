# Similar to view in WSGI. It handles websocket connection to accept read and send realtime data

import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    # There are methods like connect for establishing connection, receive for receiving messages and disconnect for disconnecting connection from the client inside WebsocketConsumer
    
    def connect(self):
        # Accept the web socket connection request from the client
        self.accept()
        
        # self.send() sends a ws msg to the connected browser
        # WS can send either text_data or binary data. Here we are send text (JSON), we use text_data
        # json.dumps() converts Python dictionary (or objects) to JSON
        # Python dictionary is just a part of python objects
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))