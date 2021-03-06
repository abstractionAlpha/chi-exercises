import chi
from chi.image import *

# Before doing anything, we must set some constants to be used in this exercise.

# Configure project and site...
chi.set('project_name', 'CH-822154') # Set to your project name
chi.set('region_name', 'CHI@UC') # Optional - defaults to CHI@UC

# Set constants...
default_image = 'CC-CentOS7'

# Define keypair name...
key_name = 'my_chameleon_key' # Change to your keypair name

# Get a list of all of the images under your project
images_list = list_images()

print(images_list)
