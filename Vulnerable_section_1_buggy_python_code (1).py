import os
 import yaml
 import flask
 
     # Fetch and print the requested URL
 
     try:
        http = urllib.PoolManager()
         # r = http.request('GET', url)
     except:
         print('Exception')
         print_nametag(input("Please format your nametag: "), new_person)
     elif choice == "2":
         urlib_version = input("Choose version of urllib: ")
        while (urlib_version != "2" and urlib_version != "3") {
             urlib_version = input("Choose version of urllib (2 or 3): ")
        }
         fetch_website(urlib_version, url="https://www.google.com")
     elif choice == "3":
         load_yaml(input("File name: "))