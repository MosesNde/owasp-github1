 # See the Mulan PSL v2 for more details.
 # ******************************************************************************/
 import os
 import re
 import gzip
 import datetime
 
     def get_kernel_version_of_system(self) -> str:
         """
        Get the kernel version of current system, according to the command of 'uname -r'.
 
         Returns:
             str: kernel version
         """
        cmd = ["uname", "-r"]
        kernel_version = ''
        kernel_version, return_code = cmd_output(cmd)
        # 'uname -r' show the kernel version-release.arch of the current system
        # [root@openEuler hotpatch]# uname -r
        # 5.10.0-136.12.0.86.oe2203sp1.x86_64
        if return_code != SUCCEED:
            return kernel_version
        kernel_version = kernel_version.split('\n')[0]
        return kernel_version
 
     def _parse_and_store_from_xml(self, updateinfoxml: str):
         """