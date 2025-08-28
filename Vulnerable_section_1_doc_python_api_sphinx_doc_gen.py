     - ``line_no_has_content`` when False, this file only contains a doc-string.
       There is no need to include the remainder.
     """
    file = open(filepath, "r", encoding="utf-8")
    line = file.readline()
    line_no = 0
    text = []
    if line.startswith('"""'):  # Assume nothing here.
        line_no += 1
    else:
        file.close()
        return "", 0, True

    for line in file:
        line_no += 1
        if line.startswith('"""'):
            break
        text.append(line.rstrip())
 
    line_no += 1
    line_no_has_content = False
 
    # Skip over blank lines so the Python code doesn't have blank lines at the top.
    for line in file:
        if line.strip():
            line_no_has_content = True
            break
         line_no += 1
 
    file.close()
    return "\n".join(text).rstrip("\n"), line_no, line_no_has_content
 
 
 def title_string(text, heading_char, double=False):
     """
     Write RST file of ``bpy`` module (disabled by default)
     """
    if ARGS.bpy:
        filepath = os.path.join(basepath, "bpy.rst")
        file = open(filepath, "w", encoding="utf-8")
        fw = file.write
 
         fw("\n")
 
         fw(title_string(title, "="))
 
         fw(".. module:: bpy.types\n\n")
        file.close()
 
 
 def write_rst_types_index(basepath):
     """
     Write the RST file of ``bpy.types`` module (index)
     """
    if "bpy.types" not in EXCLUDE_MODULES:
        filepath = os.path.join(basepath, "bpy.types.rst")
        file = open(filepath, "w", encoding="utf-8")
        fw = file.write
         fw(title_string("Types (bpy.types)", "="))
         fw(".. module:: bpy.types\n\n")
         fw(".. toctree::\n")
             fw("   :maxdepth: 1\n\n")
             fw("   Shared Enum Types <bpy_types_enum_items/index>\n\n")
 
        file.close()

 
 def write_rst_ops_index(basepath):
     """
     Write the RST file of bpy.ops module (index)
     """
    if "bpy.ops" not in EXCLUDE_MODULES:
        filepath = os.path.join(basepath, "bpy.ops.rst")
        file = open(filepath, "w", encoding="utf-8")
        fw = file.write
         fw(title_string("Operators (bpy.ops)", "="))
         fw(".. module:: bpy.ops\n\n")
         write_example_ref("", fw, "bpy.ops")
         fw("   :maxdepth: 1\n")
         fw("   :glob:\n\n")
         fw("   bpy.ops.*\n\n")
        file.close()
 
 
 def write_rst_geometry_set(basepath):
 
     # Write the index.
     filepath = os.path.join(basepath, "bpy.types.GeometrySet.rst")
    file = open(filepath, "w", encoding="utf-8")
    fw = file.write
    fw(title_string("GeometrySet", "="))
    write_example_ref("", fw, "bpy.types.GeometrySet")
    pyclass2sphinx(fw, "bpy.types", "GeometrySet", bpy.types.GeometrySet, False)
 
     EXAMPLE_SET_USED.add("bpy.types.GeometrySet")
 
 
     # Write the index.
     filepath = os.path.join(basepath, "bpy.msgbus.rst")
    file = open(filepath, "w", encoding="utf-8")
    fw = file.write
    fw(title_string("Message Bus (bpy.msgbus)", "="))
    write_example_ref("", fw, "bpy.msgbus")
    fw(".. toctree::\n")
    fw("   :glob:\n\n")
    fw("   bpy.msgbus.*\n\n")
    file.close()
 
     # Write the contents.
     pymodule2sphinx(basepath, 'bpy.msgbus', bpy.msgbus, 'Message Bus', ())
     """
     Write the RST file of ``bpy.data`` module.
     """
    if "bpy.data" not in EXCLUDE_MODULES:
        # Not actually a module, only write this file so we can reference in the TOC.
        filepath = os.path.join(basepath, "bpy.data.rst")
        file = open(filepath, "w", encoding="utf-8")
        fw = file.write
         fw(title_string("Data Access (bpy.data)", "="))
         fw(".. module:: bpy.data\n")
         fw("\n")
         fw("   :type: :class:`bpy.types.BlendData`\n")
         fw("\n")
         fw(".. literalinclude:: ../examples/bpy.data.py\n")
        file.close()
 
        EXAMPLE_SET_USED.add("bpy.data")
 
 
 def pyrna_enum2sphinx_shared_link(prop):