#include <iostream>

#ifndef COMPILE_IN_DATA_FILE
#define COMPILE_IN_DATA_FILE(name, path) extern unsigned char name[]
#endif

COMPILE_IN_DATA_FILE(data, "the_raven.txt");
COMPILE_IN_DATA_FILE(test_data, "test_data.txt");
COMPILE_IN_DATA_FILE(bird_file, "bird.jpg");

int main()
{
  std::cout << test_data;

  return 0;
}
