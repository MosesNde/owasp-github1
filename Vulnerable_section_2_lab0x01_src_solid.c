 #include <limits.h>
 #include <stdio.h>
 #include <string.h>
 
 #define OUTPUT_NAME_SIZE 500
 
     goto error;
   }
 
  if (strchr(argv[1], ';') != NULL) {
    goto error;
  }

   /* Assign names to arguments for better abstraction */
   char output_name[OUTPUT_NAME_SIZE];
   strncpy(output_name, argv[1], OUTPUT_NAME_SIZE);
   free(img->px);
   free(img);
 
  /* We want to inform user how big the new image is.
   * "stat -c %s filename" prints the size of the file
   *
   * To prevent buffer overflows we use strncat.
   */
  char command[512] = {0};

  printf("Size: ");

  /* printf will write to the screen when it encounters a new line
   * By calling fflush we force the program to output "Size " right away
   */
  fflush(stdout);
  strcat(command, "stat -c %s ");
  strncat(command, output_name, OUTPUT_NAME_SIZE);
  system(command);
 
   return 0;
 