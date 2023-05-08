#include "lists.h"
/**
 * check_cycle - checks for cycle in @list
 * @list: sturcture to check for the cycle
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *tmp = list;

	if (!list)
		return (0);
	while (tmp && tmp->next)
	{
		head = head->next;
		tmp = tmp->next->next;

		if (head == tmp)
			return (1);
	}
	return (0);
}
