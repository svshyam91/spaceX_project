import requests

def spaceX_api():
    apiURL = "https://api.spacexdata.com/v3/launches?limit=20"
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
                'image': data['links']['mission_patch_small']
                # 'land_success': data['rocket']['first_stage']['cores']
            }
            all_data.append(spacex_data)
        return all_data
    else:
        return 404


if __name__ == '__main__':
    spaceX_api()