#! /usr/bin/python
import sys
import os

def main(arg):
	dir1 = arg[0];
	dir2 = arg[1];	
	for subdir, dirs, files in os.walk(dir1):
		for file in files:
			if file.endswith('.c') or file.endswith('.h') or file.endswith('.S'):
				file1_path = os.path.join(subdir, file)
				file2_path = dir2 + file1_path[len(dir1):];
				ret = os.system('diff '+ file1_path + ' ' +file2_path);
				if ret != 0:
					print file1_path;
					print file2_path;
					print '\n';
		


if __name__ == '__main__':
	main(sys.argv[1:]);
