             bundle_namespace = dirname.split(bundle_token)[1]
             base_dir = "/".join(split_dir[0: len(split_dir) - 1])
             new_path = base_dir + "/" + bundle_namespace
            os.system("mv " + dirname + " " + new_path)
 
 if __name__ == '__main__':
     sys.exit(main(sys.argv))