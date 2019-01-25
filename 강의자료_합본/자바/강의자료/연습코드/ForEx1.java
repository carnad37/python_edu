package com.javab.test1;

public class MainApp {
	public static void main(String[] args)
	{
		/*
		if(조건식) {
			
		}
		
		for(초기화식 ; 조건식 ; 증감식) {
			실행문;
		}
		*/
//		int sum=0;
//		int i=0;
//		for(i=1; i<11 ; i++) {
//			System.out.println("- i : "+i);
//			if(i%3==0) {
//				System.out.println(" > i : "+i);
//				sum+=i;	
//			}
//		}
		
//		int sum=0;
//		int i=0;
//		for(i=3; i<11 ; i+=3) {
//			System.out.println("i : "+i);
//			sum+=i; // sum = sum +i;
//		}
		
//		int sum=0;
//		int i=0;
//		int counter=0;
//		double avg=0;
//		for(i=1; i<11 ; i++) {
//			
//			sum+=i; // sum = sum +i;
//			counter++;
//		}
//		
//		avg = (double)sum/counter;
//		System.out.println("sum : "+sum);
//		System.out.println("counter : "+counter);
//		System.out.println("avg : "+avg);
//		
		
		//1. 두개의 수를 입력받고
		int a=2,b=6;
		//2. 어떤수가 큰지, 작은지를  찾아냄
		int min=0, max=0;
		int i=0;
		if(a>b)
		{
			
			min = b;
			max = a;
		}
		else
		{
			min = a;
			max = b;
		}
		System.out.println(min +", "+max);
		//3. 초기화식에 작수의 값을 넣어주고 
		//조건식의 범위값에 큰수 
		for(i=min;i<=max;i++)
		{
			System.out.println("i : "+i);
		}
		
		
		
		
		
		
		
				
	}

}
