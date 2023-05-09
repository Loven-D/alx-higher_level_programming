#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;/* Move slow pointer by one*/
		fast = fast->next->next;/* Move fast pointer by two*/

		if (slow == fast)/* If the pointers meet, there's a cycle */
			return (1);
	}

	return (0);/* If the end of the list is reached, there's no cycle */
}
