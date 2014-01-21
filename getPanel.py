#!/usr/bin/env python
import sys
import os
import re

def fcsextract(filename, keywords):
    """
    Attempts to parse an FCS (flow cytometry standard) file
    Parameters: filename
        filename: path to the FCS file
    """
    fcs_file_name = filename
    fcs = open(fcs_file_name,'rb')
    header = fcs.read(58)
    version = header[0:6].strip()
    text_start = int(header[10:18].strip())
    text_end = int(header[18:26].strip())
    fcs.seek(text_start)
    # First byte of the text portion defines the delimeter
    delimeter = fcs.read(1)
    text = fcs.read(text_end-text_start+1)
    #Variables in TEXT portion are stored "key/value/key/value/key/value"
    keyvalarray = text.split(delimeter)
    fcs_vars = {}
    fcs_var_list = []
    # iterate over every 2 consecutive elements of the array
    for k,v in zip(keyvalarray[::2],keyvalarray[1::2]):
        fcs_vars[k] = v
        fcs_var_list.append((k,v)) # Keep a list around so we can print them in order
    print ','.join(sorted([re.sub('[\s\(\)]+','-',fcs_vars[k].strip().upper()) for k in filter(re.compile('\$P(\d+)S').match, fcs_vars.keys())]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fcs_file_name = sys.argv[1]
    else:
        print "Usage: python %s path\n" % sys.argv[0]
        print "    path: path to the fcs file or a directory"
        sys.exit(1)
    if os.path.isfile(fcs_file_name):
        #fcsextract(fcs_file_name, keywords=('$FIL', '$DATE','TUBE NAME'))
        fcsextract(fcs_file_name, keywords=('$FIL', '$DATE', '$BTIM', '$ETIM', 'TUBE NAME','GUID'))
    else:
        print fcs_file_name, "is not a valid file!"





