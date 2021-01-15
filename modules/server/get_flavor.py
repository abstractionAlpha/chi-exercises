import chi
from chi.server import *

BLAZAR_TIME_FORMAT = '%Y-%m-%d %H:%M'

# Before doing anything, we must set some constants to be used in this exercise.

# Configure project and site...
chi.set('project_name', 'CH-822154') # Set to your project name
chi.set('region_name', 'CHI@UC') # Optional - defaults to CHI@UC

# Define keypair name...
key_name = 'my_chameleon_key' # Change to your keypair name

# Set constants...
default_flavor = 'baremetal'

# Get a flavor by name.
get_flavor(default_flavor)
