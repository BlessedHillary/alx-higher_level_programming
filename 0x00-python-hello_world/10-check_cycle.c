#include "lists.h"
/**
 *check_cycle - detect cycle in loop
 *@list: param
 *Return: return 1 if cycle found, return 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;
	slow_p = list;
	fast_p = list;
	if (list == NULL)
		return (0);
	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}
