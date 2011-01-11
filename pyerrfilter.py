#!/usr/bin/env python
import sys
input = sys.stdin.readlines()
print ''.join(input)
message = input.pop()[:-1]
input.reverse()
with open(sys.argv[1], 'wb') as f:
    for line in input:
        if line.find('  File') == 0:
            f.write(line[:-1] + ', ' + message + '\n')
            message = 'Traceback'
