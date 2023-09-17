import socketio
import eventlet
from io import BytesIO
from inference.dummy_inference import dummy_inference
#from inference.inference_loop import inference_loop, preprocess

# create a Socket.IO server
sio = socketio.Server(async_mode='eventlet', logger=True)
n = 1

@sio.on('frame_data')
def on_frame_data(sid, data):
    i = 1
    global n
    for frame in data:
        stream = BytesIO(frame)
        with open(f"inference/training/tweezers/{n}-{i}.jpg", "wb") as f:
            f.write(stream.getbuffer())
        i += 1
    n += 1
    # image = Image.open(stream)
    # inference_loop(image,class_names)


if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)