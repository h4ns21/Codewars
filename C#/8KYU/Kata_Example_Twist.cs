using System;

public static class Kata 
{
  public static string[] Websites = new String[1000];
  static Kata()
  {
      for(int i = 0; i < 1000; i++)
          Websites[i] = "codewars";
  }
}
