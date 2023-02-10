import requests


def get_number_information(number):
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    if response:
        return response.content.decode()
    return None

def get_cat_image_url():
    url = "https://aws.random.cat/meow"
    response = requests.get(url)
    if response:
        return response.json()["file"]
    return None