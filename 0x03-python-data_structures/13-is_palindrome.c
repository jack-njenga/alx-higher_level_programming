#include "lists.h"
/**
 * is_palindrome - check if a linked list of integers is a palindrome
 * @head: this is the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int *arr;
	listint_t *curr;
	size_t i = 0, n = 0;

	if (*head == NULL)
		return (1);
	curr = *head;
	while (curr != NULL)
	{
		i++;
		curr = curr->next;
	}
	if (i == 0 || i == 1)
		return (1);
	arr = malloc(sizeof(int) * i);
	if (!arr)
		return (0);
	curr = *head;
	i = 0;
	while (curr)
	{
		arr[i] = curr->n;
		curr = curr->next;
		i++;
	}
	i--;
	while (i >= n)
	{
		if (arr[n] != arr[i])
		{
			free(arr);
			return (0);
		}
		i--;
		n++;
	}
	free(arr);
	return (1);
}
