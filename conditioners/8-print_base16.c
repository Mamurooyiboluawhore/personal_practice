#include <stdio.h>
/**
 *main - prints all the numbers of base 16 in lowercase
 *
 *Description: prints ints followed by a new line
 *
 *Return: 0
*/

int main(void)

{
	int numb;
	int low;

	for (numb = '0'; numb <= '9'; numb++)
	{
		putchar(numb);
	}
	for (low = 'a'; low <= 'f'; low++)
	{
		putchar(low);
	}
	putchar('\n');
	return (0);
}
