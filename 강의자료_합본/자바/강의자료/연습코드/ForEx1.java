package com.javab.test1;

public class MainApp {
	public static void main(String[] args)
	{
		/*
		if(���ǽ�) {
			
		}
		
		for(�ʱ�ȭ�� ; ���ǽ� ; ������) {
			���๮;
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
		
		//1. �ΰ��� ���� �Է¹ް�
		int a=2,b=6;
		//2. ����� ū��, ��������  ã�Ƴ�
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
		//3. �ʱ�ȭ�Ŀ� �ۼ��� ���� �־��ְ� 
		//���ǽ��� �������� ū�� 
		for(i=min;i<=max;i++)
		{
			System.out.println("i : "+i);
		}
		
		
		
		
		
		
		
				
	}

}
