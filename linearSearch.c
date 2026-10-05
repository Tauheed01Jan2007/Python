#include<stdio.h>
int  main(){
    int arr[50],search , i , n;
    printf("Enter the array element size: ");
    scanf("%d",&n);
    printf("Enter %d number: \n",n);
    for(i=0; i<n; i++){
        scanf("%d",&arr[i]);
    }
    printf("enter the search: ");
    scanf("%d",&search);
    for(i=0;i<n; i++){
        if(arr[i]==search){
            printf("%d is present at location %d",search,i+1);
            break;
        }
    }
    if(i==n){
        printf("%d is not present",search);
    }
}