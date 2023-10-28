#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t p_id;
	char num = 0;

	for (; num < 5;)
	{
		p_id = fork();
		if (p_id > 0)
		{
			printf("Zombie process created, PID: %d\n", p_id);
			sleep(1);
			num++;
		}
		else
			exit(0);
	}

	while (1)
	{
		sleep(1);
	}

	return (EXIT_SUCCESS);
}
