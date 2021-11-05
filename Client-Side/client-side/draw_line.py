import io
import os
import sys
from PIL import Image, ImageDraw, ExifTags, ImageColor
from paramiko_conn import connection

def detect_lines(photo):

    fill_red='#ff0000'
    line_width=10


    image = Image.open(open(photo,'rb'))
    #stream = io.BytesIO()   
    #image_binary = stream.getvalue()
    imgWidth, imgHeight = image.size  
    draw = ImageDraw.Draw(image)  

    boxes = connection(photo)
    for box in boxes: 
        left = imgWidth * box['Left']
        top = imgHeight * box['Top']
        width = imgWidth * box['Width']
        height = imgHeight * box['Height']
        points = (
            (left,top),
            (left + width, top),
            (left + width, top + height),
            (left , top + height),
            (left, top)
        )
        draw.line(points, fill=fill_red, width=line_width)
    if boxes != []:
        image.show()

        image.save("Output Images/"+photo, format=image.format)

def main():

    photo = sys.argv[1]
    detect_lines(photo)

if __name__ == "__main__":
    main()