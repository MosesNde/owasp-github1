         ret = std::system(cmd.c_str());
         break;
     default:
        std::cout << "please write the name of files to add" << std::endl;
         std::getline(std::cin, files);

        if (files.size())
         {
             cmd += files;
             ret = std::system(cmd.c_str());