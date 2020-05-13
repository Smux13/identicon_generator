"""
Identicon generator

Generates a randomized image.

Based on the ASCII code of the characters in the hash of the username.
If the code is even, puts a pixel on the image.
The color is got from the first 3 characters' ASCII code of the hash.
"""

from hashlib import sha256 as hsh
import sys
from PIL import Image

def generate(username):
    """
    Generates an identicon, based on the hash of the username (or other passed string).
    """

    usernameHash = hsh(username.encode()).hexdigest()


    img = Image.new("RGB", (8, 8), "white")
    pixels = img.load()

    color = (ord(usernameHash[0])*2, ord(usernameHash[1])*2, ord(usernameHash[2])*2)

    for i, char in enumerate(usernameHash):
        if not ord(char)%2:
            pixels[i%8, int(i/8)] = color

    img = img.resize((256, 256))
    img.save("generated/"+username+".png")
    img.show()


if __name__ == "__main__": # if executed as a script
    try:
        ARGUMENT = sys.argv[1]
    except IndexError:
        sys.stderr.write("Usage: "+sys.argv[0]+" username\n\n"
                         "or you can use this script as a python3 module like so:\n"
                         "from identicon_generator import generate\n"
                         "generate(\"username\")")
        sys.exit(1)

    generate(ARGUMENT)
