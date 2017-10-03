import requests
import os

def get_data(url):
    return requests.get(url)

def write_to_file(response, file_name, dir_name):
    with open(dir_name + "/" + file_name, 'wb') as f:
        f.write(response.content)

def create_directory():
    if not os.path.exists('Downloads'):
        os.makedirs('Downloads')


print ('Press Ctrl + C to quit')
try:
    try:
        create_directory()
    except Exception as e:
        print(e)

    while True:
        dir_name = 'Downloads'
        url = input("Enter Url of the file: ")
        file_name = url.split('/')[-1]
        try:
            response = get_data(url)
            write_to_file(response, file_name, dir_name)
            print("Successfully Downloaded - " + file_name)
        except Exception as e:
            print(e)


except KeyboardInterrupt:
    print("Bye!")
