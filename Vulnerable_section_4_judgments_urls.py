     re_path(
         r"^(?P<judgment_uri>.*/\d{4}/\d+.*)/data.xml$", detail_xml, name="detail_xml"
     ),
    re_path(r"^(?P<judgment_uri>.*/\d{4}/\d+.*)/data.html$", detail, name="detail"),
     re_path(r"^(?P<judgment_uri>.*/\d{4}/\d+.*)/?$", detail, name="detail"),
     path("judgments/results", results, name="results"),
     path("judgments/advanced_search", advanced_search, name="advanced_search"),