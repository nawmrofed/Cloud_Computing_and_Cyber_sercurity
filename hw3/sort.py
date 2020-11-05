#! /usr/bin/env python3
import apache_log_parser
import sys

line_parser = apache_log_parser.make_parser('%h - - %t "%r" %s %b')
for line in sys.stdin:
    print(line_parser(line)["time_received_isoformat"].split(':')[0]+'\t'+'1')
    
