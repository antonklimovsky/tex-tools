#! /usr/bin/python
#
# Strips the TeX comments (i.e., lines starting from "%") from all the files in the given directory.
#
# Usage:
#	strip-tex-comments.py /path/to/dir/with/tex-files/ output/dir
#
import sys; 
import glob;
import re;

inputdir = sys.argv[1];
outputdir = sys.argv[2];
list = glob.glob(inputdir + "*.tex")

for file in list:
    print 'Processing [' + file + ']...'

    # get the trailing name    
    outputfilename = file[file.rfind('/')+1:]
    
    outfile = open(outputdir + outputfilename, 'w')

    # filter out the commented lines 
    for line in open(file):
	if line[0] <> '%':
    	        outfile.write(line)
    outfile.close()