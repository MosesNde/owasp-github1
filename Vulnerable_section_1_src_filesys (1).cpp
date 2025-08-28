 	const io::IFileList* files_in_zip = opened_zip->getFileList();
 
 	for (u32 i = 0; i < files_in_zip->getFileCount(); i++) {
		std::string fullpath = destination + DIR_DELIM;
		fullpath += files_in_zip->getFullFileName(i).c_str();
		std::string fullpath_dir = fs::RemoveLastPathComponent(fullpath);

 		if (files_in_zip->isDirectory(i))
 			continue; // ignore, we create dirs as necessary
 
 		if (!fs::PathExists(fullpath_dir) && !fs::CreateAllDirs(fullpath_dir))
 			return false;
 