import asyncio
import websockets
import json

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        message = {
            "server_id": 2,
            "application_command": "shutdown_app"
        }
        await websocket.send(json.dumps(message))
        print(f"Sent message: {message}")
        
        # Receive a response (optional)
        # response = await websocket.recv()
        # print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(hello("ws://orin2:8673"))
