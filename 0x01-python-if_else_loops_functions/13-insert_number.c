#include "lists.h"
/**
 * insert_node - inserts a number into a sorted
 * singly linked list.
 * @head: a pointer that points to a pointer of
 * the head of the linked list
 * @number: the value to populate the linked list in order
 *
 * Return: the address of the new node, or NULL if
 * it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!(*head))
	{
		*head = new;
		return (new);
	}
	if (number < current->n)
	{
		new->next = current;
		current = new;
	}
	else
	{
		while (current->next)
		{
			if (current->next->n != number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			else
				current = current->next;
		}
		current->next = new;
	}
	return (new);
}
