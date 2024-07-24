import asyncio
from websocket_client import send_coordinates

uri = "ws://your.websocket.server"
screen_x = 100
screen_y = 200

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_coordinates(uri, screen_x, screen_y))
