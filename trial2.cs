using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.CursorVisible = false;

        List<string> options = new List<string> { "Option 1", "Option 2", "Option 3", "Option 4", "Option 5" };
        int selectedIndex = 0;

        ConsoleKeyInfo key;
        do
        {
            Console.Clear();
            DrawDropdown(options, selectedIndex);

            key = Console.ReadKey(true);

            switch (key.Key)
            {
                case ConsoleKey.UpArrow:
                    selectedIndex = (selectedIndex - 1 + options.Count) % options.Count;
                    break;
                case ConsoleKey.DownArrow:
                    selectedIndex = (selectedIndex + 1) % options.Count;
                    break;
            }
        } while (key.Key != ConsoleKey.Enter);

        Console.Clear();
        Console.WriteLine("Selected option: " + options[selectedIndex]);
    }

    static void DrawDropdown(List<string> options, int selectedIndex)
    {
        for (int i = 0; i < options.Count; i++)
        {
            Console.SetCursorPosition(2, i + 2);

            if (i == selectedIndex)
            {
                Console.BackgroundColor = ConsoleColor.Gray;
                Console.ForegroundColor = ConsoleColor.Black;
            }

            Console.Write(options[i].PadRight(20));

            Console.ResetColor();
        }
    }
}
