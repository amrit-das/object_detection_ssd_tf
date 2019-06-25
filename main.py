
from utils import detector_utils as detector_utils
import tensorflow as tf

# For passing realtime command-line arguments
import datetime
import argparse

=
import cv2

# Variable Declaration
ret = True
im_width,im_height = int(1280/1.5),int(720/1.5)            # Image width,heigh
display,start,space,fps = 1,0,30,0     	# Variable init used in codes like counters,flags etc.
en,ex = 0,0                             # Entry/Exit Counter
font = cv2.FONT_HERSHEY_SIMPLEX         # Font for the displayed text

# Loading Inference Graph  (Frozen Tensorflow Model)
detection_graph, sess = detector_utils.load_inference_graph()  

if __name__ == '__main__':

    # Command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-sth','--scorethreshold',dest='score_thresh',type=float,default=0.5,help='Confidence')
    parser.add_argument('-fps','--fps',dest='fps',type=int,default=1,help='Show FPS on detection/display visualization')
    args = parser.parse_args()

    # Reading Video
    cap = cv2.VideoCapture(0)
    
    # For calculating FPS
    start_time = datetime.datetime.now()
    num_frames = 0

    cv2.namedWindow('Nymble Task')
    try:
        while ret:
            ret, image = cap.read()
            image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_np = cv2.resize(image_np,(im_width,im_height))
            # Object detector and Score Calculator
            boxes, scores = detector_utils.detect_objects(image_np,detection_graph, sess)
            detector_utils.draw_box_on_image(1, args.score_thresh,scores, boxes, im_width, im_height,image_np)

            # Status Display on Screen
            if scores[0]>args.score_thresh:
                cv2.putText(image_np,'Detected',(20,90),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
                #start = 1
                #en = ex+1
                #cnt = -6
            #else:
                #cv2.putText(image_np,'Not Detected',(20,90),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
        

            if start == 1:
                #cnt = 0 if cnt == -1 else cnt+1
                #cv2.putText(image_np,'Entry:'+str(en),(20,90+space),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
                #if cnt==0:
                #   ex = ex+1
                #cv2.putText(image_np,'Exit:'+str(ex),(20,90+2*space),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
                cv2.putText(image_np,'FPS:'+str(int(fps)+1),(20,90+3*space),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
                #cv2.putText(image_np,'Counter:'+str(int(en-ex)),(20,90+4*space),font,0.55,(0,0,255),1,cv2.LDR_SIZE)
                
            # FPS Calculator
            num_frames += 1
            elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
            fps = num_frames / elapsed_time

            detector_utils.draw_fps_on_image("Summary",image_np)
            
            cv2.imshow('Nymble Task',cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                raise cv2.error
    
    except cv2.error:   #Releaseing the code
        cap.release()
        cv2.destroyAllWindows()
        print (".")
print("Done!")
