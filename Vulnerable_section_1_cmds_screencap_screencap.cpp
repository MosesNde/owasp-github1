 #include <linux/fb.h>
 #include <sys/ioctl.h>
 #include <sys/mman.h>
 
 #include <binder/ProcessState.h>
 
 }
 
 static status_t notifyMediaScanner(const char* fileName) {
    String8 cmd("am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file://");
    cmd.append(fileName);
    cmd.append(" > /dev/null");
    int result = system(cmd.string());
    if (result < 0) {
         fprintf(stderr, "Unable to broadcast intent for media scanner.\n");
         return UNKNOWN_ERROR;
     }