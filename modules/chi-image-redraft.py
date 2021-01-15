# Return : list of image dictionaries
def list_images_temp():
    return list(chi.glance().images.list())

# Params : image name or ID
# Return : image dict
def get_image_temp(ref):
    images_list = list_images_temp()

    image = None

    ref_list = ref.split("-")

    if len(ref_list) == 5 and len(ref_list[0]) == 8 and len(ref_list[1]) == 4 and len(ref_list[2]) == 4 and len(ref_list[3]) == 4 and len(ref_list[4]) == 12:
        reftype = 'id'
    else:
        reftype = 'name'

    for i in images_list:
        if i['name'] == ref:
            image = i
            break
        if i['id'] == ref:
            image = i
            break

    if image == None:
        if reftype == 'name':
            print('Image with name ' + ref + ' not found.')
        if reftype == 'id':
            print('Image with ID ' + ref + ' not found.')
    else:
        return image

# Params : image name
# Return : image ID
def get_image_id_temp(ref):
    images_list = list_images_temp()

    for i in images_list:
        if i['name'] == ref:
            image_id = i['id']
            break

    return image_id

get_image_temp('f980e857-afe7-4ea7-be06-1398219b9687')
