import cv2
def track():
    lh=cv2.getTrackbarPos("LH","Setter")
    ls=cv2.getTrackbarPos("LS","Setter")
    lv=cv2.getTrackbarPos("LV","Setter")
    uh=cv2.getTrackbarPos("UH","Setter")
    us=cv2.getTrackbarPos("US","Setter")
    uv=cv2.getTrackbarPos("UV","Setter")

    return lh,ls,lv,uh,us,uv
