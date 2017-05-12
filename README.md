# PaSTeL - Python Static daTa Linker

**Now with 100% more Windows support**

## What is it and how does it work?
`PaSTeL` allows you statically compile files into your binary.
My 3 main goals are for `PaSTeL` to be:
* Easy to use
* Platform independent
* Easy to integrate into your build system

## Features
- [x] Staic linking of files on Linux
- [x] Platform independent linking (**untested on OSX**)
- [x] Command line arguments
- [ ] Support for multiple source files
- [ ] Extensible configuration
- [ ] Easy integration into Makefile
- [ ] Easy integration into CMake

## Requirements
1. Python3

## Usage
Basic:
`python <path_to_pastel.py> -s <src_file> -t target_file`

Additional options:

* `-v` verbose

* `--generate_header` generates the pastel.h

## Example
**Project structure**
```
dir:
    source.cpp
    test_data.txt
    pastel.py
```

**source.cpp**
```cpp
#include <iostream>

// Necessary for macro and DataBundle structure definition
// Can be generated using the --generate_header option
#include "pastel.h"

COMPILE_IN_DATA_FILE(test_data, "test_data.txt");

int main()
{
  std::cout << test_data.data;
  return 0;
}
```

**test_data.txt**
```
Hello World!
```

**Commands**
```
> python pastel.py -s source.cpp -t data.cpp --generate_header
> g++ source.cpp data.cpp -o O
> rm data.cpp
> ./O
```

**Program output**
```
Hello World!
```
