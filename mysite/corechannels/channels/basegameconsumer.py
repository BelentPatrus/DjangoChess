import json
from channels.generic.websocket import AsyncWebsocketConsumer


class BaseGameConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.match_id = self.scope['url_route']['kwargs']['match_id']
        self.roomGroupName = 'room_%s' % self.match_id
        await self.channel_layer.group_add(self.roomGroupName, self.channel_name)
        await self.accept()
        # await self.channel_layer.group_send(self.roomGroupName, {
        #     'type': 'tester_message',
        #     'tester': 'hello world',

        # })

    # async def tester_message(self, event):
    #     tester = event['tester']
    #     await self.send(text_data=json.dumps({'tester': tester, }))

    async def disconnect(self, closeCode):
        await self.channel_layer.group_discard(self.roomGroupName, self.channel_name)


