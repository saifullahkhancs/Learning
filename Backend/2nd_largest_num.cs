using System;

class Program
{
    static int SecondLargest(int[] numbers)
    {
        if (numbers.Length < 2)
        {
            return -1;
        }

        int largest;
        int second_largest;

        if (numbers[0] >= numbers[1])
        {
            largest = numbers[0];
            second_largest = numbers[1];
        }
        else
        {
            largest = numbers[1]; // Corrected
            second_largest = numbers[0]; // Corrected
        }

        for (int i = 2; i < numbers.Length; i++)
        {
            int num = numbers[i];

            if (num > largest)
            {
                second_largest = largest;
                largest = num;
            }
            else if (num > second_largest)
            {
                second_largest = num;
            }
        }

        return second_largest;
    }

    static void Main(string[] args)
    {
        int[] numbers = { 10, 20, 30, 40, 50 };
        Console.WriteLine("Second largest number: " + SecondLargest(numbers));
    }
}

// using system;
// class Program
// {
//     static int SecondLargest(int[] numbers)
//     {
//         if (numbers.Length < 2)
//         {
//             return -1;
//         }

//         // int num1 = numbers[0];
//         // int num2 = numbers[1];
//         int largest;
//         int second_largest;

//         if (numbers[0] >= numbers[1]){
//             largest = numbers[0];
//             second_largest = numbers[1];
//         }
//         else{

//             largest = numbers[0];
//             second_largest = numbers[1]

//         }

//         for (int i = 2; i < numbers.Length; i++)
//         {
//             int num = numbers[i];

//             if (num > largest)
//             {
//                 second_largest = largest;
//                 largest = num;
//             }

//             else if (num > second_largest)
//             {
//                 second_largest = num;
//             }

//         }

//         return second_largest;
//     }

// }

// static void Main(string[] args)
// {
//         int[] numbers = { 10, 20, 30, 40, 50 };
//         Console.WriteLine("Second largest number: " + SecondLargest(numbers));
// }