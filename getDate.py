#!/usr/bin/env python
import sys
import os
import re
import datetime

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
    print datetime.datetime.strptime(fcs_vars['$DATE'],'%d-%b-%Y').strftime('%Y-%m-%d')

    #print '%s' % (','.join([fcs_vars[k] for k in keywords]),)
    #print fcs_vars['FCSVersion']
    #print '%s,%s' % (version, ','.join([fcs_vars[k] for k in keywords]),)
    #print fcs_vars['$FIL'] #: CAD76_2008may22_Treg_I008170E_017.fcs 
    #print fcs_vars['$SYS'] #: Windows XP 5.1 
    #print fcs_vars['CREATOR']# : BD FACSDiva Software Version 6.1.3 
    #print fcs_vars['TUBE NAME']# : I008170E_017 
    #print fcs_vars['$SRC'] # CAD76_2008may22_Treg 
    #print fcs_vars['EXPERIMENT NAME'] # CAD76_2008may22_Treg 
    #print fcs_vars['GUID'] # 91d5f92b-2881-4b5e-8cce-60bb3a2893a8 
    #print fcs_vars['$DATE'] # 22-MAY-2008 
    #print fcs_vars['$BTIM'] # 19:31:06 
    #print fcs_vars['$ETIM'] # 19:32:40 
    #print fcs_vars['$CYT'] # LSRII 
    #print fcs_vars['WINDOW EXTENSION'] # 10.00 
    #print fcs_vars['EXPORT USER NAME'] # User 
    #print fcs_vars['EXPORT TIME'] # 01-APR-2010-11:53:30 
    #print fcs_vars['$OP'] # Administrator 


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


