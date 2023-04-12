import cv2
import time
from keras.models import load_model
import numpy as np


def get_prediction():
    
    # loading the model
    model = load_model('keras_model.h5')
    
    # creating webcam instance
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # hashmap for output 
    hashmap = {0: "rock", 1: "paper", 2: "scissors", 3: "nothing"}
    
    # countdown limit
    timeout = 4
    time_start = time.time()
    while time.time() <= time_start + timeout:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        #print(prediction)
        ctd = (str((time_start + timeout) - time.time()))[:4]
        #print(ctd)
        cv2.putText(frame, ctd, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.imshow('frame', frame)
        # Press q to close the window
        index = np.argmax(prediction[0])
        #print(index)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return hashmap[index]
    print(f"you chose {hashmap[index]}")
          
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return hashmap[index]  

