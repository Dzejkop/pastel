# PaSTeL - Python Static daTa Linker

**Now with 100% more Windows support**

## What is it and how does it work?
`PaSTeL` allows you statically compile files into your binary.
My 3 main goals are for `PaSTeL` to be:
* Easy to use
* Platform independent
* Easy to integrate into your build system

## Features
- [x] Static linking of files on Linux
- [x] Platform independent linking (**untested on OSX**)
- [x] Command line arguments
- [x] Support for multiple source files
- [ ] Extensible configuration
- [x] Easy integration into Makefile
- [ ] Easy integration into CMake
- [ ] Easy integration with Visual Studio
- [ ] Namespaces support

## Requirements
1. Python3

## Usage
Basic:
`python <path_to_pastel.py> -s <src_file_1> -s <src_file_2> -t target_file`

Additional options:

* `--verbose` verbose

* `--generate_header` generates the pastel.h

## Examples
* [Makefile 1](/example)
