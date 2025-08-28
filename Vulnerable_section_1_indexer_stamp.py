 import zlib
 import msgpack
 import io
import binascii
 from datetime import datetime
 from decimal import Decimal
 
     check_format,
     build_src20_svg_string,
     insert_into_src20_tables,
    update_balances,
    get_total_user_balance_from_db
 )
 import traceback
 from src.aws import (
                 # this will be ok in the docker containers, but a potential problem
                 # will need to verify that there are no instances where this is su
                 command = f'printf "%s" "{base64_string}" | base64 -d 2>&1'
                image_data = subprocess.check_output(command, shell=True)
                 return image_data, True
             except Exception as e3:
                 # If all decoding attempts fail, print an error message and return None
 
     if (
         ident in config.SUPPORTED_SUB_PROTOCOLS
        or file_suffix in config.MIME_TYPES
     ):
         if type(decoded_base64) is str:
             decoded_base64 = decoded_base64.encode('utf-8')