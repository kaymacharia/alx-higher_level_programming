#include<stdio.h>
#include<stdlib.h>
#include"lists.h"

/**
*print_listint-printsallelementsofalistint_tlist
*@h:pointertoheadoflist
*Return:numberofnodes
*/
size_tprint_listint(constlistint_t*h)
{
constlistint_t*current;
unsignedintn;/*numberofnodes*/

current=h;
n=0;
while(current!=NULL)
{
printf("%i\n",current->n);
current=current->next;
n++;
}

return(n);
}

/**
*add_nodeint_end-addsanewnodeattheendofalistint_tlist
*@head:pointertopointeroffirstnodeoflistint_tlist
*@n:integertobeincludedinnewnode
*Return:addressofthenewelementorNULLifitfails
*/
listint_t*add_nodeint_end(listint_t**head,constintn)
{
listint_t*new;
listint_t*current;

current=*head;

new=malloc(sizeof(listint_t));
if(new==NULL)
return(NULL);

new->n=n;
new->next=NULL;

if(*head==NULL)
*head=new;
else
{
while(current->next!=NULL)
current=current->next;
current->next=new;
}

return(new);
}

/**
*free_listint-freesalistint_tlist
*@head:pointertolisttobefreed
*Return:void
*/
voidfree_listint(listint_t*head)
{
listint_t*current;

while(head!=NULL)
{
current=head;
head=head->next;
free(current);
}
}
