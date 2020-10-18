import requests

def spaceX_api(all_filters):
    if(all_filters == None):
        apiURL = "https://api.spacexdata.com/v3/launches?limit=50"
    else:
        filter_string = ''
        for key in all_filters:
            filter_string += '&'+key+'='+all_filters[key]
        # filter_string = filter_string[:-1]

        apiURL = "https://api.spacexdata.com/v3/launches?limit=50"+filter_string
        print("filter String",filter_string)
    res = requests.get(apiURL)

    if res.status_code == 200: 
        spacex_all_data = res.json()
        all_data = []
        for data in spacex_all_data:
            # print(data)
            spacex_data = {
                'flight_number': data['flight_number'],
                'mission_name': data['mission_name'], 
                'mission_ids': data['mission_id'],
                'launch_year': data['launch_year'],
                'launch_success': data['launch_success'],
                'image': data['links']['mission_patch_small'],
                'land_success': data['rocket']['first_stage']['cores'][0]['land_success']
                # 'land_success': data['rocket']['first_stage']['cores']
            }
            all_data.append(spacex_data)
        # print(all_data)
        return all_data
    else:
        return 404


# if __name__ == '__main__':
#     spaceX_api()