import requests
import os
import pdfkit

def get_data(url):
    return requests.get(url)

def write_to_file(response, file_name, dir_name):
    with open(dir_name + "/" + file_name, 'wb') as f:
        f.write(response.content)

def create_directory():
    if not os.path.exists('Downloads'):
        os.makedirs('Downloads')

def download_file(url, convert):
    create_directory()
    dir_name = 'Downloads'
    
    file_name = url.split('/')[-1]
    if(convert):
        try:
            pdfkit.from_url(url, dir_name + "/" + file_name + '.pdf')
            return "Successfully Downloaded - " + str(file_name)
        except Exception as e:
            return str(e)

    try:
        response = get_data(url)
        write_to_file(response, file_name, dir_name)
        return "Successfully Downloaded - " + str(file_name)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    print ('Press Ctrl + C to quit')
    try:
        try:
            create_directory()
        except Exception as e:
            print(e)

        while True:
            url = input("Enter Url of the file: ")
            file_name = url.split('/')[-1]
            download_file(url, 0)
            print("Successfully Downloaded - " + file_name)


    except KeyboardInterrupt:
        print("Bye!")
