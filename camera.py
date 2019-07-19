import cv2
import imagezmq


image_stream = imagezmq.ImageHub()

while True:
    rpi_name, image = image_stream.recv_image()
    cv2.imshow(rpi_name, image) # 1 window for each RPi
    cv2.waitKey(1)
    image_stream.send_reply(b'OK')
