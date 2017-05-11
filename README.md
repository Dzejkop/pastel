# C++ - using python to compile files into executables

## Requirements
**Only tested on Linux**
1. Python3
1. g++

## Usage
Running the parse.py on a .cpp file will cause it to generate an .s file with encoded data for any `COMPILE_IN_DATA_FILE` macro encountered.

## Example
```
> python3 parse.py source.cpp temp.s
> g++ temp.s source.cpp -o O
> rm temp.s
> ./O
```

# Stuff
[The bird image](https://upload.wikimedia.org/wikipedia/commons/8/88/Arthur_(hi_res).jpg)
