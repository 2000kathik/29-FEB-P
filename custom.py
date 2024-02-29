import sys

from PIL import Image
# Create an empty list to store Image objects
images = []
# Iterate over command-line arguments (excluding the script name)
for arg in sys.argv[1:]:
# Open each image specified in the command-line arguments
    image = Image.open(arg)
# Append the Image object to the list
    images.append(image)
# Save the animated GIF
images[0].save("costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0)
