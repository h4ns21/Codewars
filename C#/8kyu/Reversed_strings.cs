using System;

public static class Kata
{
  public static string Solution(string text) 
  {
    if (text == null) return null;
    char[] array = text.ToCharArray();
    Array.Reverse(array);
    return new String(array);
  }
}
