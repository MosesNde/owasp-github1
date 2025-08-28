 import io
from pathlib import Path
 
from unblob.extractor import carve_unknown_chunks
from unblob.models import UnknownChunk
 
 
 class TestCarveUnknownChunks:
         assert sorted(tmp_path.iterdir()) == [written_path1, written_path2]
         assert written_path1.read_bytes() == content[:4]
         assert written_path2.read_bytes() == content[4:]