import SoftLayer

def main(dict):

    API_USERNAME = dict['user']
    API_KEY = dict['apikey']
    VSI = dict['vsi']

    client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
    mgr = SoftLayer.VSManager(client)
    mgr_image = SoftLayer.ImageManager(client)

    vsiname = VSI
    image_list = mgr_image.list_private_images(name = vsiname+'_*')
    image_list.sort(key=lambda x: x['createDate'] )

    number_of_snapshots = len(image_list)
#  print('*** Before deleting old image templates')
#      for i in range(0, number_of_snapshots):
#           print(image_list[i]['id'], image_list[i]['createDate'],  image_list[i]['name'] )

    deleted_image = []
    if number_of_snapshots > 2:
        for i in range(0, number_of_snapshots-2):
#           print(i, image_list[i]['id'], image_list[i]['createDate'],  image_list[i]['name'] )
            deleted_image.append(image_list[i]['name'])
            mgr_image.delete_image(image_list[i]['id'])

    return { 'VSI' : VSI, 'deleted_image' : deleted_image }
