import cv2
import random
import time
import dropbox
start_time = time.time()

def TakeSnapshot():
    number = random.randint(0,10)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imagename = "img" + str(number) + ".png"
        cv2.imwrite(imagename,frame)
        start_time = time.time
        result = False
        return imagename
    videocaptureobject.release()
    cv2.destroyAllWindows()
    

def uploadimage(imagename):
    accessToken = "sl.A2fMauRu8kScrhdr54Ah-NyU2eybTfidRpWkpcZe9R3nGx0GgzZSV-s0HcTfR393Uil0okkPSMxksoUt1OJzZ8qV7zwEl2uiG_QuhKAsWu5s8r8RMw917IGoQLHoStgjiYAassg"
    file = imagename
    file_from = file
    file_to = "samclass102folder/" + imagename
    dbx = dropbox.Dropbox(accessToken)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def mainfunction():
    while(True):
        if((time.time()-start_time)>=300):
            name = TakeSnapshot()
            uploadimage(name)

mainfunction()
