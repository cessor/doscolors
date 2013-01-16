from doscolors import *

global default_color

default_color = current_color()

@background(Colors.red)
def error(text):
	print text

@foreground(Colors.green)
def success(text):
	print text

@colored(Colors.black, Colors.yellow)
def warning(text):
	print text

def manual(text):
	color(Colors.lightcyan, Colors.blue)
	print 'Text'
	reset()

def test():
	success('Success')
	error('Error')
	warning('Warning')
	manual('Manual')
	
if __name__ == '__main__':
	test()
	"Use the decorators to access nice colors."