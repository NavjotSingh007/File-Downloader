import urllib.request

while True:

    full_name = input("Enter the full name of file ")
    full_name = full_name.strip()

    if full_name.__contains__("."):

        while True:
            try:
                   url = input("Enter the url of file ")
                   url = url.strip()
                   urllib.request.urlretrieve(url, full_name)
                   break
            except ValueError:
                   print("Please check your url or internet connection")
        print(full_name," downloaded completed successfully")
        break

    else:
        print("Please also write extension of "+full_name)
        continue




