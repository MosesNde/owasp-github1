         goto INPUT;
         break;
     }
    if(strchr(search,'"')||strchr(search,'\'')||strchr(search,';')||strchr(search,'}')||strchr(search,'{')||strchr(search,'\\'))
     {
         printf("ARE YOU TRYING COMMAND INJECTION???\n");
         return -1;