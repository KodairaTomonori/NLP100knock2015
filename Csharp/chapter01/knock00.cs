/*
 * Chapter01, knock00
 * Task: Reverse string.
 */

using System;
using System.Collections.Generic;
using System.Linq;

public class ReverseSTring
{
    static public void Main ()
    {
        string word = "stressed";
        string rword = new string(word.Reverse().ToArray());
        Console.WriteLine(rword);
    }
}
