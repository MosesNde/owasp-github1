 File extraction related functions.
 """
 import io
 import shlex
 import subprocess
 from pathlib import Path
 
 from .file_utils import iterate_file
 from .models import Chunk, Handler, TaskResult, UnknownChunk, ValidChunk
from .report import ExtractCommandFailedReport
 
 logger = get_logger()
 
             f.write(data)
 
 
def fix_permissions(outdir: Path):
     for path in outdir.rglob("*"):
         if path.is_symlink():
            continue
        elif path.is_dir():
            path.chmod(0o775)
         else:
            path.chmod(0o664)
 
 
 def get_extract_paths(extract_dir: Path, carved_path: Path) -> Tuple[Path, Path]:
             task_result.add_report(error_report)
             logger.error("Extract command failed", **error_report.asdict())
 
        fix_permissions(outdir)
     except FileNotFoundError:
         logger.error(
             "Can't run extract command. Is the extractor installed?",