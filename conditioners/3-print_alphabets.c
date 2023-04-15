#include <stdio.h>
/*
*/

int main(void)
{
	char lower_keys;
	char upper_keys;
		for (lower_keys = 'a'; lower_keys <= 'z'; lower_keys++)
		{
			putchar(lower_keys);
		}
		for (upper_keys = 'A'; upper_keys <= 'Z'; upper_keys++)
		{
			putchar(upper_keys);
		}
		putchar('\n');
		return (0);
}

