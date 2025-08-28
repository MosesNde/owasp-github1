     bundle_id = result.group(1)
     print(f"bundleId: {bundle_id}")
 
    os.system("ipatool auth login --email=your apple id email address here")
    os.system("ipatool download -b " + bundle_id)
 else:
     print("bundleId not found.")