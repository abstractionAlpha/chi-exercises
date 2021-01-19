import chi
from chi.network import *
import os
import json

# Before doing anything, we must set some constants to be used in this exercise.

# Configure project and site...
chi.set('project_name', 'CH-822154') # Set to your project name
chi.set('region_name', 'CHI@UC') # Optional - defaults to CHI@UC

# Define keypair name...
key_name = 'my_chameleon_key' # Change to your keypair name

# Get a list of networks within your project
subnets = list_subnets()

print(json.dumps(subnets, indent=2))
