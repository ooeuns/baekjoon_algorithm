#include <stdio.h>
int main()
{
	char s[102];

	while(gets(s))
	{

		if( s[0]=='\0' )
			return 0;

		else
			puts(s);
	}

	return 0;

}
