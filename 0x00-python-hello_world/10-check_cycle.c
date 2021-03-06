#include "lists.h"
/**
 * check_cycle - function that checks if there is a cycle in linked list
 * @list: ptr to linked list
 *
 * Description: function in C that checks if a singly linked list has a cycle in it.
 * Return: 1 if there's a linked list cycle and 0 if there's not it.
 */
int check_cycle(listint_t *list)
{
listint_t *moderate = '\0', *swift = '\0';

	if (list  == NULL)
		return (0);

	moderate = swift = list;

	do
	{
		swift = swift->next;
		moderate = (*moderate).next;
		if (swift)
			swift = swift->next;
	}

	while (swift && moderate != swift);
		if (swift && moderate == swift)
			return (1);

return (0);
}
