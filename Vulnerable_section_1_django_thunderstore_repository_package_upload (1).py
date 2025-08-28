 from thunderstore.repository.validation.manifest import validate_manifest
 from thunderstore.repository.validation.markdown import validate_markdown
 from thunderstore.repository.validation.zip import (
    check_relative_paths,
     check_zero_offset,
 )
 
                 if unzip.testzip():
                     raise ValidationError("Corrupted zip file")
 
                if check_relative_paths(unzip.infolist()):
                    raise ValidationError("Relative paths inside a zip are not allowed")
 
                 if not check_zero_offset(unzip.infolist()):
                     raise ValidationError(
                         "The zip includes bogus data at the beginning of the file."
                     )
 
                 try:
                     manifest = unzip.read("manifest.json")
                     self.validate_manifest(manifest)