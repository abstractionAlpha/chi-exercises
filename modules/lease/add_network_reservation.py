import chi
from chi.lease import *
from datetime import datetime, timedelta
from dateutil import tz
import os

BLAZAR_TIME_FORMAT = '%Y-%m-%d %H:%M'

# Before doing anything, we must set some constants to be used in this exercise.

# Configure project and site...
chi.set('project_name', 'CH-822154') # Set to your project name
chi.set('region_name', 'CHI@UC') # Optional - defaults to CHI@UC

# Define keypair name...
key_name = 'my_chameleon_key' # Change to your keypair name

# We will name resources based on our environment username for easy identification
username = os.getenv("USER") # OS username. Can be replaced with any username of choice
network_name = username+'Net'
lease_name = username+'Lease'

# Set start/end date for lease
# Start one minute into future to avoid Blazar thinking lease is in past due to rounding to closest
# minute.
start_date = (datetime.now(tz=tz.tzutc()) + timedelta(minutes=1)).strftime(BLAZAR_TIME_FORMAT)
end_date   = (datetime.now(tz=tz.tzutc()) + timedelta(days=1)).strftime(BLAZAR_TIME_FORMAT)

# Build list of reservations
# NOTE: For docs you can pick and choose which reservations... Commenting out or removing lines
# will allow for only relevant reservations to be displayed by the json dump
reservation_list = []
chi.lease.add_network_reservation(reservation_list, network_name, of_controller_ip=None, of_controller_port=None, vswitch_name=None, physical_network='physnet1')


# Create the lease
chi.blazar().lease.create(name = lease_name,
                            start = start_date,
                            end = end_date,
                            reservations = reservation_list,
                            events = [])
