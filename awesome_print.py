# coding:utf-8

"""
[说明]:
	方便系统中愉快的打印信息，直接引用脚本，打印即可，
	支持命令 log/warning/error/success 
	代码很简单，根据自己的需要可以添加指令
[usage]:
	>>> from awesome_print import *
	>>> log('this is a log')
	[*] this is a log

	>>> warning(['warning', 'balabala'])
	[!] ['warning', 'balabala']

	>>> error({'error', 'msg'})
	[x] set(['msg', 'error'])

	>>> success({'success': 'God bless your code!'})
	[√] {'success': 'God bless your code!'}

"""



COMMANDS = {
	'log': (94, '[*] '),
	'warning': (93, '[!] '),
	'error': (91, '[x] '),
	'success': (92, '[√] '),
}

def _print(var, value, prefix):
	print('\033[{0}m{1}{2}'.format(value, prefix, var))


for k,v in COMMANDS.items():
    locals()[k] = lambda var, value=v[0], prefix=v[1]: _print(var, value, prefix)


__all__ = list(COMMANDS.keys())
