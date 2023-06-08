import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User
from .models import Message

class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "groupChatgfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        friends_room = text_data_json["friends_room"]
        username = text_data_json["username"]
        message = text_data_json["message"]

        await self.save_message(friends_room, username, message)

        # Send message to friends_room
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        #Send to WebSocket
        await self.send(text_data=json.dumps({
            'message' : message,
            'username' : username
        }))

    @sync_to_async
    def save_message(self, friends_room, username, message):
        user = User.objects.get(username = username)

        Message.objects.create(friends_room = friends_room, user = user, content = message)