# cam_list = {
#     "cam1": [None, None],
#     "cam2": [None, None],
#     "cam3": [None, None],
#     "cam4": [None, None],
#     "cam5": [None, None],
#     "cam6": [None, None],
# }


# def set_url(device_id, device_url):
#     # Check if values already exist in the dictionary
#     values_exist = False
#     for value in cam_list.values():
#         if [device_id, device_url] == value:
#             values_exist = True
#             break

#     # If values don't exist, set them to a key with None values
#     if not values_exist:
#         for key, value in cam_list.items():
#             if all(val is None for val in value):
#                 cam_list[key] = [device_id, device_url]
#                 print(f"The values [{device_id}, {device_url}] have been set to the key '{key}'.")
#                 break
#     else:
#         print(f"The values [{device_id}, {device_url}] already exist in the dictionary.")

            
# def clear_url():
# 	cam_list.update({
#     		"cam1": [None, None],
#             "cam2": [None, None],
#             "cam3": [None, None],
#             "cam4": [None, None],
#             "cam5": [None, None],
#             "cam6": [None, None],
#             })


# def destroy(device_id):
#     for key, value in cam_list.items():
#         if device_id in value:
#             cam_list[key] = [None, None]
#             print(f"The key '{key}' has been set to [None, None].")
#             print(cam_list)
#             break

# def has_none_value(dictionary):
#     for value in dictionary.values():
#         if all(val is None for val in value):
#             return True
#     return False


cam_list = {
    "cam1": [None, None, None],
    "cam2": [None, None, None],
    "cam3": [None, None, None],
    "cam4": [None, None, None],
    "cam5": [None, None, None],
    "cam6": [None, None, None],
}


def set_url(device_id, device_url, device_name):
    # Check if values already exist in the dictionary
    values_exist = False
    for value in cam_list.values():
        if [device_id, device_url, device_name] == value:
            values_exist = True
            break

    # If values don't exist, set them to a key with None values
    if not values_exist:
        for key, value in cam_list.items():
            if all(val is None for val in value):
                cam_list[key] = [device_id, device_url, device_name]
                print(f"The values [{device_id}, {device_url} {device_name}] have been set to the key '{key}'.")
                break
    else:
        print(f"The values [{device_id}, {device_url} {device_name}] already exist in the dictionary.")

            
def clear_url():
	cam_list.update({
    		"cam1": [None, None, None],
            "cam2": [None, None, None],
            "cam3": [None, None, None],
            "cam4": [None, None, None],
            "cam5": [None, None, None],
            "cam6": [None, None, None],
            })


def destroy(device_id):
    for key, value in cam_list.items():
        if device_id in value:
            cam_list[key] = [None, None, None]
            print(f"The key '{key}' has been set to [None, None, None].")
            print(cam_list)
            break

def has_none_value(dictionary):
    for value in dictionary.values():
        if all(val is None for val in value):
            return True
    return False