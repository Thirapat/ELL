import sys
import os
import numpy as np
import cv2

import findEll
import modelHelper as mh
import darknetReference as model

def main():
    # python somehow needs to know about the data vector type, so we provide it
    buffer = model.FloatVector(224*224*3)
    results = model.FloatVector(1000)

    camera = 0
    if (len(sys.argv) > 1):
        camera = int(sys.argv[1]) 

    # Start video capture device
    cap = cv2.VideoCapture(camera)

    # Pick the model you want to work with
    helper = mh.ModelHelper("darknetReference", ["darknet.cfg", "darknet.weights"], "darknetImageNetLabels.txt")

    while (True):
        # grab a frame
        ret, frame = cap.read()

        # Prepare the image to send to the model.
        # This involves scaling to the required input dimension and re-ordering from BGR to RGB
        data = helper.prepare_image_for_predictor(frame)

        # Get the compiled model to classify the image, by returning a list of probabilities for the classes it can detect
        model.darknet_reference(data, results)

        # Get the (at most) top 5 predictions that meet our threshold. This is returned as a list of tuples,
        # each with the text label and the prediction score.
        top5 = helper.get_top_n(results, 5)

        # Turn the top5 into a text string to display
        text = "".join([str(element[0]) + "(" + str(int(100*element[1])) + "%)  " for element in top5])
        print(text)

        # Draw the text on the frame
        frameToShow = frame
        helper.draw_label(frameToShow, text)

        # Show the new frame
        cv2.imshow('frame', frameToShow)

        # Wait for Esc key
        if cv2.waitKey(1) & 0xFF == 27:
            break

if __name__ == "__main__":
    main()