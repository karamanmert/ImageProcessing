#HAREKET HALINDEKI ARAÇ SAYIMI
#araçlar 2 şeritten gidiyor.Eğer aracın ağırlık merkezi bu şeritlerdeyse araç sayısını bir arttıracağız
#YALNIZ KAMERA  SABİT OLMALI..

import cv2

backsub = cv2.createBackgroundSubtractorMOG2()#arkaplanı temizleme (beyazlaştırma)
capture = cv2.VideoCapture("video.avi")#video yakalandı.
i = 0 #araç sayısı tutulacak.
minArea=2600#ağırlık hesabı yapacagımız için her bir aracın ağırlıgının belli bir değer üstünde mi ? kıyaslama için
while True:
    ret, frame = capture.read()
    fgmask = backsub.apply(frame, None, 0.02)#frame e , hassasiyet 0.02
    erode=cv2.erode(fgmask, None,iterations=4) #none= kernel uygulanmasın.
    moments=cv2.moments(erode,True)
    area=moments['m00']
    #yatay ust
    cv2.line(frame,(40,0),(40,176),(255,0,0),2)
    cv2.line(frame, (55, 0), (55, 176), (255, 0, 0), 2)
    #diket ust
    cv2.line(frame,(0,50),(320,50),(255,0,0),2)
    cv2.line(frame, (0, 65), (320, 65), (255, 0, 0), 2)
    #yatay alt
    cv2.line(frame, (100, 0), (100, 176), (0, 255, 255), 2)
    cv2.line(frame, (115, 0), (115, 176), (0, 255, 255), 2)
    # dikey alt
    cv2.line(frame, (0, 105), (320, 105), (0, 255, 255), 2)
    cv2.line(frame, (0, 130), (320, 130), (0, 255, 255), 2)

    if moments['m00'] >=minArea: #ağırlık merkezi minağ. dan buyukse buradan araba geçmiştir
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        print("mom :" + str(moments['m00']) + "x :" + str(x) + " y : " + str(y))
        if x>40 and x<55 and y>50 and y<65:
            i=i+1

            print("ust"+str(i))
        elif x>102 and x<110 and y>105 and y<130:
            i=i+1
            print("alt"+str(i))

    cv2.putText(frame,'Sayi: %r' %i, (200,30), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 2)
    cv2.imshow("frame", frame)
    # cv2.imshow("fgmask", fgmask)

    key = cv2.waitKey(25)
    if key == ord('q'): # q ya basınca programdan cık
            break
capture.release()

cv2.destroyAllWindows()

