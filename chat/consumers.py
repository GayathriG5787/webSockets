# Similar to view in WSGI, handles websocket connection to accept read and send realtime data

import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    # There are methods like connect for establishing connection, receive for receiving messages and disconnect for disconnecting connection from the client inside WebsocketConsumer
    
    def connect(self):
        # Accept the web socket connection request from the client
        self.accept()
        
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))