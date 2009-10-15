import sys
import os

def usage():
	print 'USAGE: %s SNIPPET [OPTIONS...]' % sys.argv[0]

PROJECT_DIR = None
path = os.getcwd()
while path != '/':
	p = os.path.join(path, '.snippets')
	if os.path.isdir(p):
		PROJECT_DIR = p
		break
	path = os.path.dirname(path)
USER_DIR = os.path.join(os.path.expanduser('~'), '.snippets')
SYS_DIR = os.path.join(os.path.dirname(__file__), 'snippets')

class SnippetDoesNotExist:
	pass

def load_snippet(name):
	import imp
	save_path = sys.path
	if PROJECT_DIR:
		sys.path = [PROJECT_DIR, USER_DIR, SYS_DIR]
	else:
		sys.path = [USER_DIR, SYS_DIR]
	try:
		module = imp.find_module(name)
	except ImportError:
		raise SnippetDoesNotExist()
	sys.path = save_path
	return imp.load_module(name, *module)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
		sys.exit(1)
	snippet_name = sys.argv[1]
	try:
		snippet = load_snippet(snippet_name)
	except SnippetDoesNotExist:
		print 'snippet %s does not found' % snippet_name
		exit_code = -1
	else:
		exit_code = snippet.generate(sys.argv[1:]) 
	if not exit_code:
		exit_code = 0
	sys.exit(exit_code)
