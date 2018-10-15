#! /usr/bin/python
#
# Assembles several TeX files in one. Recursively includes TeX files, substitutes BibTeX bibliography  and strips the TeX comments 
# (i.e., lines starting from "%").
#
# Usage:
#	assemble-latex.py main-tex-file output/dir
#
import sys; 
import glob;
import re;

def process(inputDir, curFile, outfile):
    """
    Note - this works recursively.
    """
    
    print 'Processing ['+curFile+']...'
    for line in open(inputDir+'/'+curFile):
        if line[0] <> '%':
            if line.startswith('\\include{'):
                nextFile = line[len('\include{') : line.rfind('}')]
		if not nextFile.endswith('.tex'):
		    nextFile = nextFile + '.tex'
                process(inputDir, nextFile, outfile)
	    elif line.startswith('\\input{'):
                nextFile = line[len('\input{') : line.rfind('}')]
		if not nextFile.endswith('.tex'):
		    nextFile = nextFile + '.tex'
                process(inputDir, nextFile, outfile)
            elif line.startswith('\\bibliography{'):
                # Include all bbl files from the input directory
		for nextFileFullname in glob.glob(inputdir + '/*.bbl'):
                    nextFile = nextFileFullname[nextFileFullname.rfind('/')+1 : ]
                    process(inputDir, nextFile, outfile)
            else:
                outfile.write(line)

def usage(err):
    print """
Assembles several TeX files in one. Recursively includes TeX files, substitutes BibTeX bibliography  and strips the TeX comments 
(i.e., lines starting from "%").
Usage:
    assemble-latex.py main-tex-file output/dir
"""
    sys.exit(err)
    
def main(argv):

    if len(argv) == 2 and argv[1] in ['-h', '-?', '-help', '--help']:
        usage(0)
    if len(argv) != 3:
        usage(1)

    try:
        # get the trailing name 
        inputfilenameFull = argv[1];   
        outputdir = argv[2];
        inputfilename = inputfilenameFull[inputfilenameFull.rfind('/')+1 : ]
        inputdir = inputfilenameFull[ : inputfilenameFull.rfind('/')]
        outfile = open(outputdir+'/'+inputfilename, 'w')
        process(inputdir, inputfilename, outfile)
        outfile.close()
    except:
        sys.stderr.write("failed\n")
        raise
							    
if __name__ == '__main__':
    main(sys.argv)
