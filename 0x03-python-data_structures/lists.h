#ifndefLISTS_H
#defineLISTS_H

/**
*structlistint_s-singlylinkedlist
*@n:integer
*@next:pointstothenextnode
*
*Description:singlylinkedlistnodestructure
*forproject
*/
typedefstructlistint_s
{
intn;
structlistint_s*next;
}listint_t;

size_tprint_listint(constlistint_t*h);
listint_t*add_nodeint_end(listint_t**head,constintn);
voidfree_listint(listint_t*head);

intis_palindrome(listint_t**head);

#endif/*LISTS_H*/
