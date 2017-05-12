#include <iostream>

// Necessary for macro and DataBundle structure definition
// Can be generated using the --generate_header option
#include "pastel.h"

#include "test.h"

PASTEL_COMPILE(test_data, "test_data.txt"); // This comment will not interfere with parsing

// This macro will not be parsed
// PASTEL_COMPILE(derp_data, "derp_data.txt");

int main()
{
  std::cout << test_data.data;

  Test::test_display();

  return 0;
}
