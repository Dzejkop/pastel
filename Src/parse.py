import os
import sys
import re

data_header_template = """.globl %(name)s
.section .rodata
.p2align 5
.type %(name)s, "object"
.size %(name)s, %(size)d
%(name)s:
"""

data_part_template = "    .byte %(data)d\n"

def write_symbol_name(symbol_name, size, target_file):
    target_file.write(data_header_template % {'name': symbol_name, 'size' : size})

def write_symbol_data(symbol_name, data, target_file):
    for byte in data:
        target_file.write(data_part_template % {'data': byte})

def write_symbol(symbol_name, symbol_data, target_file):
    write_symbol_name(symbol_name, len(symbol_data), target_file)
    write_symbol_data(symbol_name, symbol_data, target_file)

CONFIG_ROW_WIDTH = 10

def write_symbol_cpp_style(symbol_name, symbol_data, target_file):
    target_file.write("unsigned char %(name)s[] = {\n" % {'name' : symbol_name})

    current_column = 0
    for byte in symbol_data:
        target_file.write("0x%(b)X," % {'b' : byte})
        current_column += 1
        if current_column >= CONFIG_ROW_WIDTH:
            current_column = 0
            target_file.write("\n")

    target_file.write("};\n")

def read_whole_file(path):
    with open(path, 'rb') as f:
        return f.read()

if len(sys.argv) != 3:
    print ("Invalid number of arguments.")
    print ("Expected 2 arguments the .cpp source file and target .s file.")

cpp_src = sys.argv[1]
asm_target = sys.argv[2]

MACRO_REG=r'COMPILE_IN_DATA_FILE\((.*),\"(.*)\"\);'

matches = [re.findall(MACRO_REG, line.replace(' ', '')) for line in open(cpp_src)]

asm_temp = open(asm_target, 'w')

for m in matches:
    if (len(m) != 0):
        print ("Var name: %s" % m[0][0])
        print ("File name: %s" % m[0][1])

        file_contents = read_whole_file(m[0][1])

        write_symbol_cpp_style(m[0][0], file_contents, asm_temp)
