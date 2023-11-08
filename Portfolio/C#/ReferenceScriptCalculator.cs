using System;

namespace BetterCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            //Setting up the for loop so the code can be run repeatedly
            for (int x = 0; x > -1; x++) 
            {
                //Checking if the code has run more than once
                if (x > 0)
                {
                    Console.WriteLine("");
                    Console.WriteLine("Running code again . . .");
                }
                //Asking for a number an operator and another number for the calculator to work
                //Converting the numbers inputed into a double also using variables
                Console.Write("Enter a number: ");
                double num1 = Convert.ToDouble(Console.ReadLine());
                //Asking for an operator
                Console.Write("Enter Operator (+, -, *, or /): ");
                string op = Console.ReadLine();
                //Asking for another number
                Console.Write("Enter another number: ");
                double num2 = Convert.ToDouble(Console.ReadLine());

                //If else statements to print the outcome to the operator and numbers given
                if (op == "+")
                {
                    Console.WriteLine("The answer is " + (num1 + num2));
                }
                else if (op == "-")
                {
                    Console.WriteLine("The answer is " + (num1 - num2));
                }
                else if (op == "*")
                {
                    Console.WriteLine("The answer is " + (num1 * num2));
                }
                else if (op == "/")
                {
                    Console.WriteLine("The answer is " + (num1 / num2));
                }
                else
                {
                    Console.WriteLine("Invalid operator try again!");
                }
            } 
        }
    }
}
