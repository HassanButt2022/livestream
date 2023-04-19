import websockets
import asyncio
import json 

import cv2, base64

port = 8055
print("Started server on port : ", port)

async def transmit(websocket, path):
    print("Client Connected !")
    try :
        cap = cv2.VideoCapture("/Users/hassanrauf/Desktop/livestream/movie.mp4")

        while cap.isOpened():
            # minutes = 0
            # seconds = 28
            # fps = cap.get(cv2.CAP_PROP_FPS)
            # frame_id = int(fps*(minutes*60 + seconds))
            # cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
            _, frame = cap.read()          
            encoded = cv2.imencode('.png', frame)[1]
            data = str(base64.b64encode(encoded))
            data = data[2:len(data)-1]
        
            await websocket.send(data)
        
            
        cap.release()
    except websockets.connection.ConnectionClosed as e:
        print("Client Disconnected !")
        cap.release()
    except:
        print("Someting went Wrong !")

start_server = websockets.serve(transmit, host="192.168.0.121" , port=port)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()