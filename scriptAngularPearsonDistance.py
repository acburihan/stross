import os

images = int(input("How many images as input? Name the files content001.jpg, style001.jpg, etc. "))
weight = float(input("What weight? Default is 1.0:"))
device = int(input("What device? 0 for MPS, 1 for CUDA: "))


for i in range(1, images):
    content_file = f"content{i:03d}.jpg"
    style_file = f"style{i:03d}.png"
    output_file = f"angularp{i:03d}.png"
    weight = f"{weight:.1f}"
    if device == 1:
        device = "\"cuda:0\""
    else:
        device = "\"mps:0\""
    command = f"python3 strotssAngularPearsonDistance.py {content_file} {style_file} --weight {weight} --output {output_file} --device {device}"
    os.system(command)

