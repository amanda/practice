def foo(x):
	return x + 1

l = [foo, foo, foo]
#l[1](2) returns 3

def hello():
	print 'hello'

def do_twice(func):
	func()
	func()

def foo():
	def bar():
		print 'hi'
	return bar

def make_printer(msg):
	def bar():
		print msg
	return bar

def capitalize(func):
	def wrapper():
		return func.upper()
	return wrapper

 
