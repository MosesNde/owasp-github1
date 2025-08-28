 #include <shlwapi.h>
 #include <ctype.h>
 #include <string.h>
 const char * getdirname(const char *path)
 {
 	const char *a = strpbrk(path, "\\/");
 		if (!a) return path;
 	}
 }
 void copy(const char * src, const char *dst)
 {
 	char buf[512];
	//TODO:command injection
	snprintf(buf, sizeof(buf), "xcopy \"%s\" \"%s\" /I", src, dst);
 	system(buf);
 }
 typedef struct
 }
 void generateDEF(makein *makedata, const char *spec, const char *path)
 {
	char commandline[512];
	sprintf(commandline, "convspec %s -DEF > \"%s\"", spec, path);
	system(commandline);
 }
 void generateASM(makein *makedata, const char *spec, const char *path, const char *mod)
 {
	char commandline[512];
	sprintf(commandline, "convspec \"%s\" \"%s\" > \"%s\"", spec, mod, path);
	system(commandline);
 }
 int main(int argc, char **argv)
 {
 	if (argc != 3)
 	{
        puts("Converts wine DLL source Makefiles to MSVC projects.")
 		puts("usage: convertwinefile <dll directory> <2>");
 		return 0;
 	}