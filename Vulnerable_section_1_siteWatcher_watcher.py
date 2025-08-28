             output.append(arg)	
         print(output)
 
def webCrawl(urlToCrawl: str, domainBound: str):
     #create dictionary of web links and if visited and visit time.
 
     #urlToCrawl = "https://www.tennisonly.com.au/Wilson_Tennis_Racquets.html"
     #domainBound = "https://www.tennisonly.com.au"
     
     linkSet = set()
 
    foundLinks = findLinks(urlToCrawl, linkSet, "1", domainBound)
     
     for link in foundLinks:
        newLinks = findLinks(link, linkSet, "2", domainBound)
     
     return linkSet
 
 
     #take in domain and parse sitemap.xml for more xml's and urls of weblinks and their lastModified date
 
 def readURL(urlToRead: str):
    if urlToRead == "https://wdt.wilson.com/":
        pass
    else:
        url = urlToRead
        print('url page:' + url)
        req = Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        content = urlopen(req).read()
        return content

        #content = urllib.request.urlopen(url).read()
 
 def findLinks(urlToSearch: str, linkSet: set, roundTag: str, siteDomain: str):
     try:
                     debugPrint(f".html found but no http in {link['href']}")
                     if link['href'][0] == "/":            
                         newLink = siteDomain + link['href']
                    elif "../" in link['href'][0]:
                        newLink = urlToSearch + link['href']
                     else:
                         newLink = siteDomain + "/" + link['href']
 
     #     "https://www.tennisonly.com.au/Tecnifibre_Tennis_Racquets.html",
     # ]
 
    domain = "https://patrickrothfuss.com"
    pagesToCrawl = [
        "https://patrickrothfuss.com"
    ]
    
    masterLinkSet = set()
 
    for page in pagesToCrawl:
        masterLinkSet.update(webCrawl(page,domain))
 
     for item in masterLinkSet:
         print(item)