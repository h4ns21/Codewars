```c
using System;

namespace Solution
{
  public static class Program
  {
    public static int[] reverseList(int[] list)
    {
      if (list == null) return null;
      Array.Reverse(list);
      return list;
    }
  }
}
```

