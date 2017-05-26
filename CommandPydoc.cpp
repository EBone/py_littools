// Win32Project1.cpp : 定义控制台应用程序的入口点。
//


#include <stdio.h>  
#include <stdlib.h>  
#include<string.h>

int main(int argc, char *argv[])
{

	char   psBuffer[128];
	FILE   *pPipe;

	/* Run DIR so that it writes its output to a pipe. Open this
	* pipe with read text attribute so that we can read it
	* like a text file.
	*/
	char py[100] = "python3 -m pydoc ";
	if (argv[1])
	{
		strcat(py, argv[1]);
		//printf("%s",py);
	}

	if ((pPipe = _popen(py, "rt")) == NULL)
		exit(1);

	/* Read pipe until end of file, or an error occurs. */

	while (fgets(psBuffer, 128, pPipe))
	{
		printf(psBuffer);
	}

	/* Close pipe and print return value of pPipe. */
	if (feof(pPipe))
	{
		printf("\nProcess returned %d\n", _pclose(pPipe));
	}
	else
	{
		printf("Error: Failed to read the pipe to the end.\n");
	}

}