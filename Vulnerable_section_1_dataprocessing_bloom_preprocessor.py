 def command_injection(data):
     system_call_pattern = re.compile(r'\b(?:exec|system|shell_exec|passthru)\b', re.IGNORECASE)
     invoked_function_pattern = re.compile(r'\b(?:eval|create_function)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']|'
                                             r'\(\s*[\'"]\s*\.\s*[\w$]+\s*\)|'  # function_name (''.variable)
                                             r'\(\s*[\'"]\s*\+\s*[\w$]+\s*\)|'  # function_name (''+variable)
                                             r'\(\s*`.*?`\s*\)|'  # function_name (`${variable}`)
                                             r'\(\s*\w+\s*\)',  # function_name (variable)
                                             re.IGNORECASE)
 
     system_call_count = 0
     invoked_function_count = 0
         if re.search(array_copy_pattern, snippet):
             array_copy_count += 1
 
     return [prototype_assignment_count, object_assignment_count, object_manipulation_count,
             json_parse_count, property_check_count, default_object_assignment_count,
             dynamic_property_assignment_count, array_copy_count]
 
 def file_inclusion(data):
    php_dynamic_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
     php_unsanitized_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
     php_allow_url_include_pattern = re.compile(r'allow_url_include\s*=\s*(1|On)', re.IGNORECASE)
     php_dynamic_path_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?".*?\$_(GET|POST|REQUEST|COOKIE).*?\.\w+', re.IGNORECASE)
     php_directory_traversal_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\.+\.\.\/', re.IGNORECASE)
     php_sensitive_file_access_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?(config|passwords|settings)\.php', re.IGNORECASE)
 
    js_dynamic_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)
     js_unsanitized_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)
 
     # Concatenation patterns
    concat_pattern = r'[\'"]\s*\.\s*[\'"]|\(\s*[\'"]\s*\.\s*[\w$]+\s*\)|' \
                    r'\(\s*[\'"]\s*\+\s*[\w$]+\s*\)|\(\s*`.*?`\s*\)|\(\s*\w+\s*\)'
 
    php_dynamic_inclusion_pattern = re.compile(f'{php_dynamic_inclusion_pattern.pattern}|{concat_pattern}', re.IGNORECASE)
    php_unsanitized_inclusion_pattern = re.compile(f'{php_unsanitized_inclusion_pattern.pattern}|{concat_pattern}', re.IGNORECASE)
    php_dynamic_path_pattern = re.compile(f'{php_dynamic_path_pattern.pattern}|{concat_pattern}', re.IGNORECASE)
 
     dynamic_inclusion_count = 0
     unsanitized_inclusion_count = 0
         php_directory_traversal_count += len(re.findall(php_directory_traversal_pattern, snippet))
         php_sensitive_file_access_count += len(re.findall(php_sensitive_file_access_pattern, snippet))
 
     return [dynamic_inclusion_count, unsanitized_inclusion_count, php_allow_url_include_count,
             php_dynamic_path_count, php_directory_traversal_count, php_sensitive_file_access_count]
 
     X_Feature_1D = [item for column in zip(*matrix) for item in column]
     Y_Feature_1D = compute_combined_matrix(matrix)
 
    # Don't print when extracting to make this faster
 
     # print("\nX-Feature:")
     # for row in matrix:
     #     print(row)
    # print(X_Feature_1D)
 
     # print("\nY-Feature:")
     # combined_matrix = compute_combined_matrix(matrix)