# tex-tools

## assemble-latex.py

Assembles several TeX files in one. Recursively includes TeX files, substitutes BibTeX bibliography and strips the TeX comments (i.e., lines starting from "%"). This can be useful to do before submission of an article for publication.

Usage:
	assemble-latex.py main-tex-file output/dir

## strip-tex-comments.py

Strips the TeX comments (i.e., lines starting from "%") from all the files in the given directory.

Usage:
	strip-tex-comments.py /path/to/dir/with/tex-files/ output/dir
