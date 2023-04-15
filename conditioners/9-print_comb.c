#include <stdio.h>

/**
 *main - prints all possible combinations of single-digit numbers
 *
 *Description: prints all possible combinations of single-digit numbers
 *
 *Return: 0
 */
int main(void)
{
	int digit;

	for (digit = '0'; digit <= '9'; digit++)
	{
		putchar(digit);
		putchar(',');
		putchar(' ');
	}
/**
*putchar(' ');these lines are here 
*putchar(',');
*/
	putchar('\n');
	return (0);
}
