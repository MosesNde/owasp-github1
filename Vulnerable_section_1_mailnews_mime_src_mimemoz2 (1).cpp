   if (!urlSpec) return NS_ERROR_OUT_OF_MEMORY;
 
   if ((options->format_out == nsMimeOutput::nsMimeMessageBodyDisplay) &&
      (PL_strncasecmp(aMessageURL, urlSpec, strlen(urlSpec)) == 0))
     return NS_OK;
 
   nsCString urlString(urlSpec);
 