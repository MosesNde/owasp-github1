       url_unescape (u->host);
       host_modified = true;
 
       /* Apply IDNA regardless of iri->utf8_encode status */
       if (opt.enable_iri && iri)
         {