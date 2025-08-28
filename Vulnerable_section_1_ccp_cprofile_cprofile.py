 
 if __name__ == "__main__":
     func = sys.argv[1]
    file_name = generate_label(func)
    cProfile.run(func + "()", file_name)