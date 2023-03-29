import os

for i in range(1, 7):
    content_file = f"content-00{i}.jpg"
    style_file = f"style-00{i}.jpg"
    output_file = f"strotss-00{i}.png"
    weight = "1.0"
    device = "\"cuda:0\""
    command = f"python3 strotss.py {content_file} {style_file} --weight {weight} --output {output_file} --device {device}"
    os.system(command)

