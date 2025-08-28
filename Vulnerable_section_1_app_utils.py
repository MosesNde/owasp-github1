     def sanitize(url: Optional[str], allowed_domains: List[str]) -> Optional[str]:
         if not url:
             return None
        result = urllib.parse.urlparse(url)
         if result.hostname:
             if result.hostname in allowed_domains:
                return url
             else:
                 return None
         if result.path and result.path[0] == "/":