import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.match_id = self.scope['url_route']['kwargs']['match_id']
        self.roomGroupName = 'room_%s' % self.match_id
        await self.channel_layer.group_add(self.roomGroupName, self.channel_name)
        await self.accept()
        await self.channel_layer.group_send(self.roomGroupName,{
            'type': 'tester_message',
            'tester' : 'hello world',

        })
    
    async def tester_message(self,event):
        tester = event['tester']
        await self.send(text_data=json.dumps({'tester' : tester,}))
    
    async def disconnect(self, closeCode):
        await self.channel_layer.group_discard(self.roomGroupName, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(self.roomGroupName, {
            'type' : 'chat_message',
            'message' : message,
        })
    async def chat_message(self,event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message' : message,
        }))
