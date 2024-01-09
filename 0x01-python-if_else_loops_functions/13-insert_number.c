#include "lists.h"
/**
 *insert_node - insert a node at beginning, middle or end of sorted singly
 * linked list
 *@head: the head pointer that point to the first member of the singly linked
 *list
 *@number: the data to be added to the singly linked list
 *Return: return the newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode_sort, *tmp;
	int key;

	tmp = *head;
	key = number;
	if (head == NULL)
		return (NULL);
	newNode_sort = malloc(sizeof(listint_t));
	if (newNode_sort == NULL)
		return (NULL);
	newNode_sort->n = number;
	newNode_sort->next = NULL;

	if (*head == NULL || key < (*head)->n)
	{
		newNode_sort->next = *head;
		*head = newNode_sort;
	}
	else
	{
		while (tmp->next != NULL && tmp->next->n < key)
			tmp = tmp->next;
		newNode_sort->next = tmp->next;
		tmp->next = newNode_sort;
	}

	return (newNode_sort);

}
