#!/usr/bin/env python3
from PIL import Image
import os
folder = "imgs"
for filename in os.listdir(folder):
  f=os.path.join(folder, filename)
  if os.path.isfile(f):
    im=Image.open(f).convert('RGB')
    filepath= '\\Users\\abhir\\scripts\\newimgs\\'+filename
    im.rotate(270).resize((128,128))
    im.save(filepath,format="JPEG")
