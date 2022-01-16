#!/usr/bin/env python3

import gen
import os

tpuser = os.environ['TPUSER']
tphost = os.environ['TPHOST']

works_cats, years = gen.load_data()
gen.gen_works(works_cats)
gen.gen_timeline(years)

os.system('make html')
#os.system('rsync -avz -e "ssh -l %s" output/* %s@%s:~/www/thomaspaine/' % (tpuser, tpuser, tphost))
