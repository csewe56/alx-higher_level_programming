#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - function that checks if a singly linked list has a cycle in it
 *@list: a singly linked list
 *Return: always success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
