#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that determines whether a string is a palidrone
 * @listint_t: parameter
 * @*head: pointer to head of s..linked list
 *
 * Return: 1
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL;

    /* Check if the list is empty or has only one element */
    if (!*head || !(*head)->next) {
        return (1);
    }

    /* Find the middle node using fast and slow pointers */
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Reverse the second half of the list */
    while (slow) {
        slow->next = prev;
        prev = slow;
        slow = slow->next;
    }

    /* Compare the first and second halves */
    slow = prev;
    while (*head && slow) {
        if ((*head)->n != slow->n) {
            return (0);
        }
        *head = (*head)->next;
        slow = slow->next;
    }

    return (1);
}

