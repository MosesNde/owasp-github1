     return len;
 }
 
 static inline bool path_is_absolute(const char *path) { return path[0] == '/'; }
 
 /**
 
     // NOTE: This assumes that the paths in the mountpoints are ordered by length descending
     auto *mp = s_mountpoints.find_first([&](MountPoint *mp) {
        return startswith(cpath, mp->path);
     });
     if (mp == nullptr) {
        LOGW("Mo mountpoint found");
         rc = -ERR_NOENT;
     } else {
         LOGI("Found mountpoint at '%s'", log_canonicalized_path(mp->path));
     LOGD("Mountpoint %s ('%s') has path skip %" PRIu32, path, log_canonicalized_path(mp->path), mp->path_skip);
 
     auto *after = s_mountpoints.find_first([&](MountPoint *mp) {
        return strlen(mp->path) < strlen(cpath);
     });
     if (after) {
         s_mountpoints.append_before(mp, after);
     } else {
         s_mountpoints.add(mp);
     }
 
     kassert(rc == 0); // TODO: handle this error
     icache_insert(&fs.icache, root_inode->identifier, root_inode);
 
     return rc;
 }
 