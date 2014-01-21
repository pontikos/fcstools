import sys
import re
for l in file('/home/nikolas/dunwich/Projects/IL2/pstat5-cb-dgap-2014-01-07.csv','r').readlines():
    s=l.strip().split(';')[0]
    sys.stdout.write(l.strip())
    sys.stdout.write(';')
    if re.compile('.*_0_?U?_?(_IL.)?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write('0U')
    elif re.compile('.*_0?_?1U?_?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write('01U')
    elif re.compile('.*_10U?_?(_(bas|hIgG1|M_A251|mIgG1)_[\d_]+)?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write('10U')
    elif re.compile('.*_100U?_?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write( '100U')
    elif re.compile('.*_1000U?_?(_IL.)?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write('1000U')
    elif re.compile('.*_10000U?_?(IL2_.*)?.fcs', re.IGNORECASE).match(s): sys.stdout.write( '10000U')
    elif re.compile('.*complex.*.fcs').match(s): 
        sys.stdout.write('\n')
        continue
    else:
        print s
        raise 'hell'
    sys.stdout.write('\n')


