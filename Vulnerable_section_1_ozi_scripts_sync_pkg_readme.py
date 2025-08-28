 # Copyright 2023 Ross J. Duff MSc
 # The copyright holder licenses this file
 # to you under the Apache License, Version 2.0 (the
 except ImportError:
     import tomli as toml  # noqa: F401
 # pylint: disable=consider-using-with
source = pathlib.Path(os.environ.get("MESON_SOURCE_ROOT", ".."))
 pkg_info_file = open('PKG-INFO', 'r', encoding='utf-8')
 pkg_info = email.message_from_file(pkg_info_file).get_payload()
 pkg_info_file.close()
 if DIFF1 != '':
     print(DIFF1)
     sys.exit(len(DIFF1))
elif DIFF2 != "":
     print(DIFF2)
     sys.exit(len(DIFF2))
elif DIFF3 != "":
     print(DIFF3)
     sys.exit(len(DIFF3))