# include <stdio.h>
int main()  {
    char operator;
 char answer; 
    float num1,num2,f,m; 
 int n,i,e,sum=0,mul=1,b,p,x=1,t=1,a,fact=1,y=1;
    printf("Enter operator either + or - or * or / or ^ or ! : ");
    scanf("%c",&operator);
switch(operator) { 
        case '+': 
     printf("Enter no of numbers you want to add:\n");
     scanf("%d",&n);
  printf("Enter the numbers:\n");
  for(i=0;i<n;i++)
  {
     scanf("%f",&f);
     sum+=f;      
                   
  }      
        printf("sum of two numbers=%d",sum);     
        break; 
        case '-':
   printf("Enter two numbers:\n");
     scanf("%f %f",&num1,&num2);
  printf("Difference between two numbers=%.2f",num1-num2);
        break; 
        case '*':
          printf("Enter no of numbers you want to multiply:\n");
     scanf("%d",&n);
  printf("Enter the numbers:\n");
  for(i=0;i<n;i++)
  {
     scanf("%f",&m);
     mul*=m;      
                   
  }      
        printf("Multiplication of two numbers=%d",mul);
        break;
        case '/':
     printf("Enter two numbers:\n");
     scanf("%f %f",&num1,&num2);
  printf("Division between two numbers=%.2f",num1/num2);
        break;
  case'^':
  printf("Enter the base:\n");
  scanf("%d",&b);
  printf("Enter the power:\n");
  scanf("%d",&p);
  while(x<=p)
        {
            t*=b;
            x++;
        }
  printf("%d^%d=%d",b,p,t);
  break;
  case'!':
  printf("Enter the num:\n");
  scanf("%d",&a);
  while(y<=a)
        {
          fact*=y;
          y++;  
        }
  printf("%d!=%d",a,fact);
  break;                  
     default: 
        printf("Error! operator is not correct");
        break;
}}
