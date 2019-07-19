import socket
import time
from imutils.video import VideoStream
import imagezmq

raspberry_pi = True

sender = imagezmq.ImageSender(connect_to="tcp://192.168.8.1:5555")

rpi_name = socket.gethostname()
if raspberry_pi:
    picam = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
else:
    picam = VideoStream().start()
time.sleep(2.0)

while True:
    image = picam.read()
    sender.send_image(rpi_name, image)
