import asyncio
import websockets
import json
import logging
import random

# Enable debugging
logging.basicConfig(level=logging.DEBUG)

async def send_coordinates(uri, screen_x, screen_y):
    try:
        async with websockets.connect(uri) as websocket:
            try:
                while True:
                    await websocket.send(json.dumps({"x": screen_x, "y": screen_y}))
                    response = await websocket.recv()
                    print(response)

                    # Update coordinates (replace with your eye-tracking logic)
                    screen_x, screen_y = get_eye_tracking_coordinates()

                    # Simulate a delay between coordinate updates (adjust as necessary)
                    await asyncio.sleep(1)
            except websockets.exceptions.ConnectionClosedError as e:
                print(f"Connection closed unexpectedly: {e}")
                # Implement reconnection logic if necessary
            except Exception as e:
                print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Failed to connect to WebSocket server: {e}")

def get_eye_tracking_coordinates():
    """
    Simulate getting eye-tracking coordinates.
    Replace this function with actual eye-tracking logic.
    """
    screen_x = random.randint(0, 1920)
    screen_y = random.randint(0, 1080)
    return screen_x, screen_y

async def main():
    uri = "ws://localhost:8000"  # Ensure this matches the server port

    # Initial coordinates (can be set to starting position or initial values)
    screen_x, screen_y = get_eye_tracking_coordinates()

    while True:
        await send_coordinates(uri, screen_x, screen_y)
        # Wait before attempting to reconnect
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
