# This script automatically changes the Memo field in the OFX file to NAME and saves it with a new name containing the date

import re
from datetime import datetime

##Get date for filename
now = datetime.now() # current date and time
shortdate = now.strftime("%Y%m%d")

out_filename = "CC_" + shortdate +".ofx"
in_filename = "490115______2000.ofx"
#out_filename = "490115______2000_test.ofx"



with open(in_filename, 'r+') as f, open(out_filename, 'x+') as o: #Check if output file exist, if yes then raise an error
    text = f.read()
    text = re.sub('<MEMO>', '<NAME>', text)
    f.seek(0)
    o.write(text)
##    ##f.truncate()
