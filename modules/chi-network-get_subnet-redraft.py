import chi
from chi.network import *

# Params : subnet name or ID
# Return : subnet dict
def get_subnet(ref):
    subnets = list_subnets()
    subnet = None

    ref_list = ref.split("-")

    if len(ref_list) == 5 and len(ref_list[0]) == 8 and len(ref_list[1]) == 4 and len(ref_list[2]) == 4 and len(ref_list[3]) == 4 and len(ref_list[4]) == 12:
        reftype = 'id'
    else:
        reftype = 'name'

    for i in subnets:
        if i['name'] == ref:
            image = i
            break
        if i['id'] == ref:
            image = i
            break

    if subnet == None:
        if reftype == 'name':
            print('Subnet with name ' + ref + ' not found.')
        if reftype == 'id':
            print('Subnet with ID ' + ref + ' not found.')
    else:
        return subnet
