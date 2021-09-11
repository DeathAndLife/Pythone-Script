import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image
import ToFile


def get_ewm(img_adds):
    if os.path.isfile(img_adds):
        img = Image.open(img_adds)
    else:
        rq_img = requests.get(img_adds).content
        img = Image.open(BytesIO(rq_img))

    txt_list = pyzbar.decode(img)

    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        ToFile.txt('result', barcodeData + "\n")
        print(barcodeData)

    os.remove(img_adds)
