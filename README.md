# w251_studentwork
Repo to store work for W251

Files:

	mumbler_dl_zip.py: Python script to download all 100 zip.csv files from the google ngram dataset.  Argument
			   is used to specify which machine, to control which files are downloaded where.

	gpfs_preprocess.sh: Shell script designed to take zip file, select only rows with 2 valid words, and then aggregate
			    the quantity column, while dropping all other columns.  One file for each machine to process
			    the files which were downloaded on that node.
	
	gpfs_preprocess_2:  Shell script designed do take output from gpfs_preprocess files and create a single file for each letter.  				  This enables mumble.py to grep through only a single file based on first letter of the word.

	mumble.py: Python script which takes a beginning word and length, and generates random text by selecting a random
		   second word from the 2grams which start with input word, weighted by the frequency of that word.  The 
		   new word is then used to restart the process.
