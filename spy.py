import socket
import time
from imutils.video import VideoStream
import imagezmq

raspberry_pi = False

sender = imagezmq.ImageSender()

rpi_name = socket.gethostname()
if raspberry_pi:
    picam = VideoStream(usePiCamera=True).start()
else:
    picam = VideoStream().start()
time.sleep(2.0)

while True:
    image = picam.read()
    sender.send_image(rpi_name, image)
