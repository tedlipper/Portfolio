public class Reference 
{
	//This is a comment
	//This is an example of a function
	static void FunctionExample() 
	{
		//This is a print statement that prints "This is a function example!"
		System.out.println("This is a function example!");
	}
	
	//Bubble sort algorithm
		//1 Gets array length
		//2 Initialise variables i and j
			//i = current number in the array
			//j = next number in the array
		//3 Traverse the array and if i>j swap the numbers
		//4 Loop until sorted
    	static void bubbleSort(int arr[])
    	{
		//Sets the variable n to be the array length
        	int n = arr.length;
        	//i = current number in the array
        	for (int i = 0; i < n - 1; i++)
		{
			//j = next number in the array
        		for (int j = 0; j < n - i - 1; j++)
			{
        	    		//Compares the elements in the array and swaps the elements if they're out of order
        	        	if (arr[j] > arr[j + 1]) 
        	        	{
        	           		// swap arr[j+1] and arr[j]
        	            		int temp = arr[j];
        	            		arr[j] = arr[j + 1];
        	            		arr[j + 1] = temp;
        	        	}
			}
		}
    	}
    	//Function that prints the array
    	static void printArray(int arr[])
    	{
		//Sets n to the array length
        	int n = arr.length;
		//Iterates through the array and prints each element
        	for (int i = 0; i < n; ++i)
        	    System.out.print(arr[i] + " ");
        	System.out.println();
    	}
	public static void main(String[] args)
	{


		//this is a variable
		String x = "this is a variable";
		System.out.println(x);
		System.out.println("this is a statement");
		//this is a for loop that counts to ten
		System.out.println("For loop");
		for (int i = 1; i <= 10; i = i + 1) 
		{
			System.out.print(i);
			System.out.print(" ");
		}
		System.out.println();
		//this is a while loop that counts to ten
		System.out.println("While loop");
		int i = 0;
		while (i < 10) 
		{
			System.out.print(i+1);
			System.out.print(" ");
			i++;
		}
		System.out.println();
		//declares an array
     		int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        	//prints every element in the array
        	System.out.println("For each loop");
        	for (int element : ar)
		{
            		System.out.print(element + " ");
		}
		System.out.println("");
        
		//self explanatory name
		FunctionExample();
		
        //initializes the unsorted array
        int arr[] = { 5, 1, 4, 2, 8 };
        //prints the unsorted array
        System.out.println("Unsorted array");
        printArray(arr);
        
        //calls the bubble sort method
        bubbleSort(arr);
        //prints the sorted array
        System.out.println("Sorted array");
        printArray(arr);
	}
	
}
