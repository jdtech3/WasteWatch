import socketio
import eventlet
from io import BytesIO
from enum import Enum

# from inference.dummy_inference import dummy_inference
from inference.inference_loop import load_model, load_file, inference
from db_jetson import DBJetson

# State machine
class ObjectCountingState(Enum):
    WAIT_FOR_OBJ = 0
    WAIT_FOR_NOTHING = 1

# create a Socket.IO server
db = DBJetson()
sio = socketio.Server(async_mode='eventlet', logger=True)
state = ObjectCountingState.WAIT_FOR_OBJ
# n = 1

class_names = load_file('inference/class_names.yaml')
model = load_model('inference/CNN.keras')

recognitions = {}

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)
    recognitions = {}

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    print(recognitions)
    print(max(recognitions, key=recognitions.get))

@sio.on('frame_data')
def on_frame_data(sid, data):
    # i = 1
    # global n

    global state

    # Data is a list of 10 frames (binary JPEG)
    for frame in data:
        stream = BytesIO(frame)
        
        prediction = inference(model, frame, class_names)
        # print(f"Object class: {prediction}") #this gets sent to DB
        
        recognitions[prediction] = recognitions.get(prediction, 0) + 1

        # if state == ObjectCountingState.WAIT_FOR_OBJ and prediction is not None:
        #     db.update_surgery(1, prediction)    # state is record obj
        #     state = ObjectCountingState.WAIT_FOR_NOTHING

        # with open(f"inference/dataset/2/tweezers/{n}-{i}.jpg", "wb") as f:
        #     f.write(stream.getbuffer())
        # i += 1
    # n += 1

    # image = Image.open(stream)
    # inference_loop(image,class_names)


if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)