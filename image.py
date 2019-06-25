from utils import detector_utils as detector_utils
import tensorflow as tf
import cv2
im_width,im_height,score_thresh = int(1280/1.5),int(720/1.5),0.5
detection_graph, sess = detector_utils.load_inference_graph()  
image = cv2.imread("image/himym.jpg")

image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_np = cv2.resize(image_np,(im_width,im_height))

boxes, scores = detector_utils.detect_objects(image_np,detection_graph, sess)
#for boxes in boxes:
detector_utils.draw_box_on_image(10,score_thresh,scores, boxes, im_width, im_height,image_np)
cv2.imshow('SSD',cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)

