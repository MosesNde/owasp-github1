 ERROR_PAGE_TEMPLATE = """
 <!DOCTYPE html>
 <html lang="en">
     return (
         ERROR_PAGE_TEMPLATE.replace("STATUS_CODE", status_code)
         .replace("ERROR_TITLE", error_title)
        .replace("ERROR_MESSAGE", error_message)
        .replace("ERROR_DETAILS", error_details)
     )