# hard erase data from a file by overwriting it with all zeros

import os
import sys

def eraseData(filename):
    # open the file
    f = open(filename, "r+b")
    # get the file size
    fsize = os.path.getsize(filename)
    # write zeros to the file
    f.write("\0" * fsize)
    # close the file
    f.close()

if __name__ == "__main__":
    # get the filename from the command line
    filename = sys.argv[1]
    # erase the data
    eraseData(filename)

# The eraseData function opens the file in read and write binary mode, gets the file size, writes zeros to the file, and then closes the file. The main function gets the filename from the command line and calls the eraseData function.
