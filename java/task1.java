import java.util.*;
public class solution{
public static int add (int a,int b){
while (b!=0){
int carry=a&b;
a=a^b;
b=carry <<1;
}
return 0;
}
public static void main (String[]args){
int num1=10;
int num2=5;
System.out.println("Sum: "+add(num1,num2));
}
}