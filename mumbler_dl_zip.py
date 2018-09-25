from subprocess import call
import argparse

list1 = [x for x in range(0,33)]
list2 = [x for x in range(33,67)]
list3 = [x for x in range(67,100)]

worker_list = [list1,list2,list3]

parser = argparse.ArgumentParser(prog="hw4 mumbler",
                                     description="a mumber")

parser.add_argument('-m', '--machinenumber', nargs='?', type=int, required=True,
                     help='Date running report', dest='machine')
args = parser.parse_args()

def download_2gram(number):
	call(["wget","-O","/gpfs/gpfsfpo/2gram-{number}.csv.zip".format(number=number),
		"http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20090715-{number}.csv.zip".format(number=number)])

active_list = worker_list[args.machine]
for num in active_list:
    download_2gram(num)
