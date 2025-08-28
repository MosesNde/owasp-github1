             URLs that are to html files (e.g., GitHub Pages will serve
             an html file if URL doesn't include the .html extension).
     """
    os.chdir(websiteRoot)
     blockedPaths = parseRobotsTxt()
     
     allFiles = gatherfiles(createExtensionSet(includeHTML, includePDF, additionalExt))