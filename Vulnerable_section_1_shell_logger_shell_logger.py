 from datetime import datetime, timedelta
 from distutils import dir_util
 from pathlib import Path
 from types import SimpleNamespace
 from typing import Iterator, Optional, Union
 
             # `stream_dir`.
             curr_html_file = self.html_file.name
             new_location = self.log_dir / curr_html_file
            temp_link_name = Path(tempfile.mktemp(dir=self.log_dir))
            temp_link_name.symlink_to(self.html_file)
             temp_link_name.replace(new_location)
 
             # Save everything to a JSON file in the timestamped