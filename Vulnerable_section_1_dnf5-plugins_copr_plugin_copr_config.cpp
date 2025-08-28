 
 #include "libdnf5/utils/os_release.hpp"
 
 #include <filesystem>
 
 
 namespace dnf5 {
     load_copr_config_file("/usr/share/dnf/plugins/copr.vendor.conf");
     load_copr_config_file(etc_dir / "dnf/plugins/copr.vendor.conf");
     load_copr_config_file(etc_dir / "dnf/plugins/copr.conf");
    std::string pattern = etc_dir / "dnf/plugins/copr.d/*.conf";
    glob_t glob_result;
    glob(pattern.c_str(), GLOB_MARK, nullptr, &glob_result);
    for (size_t i = 0; i < glob_result.gl_pathc; ++i) {
        std::string file_path = glob_result.gl_pathv[i];
        load_copr_config_file(file_path);
     }
 
     // For DNF4, we used to have: