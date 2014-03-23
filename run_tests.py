import os
from subprocess import call


def main():
	for root, dirs, files in os.walk('./'):
		for file in files:
			if file.startswith('tests'):
				call(['python3', root + '/' + file])


if __name__ == '__main__':
	main()