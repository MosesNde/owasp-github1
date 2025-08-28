         print_nametag(input("Please format your nametag: "), new_person)
     elif choice == "2":
         urlib_version = input("Choose version of urllib: ")
         fetch_website(urlib_version, url="https://www.google.com")
     elif choice == "3":
         load_yaml(input("File name: "))