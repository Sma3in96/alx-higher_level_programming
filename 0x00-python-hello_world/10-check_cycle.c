#include "lists.h"
/**
 * check_cycle - checks if for a cycle
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp->next)
	{
		if ((temp->next) == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
