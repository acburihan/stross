import os

images = 7


for i in range(1, images):
    content_file = f"content{i:03d}.jpg"
    style_file = f"style{i:03d}.jpg"
    output_file = f"angular{i:03d}.png"
    weight = "1.0"
    # device = "\"mps:0\""
    device = "\"cuda:0\""
    command = f"python3 strotssAngularPearsonDistance.py {content_file} {style_file} --weight {weight} --output {output_file} --device {device}"
    os.system(command)

