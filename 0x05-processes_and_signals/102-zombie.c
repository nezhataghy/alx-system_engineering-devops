#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int loop_inifinit(void);

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

    loop_inifinit();

    return (EXIT_SUCCESS);
}

/**
 * loop_inifinit - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int loop_inifinit(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
