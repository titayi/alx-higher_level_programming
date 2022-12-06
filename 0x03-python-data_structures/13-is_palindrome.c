#include "lists.h"
/**
 * palindrome - check if is palindrome with recursion
 * @list: pointer to list head
 * @m: pointer
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **list, listint_t *m)
{
	int response;

	if (m != NULL)
	{
		response = palindrome(list, m->next);
		if (response != 0)
		{
			response = (m->n == (*list)->n);
			*list = (*list)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: pointer to the list head
 *
 *Return: 0 if not palindrome or 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
