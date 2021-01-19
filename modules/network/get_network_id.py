import chi
from chi.network import *
import os

# Before doing anything, we must set some constants to be used in this exercise.

# Configure project and site...
chi.set('project_name', 'CH-822154') # Set to your project name
chi.set('region_name', 'CHI@UC') # Optional - defaults to CHI@UC

# Define keypair name...
key_name = 'my_chameleon_key' # Change to your keypair name

# We will name resources based on our environment username for easy identification
username = os.getenv("USER") # OS username. Can be replaced with any username of choice
network_name = username+'Net'

# Create a network out of provider network physnet1
create_network(network_name, of_controller_ip=None, of_controller_port=None, vswitch_name=None,
                provider='physnet1', port_security_enabled=True)

# Get the ID of the network just created
network_id = get_network_id(network_name)

print(network_id)
