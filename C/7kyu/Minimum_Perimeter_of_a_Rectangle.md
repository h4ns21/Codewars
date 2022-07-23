```c
#include <math.h>
typedef unsigned long long ull;

ull minimum_perimeter(area) {
  int l;
  int w;
  l = sqrt(area);  // square root of the area
  while (area % l != 0) {
    l -= 1;  // find the next lowest integer that evenly divides the area
  }
  w = area / l;  // get the corresponding width
  return (2 * l + 2 * w); // get the perimeter
```
