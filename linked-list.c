#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head;

void beg_insert();
void end_insert();
void beg_delete();
void end_delete();
void display();

int main(){
    int choice = 0;
    printf("1. beg_insert\n2. end_insert\n3. beg_delete\n4. end_delete\n5. Display\n6. Exit\n");
    while (choice != 6)
    {
        printf("Enter the choice: ");
        scanf("%d",&choice);
        switch (choice)
         {
         case 1:
            beg_insert();
            break;
         case 2:
            end_insert();
            break;
         case 3:
            beg_delete();
            break;
         case 4:
           end_delete();
           break;
         case 5:
            display();
            break;
         case 6:
            printf("Exit..");
            return 0;
         default:
            printf("Invalid choice");
         }
    }
}

void beg_insert()
{
    struct node *ptr;
    int item;
    ptr = (struct node *)malloc(sizeof(struct node *));
    if(ptr == NULL){
        printf("\nOVERFLOW");
    }
    else{
        printf("Enter value: ");
        scanf("%d",&item);
        ptr -> data = item;
        ptr -> next = head;
        head = ptr;
        printf("%d, Item Inserted",item);
    }
}

void end_insert()
{
    struct node *ptr, *temp;
    int item;
    ptr = (struct node *)malloc(sizeof(struct node));
    if(ptr == NULL){
        printf("\nOVERFLOW");
    }
    else{
        printf("\nEnter value: ");
        scanf("%d",&item);
        ptr -> data = item;
        if(head == NULL){
            ptr -> next = NULL;
            head = ptr;
            printf("%d, Item Inserted",item);
        }
        else{
            temp = head;
            while(temp -> next != NULL){
                temp = temp -> next;
            }
            temp -> next = ptr;
            ptr -> next = NULL;
            printf("%d, Item Inserted",item);
        }
    }
}

void beg_delete()
{
    struct node *ptr;
    if(head == NULL){
        printf("List is empty\n");
    }
    else{
        ptr = head;
        head = ptr -> next;
        free(ptr);
        printf("item deleted from begining..\n");
    }
}

void end_delete()
{
    struct node *p, *q;
    if(head == NULL){
        printf("\nList is empty\n");
    }
    else if(head -> next == NULL){
        head = NULL;
        free(head);
        printf("   Only node of the list deleted..\n");
    }
    else{
        p = head;
        while(p -> next != NULL){
            q = p;
            p = p -> next;
        }
        q -> next = NULL;
        free(p);
        printf("item deleted from last position..\n");
    }
}

void display()
{
    struct node *ptr;
    ptr = head;
    if(ptr == NULL){
        printf("\nOVERFLOW");
    }
    else{
        while(ptr != NULL){
            printf("%d\n",ptr -> data);
            ptr = ptr -> next;
        }
    }
}