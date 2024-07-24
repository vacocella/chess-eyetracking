import asyncio
import websockets
import json
import logging

# Enable debugging
logging.basicConfig(level=logging.DEBUG)

async def send_coordinates(uri, screen_x, screen_y):
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"x": screen_x, "y": screen_y}))
            response = await websocket.recv()
            print(response)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")
        # Implement reconnection logic if necessary
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    uri = "ws://localhost:8000"  # Replace with the port your WebSocket server is using
    screen_x = 100  # Replace with actual X coordinate
    screen_y = 200  # Replace with actual Y coordinate

    asyncio.get_event_loop().run_until_complete(send_coordinates(uri, screen_x, screen_y))
