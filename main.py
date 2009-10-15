import sys
import os

def usage():
	print 'USAGE: %s SNIPPET [OPTIONS...]' % sys.argv[0]

SNIPPETS_PATH = []
user_home = os.path.join(os.path.expanduser('~'))

# Project snippets.
path = os.getcwd()
while path != '/':
	p = os.path.join(path, '.snippets')
	if os.path.isdir(p):
		SNIPPETS_PATH.append(p)
		break
	path = os.path.dirname(path)

# User snippets.
SNIPPETS_PATH.append(os.path.join(user_home, '.snippets'))

# System snippets.
SNIPPETS_PATH.append(os.path.join(os.path.dirname(__file__), 'snippets'))

# Default user package.
SNIPPETS_PATH.append(os.path.join(user_home, '.snippets/default'))

class SnippetDoesNotExist:
	pass

def load_snippet(name):
	import imp
	parts = name.split('.')
	if len(parts) > 1:
		package_path = os.path.join(*parts[:-1])
	else:
		package_path = ''
	module_name = parts[-1]
	search_path = [os.path.join(p, package_path) for p in SNIPPETS_PATH]
	try:
		module = imp.find_module(module_name, search_path)
	except ImportError:
		raise SnippetDoesNotExist()
	return imp.load_module(module_name, *module)

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

# vim:set ft=python ts=4 sw=4 tw=79 noet: 
