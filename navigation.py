"""
This module allows you to navigate throught a json file
"""
import json
def user_input(type: str) -> str:
    """
Gets user's input which determines the next step
    """
    if type == "dict":
        user_choice = input("Which key you'd like to choose (enter key): ")
    elif type == "list":
        user_choice = input("Which item you'd like to choose (enter its number starting from 1): ")
        if int(user_choice) <0:
            print("Index has to be positive integer")
    return user_choice


def navigation(path_to_json: str):
    """
Main loop which walks trought json file
    """
    with open(path_to_json) as file:
        data = json.load(file)
    while True:
        if isinstance(data, list):
            try:
                print("List has {0} items ".format(len(data)))
                next = user_input("list")
                data = data[int(next)-1]
            except:
                print("Wrong index")
                next = user_input("list")
        elif isinstance(data, dict):
            try:
                print("Dictionary has such keys: {0}".format(list(data.keys())))
                next = user_input("dict")
                data = data[next]
            except:
                print("No such key in a dictionary")
                next = user_input("dict")
        else:
            print(data)
            break

if __name__ == "__main__":
    navigation("web.json")
