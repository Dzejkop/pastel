#include "test.h"
#include "pastel.h"
#include <iostream>

PASTEL_COMPILE(d1, "data.txt");

void Test::test_display()
{
  std::cout << d1.data << std::endl;
}
