#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to pointer of first node
 * Return: 0 if palindrom isn't detected
 */

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *temp;
	listint_t *mid;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	mid = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;

	len = len / 2;

	for (i = 1; i < len; i++)
		mid = mid->next;
	if (len % 2 != 0 && len != 1)
	{
		mid = mid->next;
		len = len - 1;
	}
	reverse(&mid);
	i = compare_lists(*head, mid, len);

	return (i);
}

/**
 * compare_lists - compare lists
 * @head: pointer to the head node
 * @mid: pointer to the middle node
 * @len : length of the list
 * Return: if the same 1
 */

int compare_lists(listint_t *head, listint_t *mid, int len)
{
	int i;

	if (head == NULL || mid == NULL)
		return (1);

	for (i = 0; i < len; i++)
	{
		if (head->n != mid->n)
			return(0);
		head = head->next;
		mid = mid->next;
	}
	return (1);
}

/**
 * reverse - reverse a list
 * @head: pointer to head of list
 */

void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL|| *head == NULL)
		return;

	prev = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
