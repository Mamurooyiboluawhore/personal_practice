#include <stdio.h>
/**
 *main - prints the alphabet in lowercase
 *Description:prints the alphabet in lowercase, followed by a new line
 *Return: 0
*/

int main(void)
{
	char lower_keys;

		for (lower_keys = 'a'; lower_keys <= 'z'; lower_keys++)
		{
			putchar(lower_keys);
		}
		putchar('\n');
		return (0);
}

