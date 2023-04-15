#include <stdio.h>
/**
*/
int main(void)
{
	int rev;

	for (rev = 'z';rev >= 'a'; rev--)
	{
		putchar(rev);
	}
	putchar('\n');
	return (0);
}
