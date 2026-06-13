# Similar to view in WSGI. It handles websocket connection to accept read and send realtime data
# This is from server side 

import json
from channels.generic.websocket import WebsocketConsumer
# WebsocketConsumer is an synchronous class, but group_send() is an async function. 
# To use async function inside sync class, we are using async_to_sync
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # There are methods like connect for establishing connection, receive for receiving messages and disconnect for disconnecting connection from the client inside WebsocketConsumer
    
    def connect(self):
        self.room_group_name = 'test'
        
        # group_add => adds ws connection to group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            # unique id automatically assigned to each websocket connection created by client
            self.channel_name
        )
        
        # Accept the web socket connection request from the client
        self.accept()
        
        # self.send() sends a ws msg to the connected browser
        # WS can send either text_data or binary data. Here we are send text (JSON), we use text_data
        # json.dumps() converts Python dictionary (or objects) to JSON
        # Dictionary is one type of Python object
        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'You are now connected!'
        # }))
        
    # text_data contains the message sent by the browser
    def receive(self, text_data):
        # json.loads() converts JSON string into Python dictionary
        # json.parse(), used in lobby.html, converts JSON string into JS object
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # group_send() just triggers an event, actual sending of messages in done in chat_message fn
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                # This line automatically calls chat_message fn
                'type':'chat_message',
                'message':message
            }
        )
        
    def chat_message(self, event):
        message = event['message']
        
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
        
        # print('Message:', message)
        
        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))