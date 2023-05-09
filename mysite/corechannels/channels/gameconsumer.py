import json
from .basegameconsumer import BaseGameConsumer
class GameConsumer(BaseGameConsumer):
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['gamedata']

        await self.channel_layer.group_send(self.roomGroupName, {
            'type': 'game_update',
            'gamedata': data,
        })

    async def game_update(self, event):
        data = event['gamedata']
        await self.send(text_data=json.dumps({
            'gamedata': data,
        }))

    async def chat_message(self, event):
        try:
            message = event['message']
            await self.send(text_data=json.dumps({
                'message': message,
            }))
        except Exception as e:
            print(f"Error in chat_message: {e}")
            raise
