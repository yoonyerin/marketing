
import os
import argparse
from huggingface_hub import hf_hub_download
from ultralytics.utils import plotting
from ultralytics import YOLO
from diffusers import StableDiffusionInpaintPipeline
import numpy as np

from PIL import Image, PngImagePlugin

path = hf_hub_download("Bingsu/adetailer", "face_yolov8n.pt")
model = YOLO(path)

img=Image.open("/home/yerin/code/marketing/face4.jpg")

output = model(img)
print(output[0].boxes.xyxy)
box=output[0].boxes.xyxy[0]
x_range=range(int(box[0]), int(box[2]))
y_range=range(int(box[1]), int(box[3]))

np_img=np.asarray(img)
mask=np.zeros(np_img.shape[0:2])
    
for j in x_range:
    for i in y_range:     
        mask[i][j]=1
        
print(mask)