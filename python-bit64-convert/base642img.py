# take a base64 string from a .txt file and convert it to an image
# usage: python base642img.py image_name.txt

import sys
import os
import struct
import base64

def main():
    # take the name of image from command line
    if len(sys.argv) != 2:
        print("usage: python base642img.py image_name.txt")
        return
    image_name = sys.argv[1]

    # check if the image exists
    if not os.path.exists(image_name):
        print("image not found")
        return

    # open the image
    with open(image_name, "r") as f:
        # read the image
        base64Str = f.read()

        # decode the base64 string
        image = base64.b64decode(base64Str)

        # write the image to a file
        with open(image_name + ".jpg", "wb") as f:
            f.write(image)
    
    print("done")

if __name__ == "__main__":
    main()