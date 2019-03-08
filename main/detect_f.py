import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-p", "--prototxt", required=True,
                help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
                help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                             (300, 300), (104.0, 177.0, 123.0))

print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()


#loop
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > args["confidence"]:

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (sx, sy, ex, ey) = box.astype("int")

            text = "{:.2f}%".format(confidence * 100)
            y = sy - 10 if sy - 10 > 10 else sy + 10
            cv2.rectangle(image, (sx, sy), (ex, ey), (0, 0, 255), 2)

            cv2.putText(image, text, (sx, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

cv2.imshow("Output", image)
cv2.waitKey(0)