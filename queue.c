#include<stdio.h>
#define SIZE 3
int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int item){
       if(rear == SIZE - 1){
          printf("Queue is Full!! OVERFLOW condition\n");
       }
        else{
                if(front == -1){
                    front = 0;
                    rear = 0;
                }
                else{
                    rear ++;
                }
                queue[rear] = item;  
                printf("%d, Item Inserted\n",item);
            }
        }
void dequeue(int item){
        if(front == -1)
            {
               printf("Queue is Empty! UNDERFLOW condition\n"); 
            }
        else{
            item = queue[front];
            if(front == rear){
                front = -1;
                rear = -1;
            }
            else{
                front++;
            }
            printf("%d, Item Deleted\n",item);
        }
}

void display(){
    if(front == -1){
        printf("Queue is empty!!\n");
    }
    else{
        printf("Queue elements: ");
        for(int i = front; i <= rear; i++){
            printf("%d\t",queue[i]);
        }
        printf("\n");
    }
}

int main(){
    int choice, item;
    printf("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
    while(1){
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("Enter the element: ");
            scanf("%d",&item);
            enqueue(item);
            break;

        case 2:
            dequeue(item);
             break;

        case 3: 
           display();
            break; 

        case 4:
            printf("Exit\n");
             return 0;

        default:
            printf("Invalid choice!!\n");
        }
    }
}