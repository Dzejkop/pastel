#include <iostream>

// Necessary for macro and DataBundle structure definition
// Can be generated using the --generate_header option
#include "pastel.h"

PASTEL_COMPILE(test_data, "test_data.txt");

int main()
{
  std::cout << test_data.data;
  return 0;
}
