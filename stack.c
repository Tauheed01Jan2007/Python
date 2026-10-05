#include<stdio.h>
#define size 5
int stack[size];
int top = -1;

void push(int value){
    if(top ==size - 1){
        printf("stack is full !! OVERFLOW conditions\n");
    }
    else{
        top = top + 1;
        stack[top] = value;
        printf("%d, Inserted item\n",value);
    }
}
void pop(){
    if (top == -1){
        printf("Stack is empty !! UNDERFLOW condition\n");
    }
    else{
        int value = stack[top];
        top = top - 1;
        printf("%d, Item is Deleted\n",value);
    }
}
void display(){
    if (top == -1){
        printf("the Stack is empty!!\n");
    }
    else{
        printf("Stack element: ");
        for(int i = 0; i <= top; i++){
            printf("%d\t",stack[i]);
        }
        printf("\n");
    }
}

int main(){
    int choice, value;
    printf("1. Push\n2. Pop\n3. Display\n4. Exit\n");
    while(1){
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch (choice)
        {
          case 1:
            printf("Enter value to push: ");
            scanf("%d",&value);
            push(value);
            break;
          case 2:
            pop();
            break;
          case 3:
             display();
             break;
          case 4:
             return 0;
          default:
             printf("Invalid choice\n");
        }
    }
}