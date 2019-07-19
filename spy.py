import socket
import time
from imutils.video import VideoStream
import imagezmq


sender = imagezmq.ImageSender()

rpi_name = socket.gethostname()
picam = VideoStream().start()
time.sleep(2.0)

while True:
    image = picam.read()
    sender.send_image(rpi_name, image)
