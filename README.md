# Awesome-print

## 说明:

方便系统中愉快的打印信息，直接引用脚本，打印即可，

支持命令 log/warning/error/success 

代码很简单，根据自己的需要可以添加指令

## 使用:

```python
>>> from awesome_print import *
>>> log('this is a log')
[*] this is a log

>>> warning(['warning', 'balabala'])
[!] ['warning', 'balabala']

>>> error({'error', 'msg'})
[x] set(['msg', 'error'])

>>> success({'success': 'God bless your code!'})
[√] {'success': 'God bless your code!'}
```

## 截图：

![awesome-print](http://opbkao85k.bkt.clouddn.com/awesome-print.png)

## License

MIT