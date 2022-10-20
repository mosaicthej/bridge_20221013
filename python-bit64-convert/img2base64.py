# convert a image to bit64 .txt file

# image from command line
#Open an image file.
# read the image data.
# encode it in base64 using the base64 module in Python.
# save the encoded data to a text file.

# usage: python img2base64.py image_name
# python 3.10

import sys
import os
import struct
import base64

def main():
    # take the name of image from command line
    if len(sys.argv) != 2:
        print("usage: python img2base64.py image_name")
        return
    image_name = sys.argv[1]

    # check if the image exists
    if not os.path.exists(image_name):
        print("image not found")
        return

    # open the image
    with open(image_name, "rb") as f:
        # read the image
        image = f.read()

        # encode the image in base64 using the base64 module in Python
        base64Str = base64.b64encode(image)
        # print(base64Str)

        # write the base64 to a .txt file
        with open(image_name + ".txt", "w") as f:
            f.write(base64Str.decode("utf-8"))
    
    print("done")

if __name__ == "__main__":
    main()