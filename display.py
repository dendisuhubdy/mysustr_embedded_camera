import cv2
import imagezmq
import redis
import pickle
import base64
from io import BytesIO
from PIL import Image

def main():
    image_stream = imagezmq.ImageHub()
    
    redis_image = redis.StrictRedis(host="localhost", port=6379, db=0)

    while True:
        rpi_name, image = image_stream.recv_image()
        pil_img = Image.fromarray(image)
        buff = BytesIO()
        pil_img.save(buff, format="JPEG")
        new_image_string = base64.b64encode(buff.getvalue())
        print(new_image_string)
        redis_image.set("image", new_image_string)
        cv2.imshow(rpi_name, image) # 1 window for each RPi
        cv2.waitKey(1)
        del buff
        image_stream.send_reply(b'OK')

if __name__ == "__main__":
    main()
