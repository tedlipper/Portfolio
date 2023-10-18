using System;

namespace BetterCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int x = 0; x > -1; x++) 
            {
                if (x > 0)
                {
                    Console.WriteLine("");
                    Console.WriteLine("Running code again . . .");
                }
                //Asking for a number an operator and another number for the calculator to work
                //Converting the numbers inputed into a double also using variables
                Console.Write("Enter a number: ");
                double num1 = Convert.ToDouble(Console.ReadLine());

                Console.Write("Enter Operator (+, -, *, or /): ");
                string op = Console.ReadLine();

                Console.Write("Enter another number: ");
                double num2 = Convert.ToDouble(Console.ReadLine());

                //If else statements to match the printed outcome to the operator given
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
