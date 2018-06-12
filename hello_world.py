from monkey import print_monkeys
import sys
# -*- coding:utf-8 -*-
def print_rabbit_range(num):
              for i in range(num):
                  sys.stdout.write(' \\/ ')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write(' oo ')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write(' ** ')
              sys.stdout.write('\n')

def print_palmtrees(num):
              for i in range(num):
                  sys.stdout.write(' /|\\')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write('  | ')
              sys.stdout.write('\n\n')

if __name__ == "__main__":
	print('Hello Monkeys')
	print('I think I already understood the basic concept of add and commit')
	print('But how can git recognize it is the same file if both name and some of the content changed? Is there a limit?')
	print_monkeys([0,1,2,3,4,5])
	print_palmtrees(10)
	print_rabbit_range(7)
