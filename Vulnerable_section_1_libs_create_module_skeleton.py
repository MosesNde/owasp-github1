         if not os.path.exists(path):
             os.makedirs(path)
 
    mkdir(os.path.join(lib_name, module_name))
 
     ################################################################################
     # Generate basic directory structure
     for subdir in ["docs", "examples", "include", "src", "tests"]:
        path = os.path.join(lib_name, module_name, subdir)
         mkdir(path)
     # Generate include directory structure
     # Normalize path...
     include_path = "".join(module_name)
    path = os.path.join(lib_name, module_name, "include", "pika", include_path)
     mkdir(path)
    path = os.path.join(lib_name, module_name, "tests", "unit")
     mkdir(path)
    path = os.path.join(lib_name, module_name, "tests", "regressions")
     mkdir(path)
    path = os.path.join(lib_name, module_name, "tests", "performance")
     mkdir(path)
     ################################################################################
 
     ################################################################################
     # Generate README skeleton
    f = open(os.path.join(lib_name, module_name, "README.rst"), "w")
     f.write(readme_template)
     ################################################################################
 
     ################################################################################
     # Generate CMakeLists.txt skeletons
 
     # Generate top level CMakeLists.txt
    f = open(os.path.join(lib_name, module_name, "CMakeLists.txt"), "w")
     f.write(root_cmakelists_template)
 
     # Generate docs/index.rst
    f = open(os.path.join(lib_name, module_name, "docs", "index.rst"), "w")
     f.write(index_rst)
 
     # Generate examples/CMakeLists.txt
    f = open(os.path.join(lib_name, module_name, "examples", "CMakeLists.txt"), "w")
     f.write(examples_cmakelists_template)
 
     # Generate tests/CMakeLists.txt
    f = open(os.path.join(lib_name, module_name, "tests", "CMakeLists.txt"), "w")
     f.write(tests_cmakelists_template)
 
     # Generate tests/unit/CMakeLists.txt
     f = open(
        os.path.join(lib_name, module_name, "tests", "unit", "CMakeLists.txt"), "w"
     )
     f.write(cmake_header)
 
     # Generate tests/regressions/CMakeLists.txt
     f = open(
        os.path.join(lib_name, module_name, "tests", "regressions", "CMakeLists.txt"),
         "w",
     )
     f.write(cmake_header)
 
     # Generate tests/performance/CMakeLists.txt
     f = open(
        os.path.join(lib_name, module_name, "tests", "performance", "CMakeLists.txt"),
         "w",
     )
     f.write(cmake_header)
 modules = sorted(
     [
         module
        for module in os.listdir(os.path.join(cwd, lib_name))
         if os.path.isdir(os.path.join(cwd, lib_name, module))
     ]
 )
 endforeach()
 """
 
f = open(os.path.join(cwd, lib_name, "CMakeLists.txt"), "w")
 f.write(modules_cmakelists)
 
 header_name_str = (
 for module in modules:
     modules_rst += f"   /libs/{lib_name}/{module}/docs/index.rst\n"
 
f = open(os.path.join(cwd, lib_name, "modules.rst"), "w")
 f.write(modules_rst)
 
 ################################################################################