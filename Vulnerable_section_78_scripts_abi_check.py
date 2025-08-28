 #!/usr/bin/env python3
"""
This script compares the interfaces of two versions of Mbed TLS, looking
 for backward incompatibilities between two different Git revisions within
 an Mbed TLS repository. It must be run from the root of a Git working tree.
 
 For the source (API) and runtime (ABI) interface compatibility, this script
 is a small wrapper around the abi-compliance-checker and abi-dumper tools,
 applying them to compare the header and library files.
 Returns 0 on success, 1 on non-compliance, and 2 if there is an error
 while running the script.
 
You must run this test from an Mbed TLS root.
 """
 
 # Copyright The Mbed TLS Contributors