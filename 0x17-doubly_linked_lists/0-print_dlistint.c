#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;
	int elements = 0;
	while (current != NULL)
	{
		printf("%d \n", current->n);
		elements++;
		current = current->next;
	}
	return elements;
}