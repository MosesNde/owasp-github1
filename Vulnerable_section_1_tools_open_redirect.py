             
                 try:
                     r = requests.head(url, allow_redirects=True, timeout=5)
                except:
                    print "[-]Error on " + url
 
                if r.history:  
                    if r.url == "https://example.com":
                        print "[+]"+url
                        if is_closed:
                            file = open(output_file,"w+")
                        is_closed = False
                        file.write(url + "\n")
                     else:
                         print "[-]"+url
                else:
                    print "[-]"+url
        else:
            print "[-]Domain is invalid"
 
     if is_closed == False:
         file.close()