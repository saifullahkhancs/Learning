using System;

class Program
{
    static string ReverseString(string input)
    {
        char[] charArray = input.ToCharArray();
        int start = 0;
        int end = input.Length - 1;

        while (start < end)
        {
            char temp = charArray[start];
            charArray[start] = charArray[end];     // charArray[start]  , charArray[end]= charArray[end] , charArray[end];   why it is not possible
            charArray[end] = temp;
            start++;
            end--;
        }

        return new string(charArray);
    }

    static void Main(string[] args)
    {
        string input = "Hello, world!";
        string reversed = ReverseString(input);
        Console.WriteLine("Reversed string: " + reversed);
    }
}


// Without using third variable 

// using System;

// class Program
// {
//     static string ReverseString(string input)
//     {
//         char[] charArray = input.ToCharArray();
//         int start = 0;
//         int end = input.Length - 1;

//         while (start < end)
//         {
//             // Swap characters without using a third variable
//             charArray[start] = (char)(charArray[start] + charArray[end]);
//             charArray[end] = (char)(charArray[start] - charArray[end]);
//             charArray[start] = (char)(charArray[start] - charArray[end]);

//             start++;
//             end--;
//         }

//         return new string(charArray);
//     }

//     static void Main(string[] args)
//     {
//         string input = "Hello, world!";
//         string reversed = ReverseString(input);
//         Console.WriteLine("Reversed string: " + reversed);
//     }
// }

