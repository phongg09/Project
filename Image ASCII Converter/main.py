from PIL import Image
import subprocess


def replace_pixels(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert('L')

    ascii_chars = '@%X=*+-. '  # Dark -> Bright

    ascii_art = ""

    height, width = img.size
    for y in range(0, width):
        for x in range(0, height):
            brightness = img.getpixel((x, y))
            ascii_art += ascii_chars[int(brightness / 255 * (len(ascii_chars) - 1))]
        ascii_art += "\n"

    with open(output_path, 'w') as f:
        f.write(ascii_art)


# Change input path for different pictures
# Best for low-res portraits
input_image_path = 'MonaLisa.jpg'
output_text_path = 'output_pic.txt'
replace_pixels(input_image_path, output_text_path)
subprocess.Popen(['notepad.exe', output_text_path])
