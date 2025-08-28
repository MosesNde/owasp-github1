 def is_request_hpp(request_data, url):
     """
     Function that checks if a request contains HTTP Parameter Pollution (HPP).
        First, it checks for HPP in the parameters when entered in the URL directly.
        Then, it checks for HPP in the parameters when entered in a input field.
     
     Args:
         request_data (str): A JSON string of the request data.
     Returns:
         tuple(bool, str): A tuple of (True/False - HPP detected, str - The string where HPP was detected)
     """
     
     # Send the request URL to the function that checks it.
     is_url_safe = is_url_hpp(url)
     
     # Check if the URL is safe.
    if is_url_safe != (False, None):
         return is_url_safe
     
     # Check if the request data contains HPP.
     """
     # Loop through all the keys and values in the query parameters.
     for key, value in args.items():
         # Check if the parameter key is present in the text.
         if ("&" + key + "=") in text:
             # Return a tuple indicating that HPP was detected and the parameter name with HPP.