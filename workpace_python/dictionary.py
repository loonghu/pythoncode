>>> 'a'*2
'aa'
>>> b=2**999
>>> b
5357543035931336604742125245300009052807024058527668037218751941851755255624680612465991894078479290637973364587765734125935726428461570217992288787349287401967283887412115492710537302531185570938977091076523237491790970633699383779582771973038531457285598238843271083830214915826312193418602834034688L
>>> a=2**1000
>>> a
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376L
>>> 3/5
0
>>> 3.0/5
0.6
>>> 2L
2L
>>> a/b
2L
>>> x=0.1
>>> x
0.1
>>> x=0.1
>>> x
0.1
>>> s=0.0
>>> import math
>>> 
>>> counts={'chuck':1,'fred':42,'jan':100}
>>> for key in counts
SyntaxError: invalid syntax
>>> for key in counts:
	print key, counts[key]

	
jan 100
chuck 1
fred 42
>>> counts={'chuck':1,'fred':42,'jan':100}
>>> 
>>> for aaa,bbb in counts.items();
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> counts={'chuck':1,'fred':42,'jan':100}:
	
SyntaxError: invalid syntax
>>> for aaa,bbb in counts.items():
	print aaa,bbb

	
jan 100
chuck 1
fred 42
>>> jjj=list(counts)
>>> print jjj
['jan', 'chuck', 'fred']
>>> print jjj.values()

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print jjj.values()
AttributeError: 'list' object has no attribute 'values'
>>> print jjj.value()

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print jjj.value()
AttributeError: 'list' object has no attribute 'value'
>>> name=raw_input("Enter file:"):
	
SyntaxError: invalid syntax
>>>  name=raw_input("Enter file:")
 
  File "<pyshell#35>", line 1
    name=raw_input("Enter file:")
   ^
IndentationError: unexpected indent
>>> name=raw_input("Enter file:"):
	
SyntaxError: invalid syntax
>>> name=raw_input("Enter file:")
Enter file:d:\site.txt
>>> print name
d:\site.txt
>>> handle = open(name,'r')
>>> text=handle.read()
>>> words=text.split()
>>> print words
['http://mariosandreou.com/deltacloud/2012/02/15/deltacloud-opennebula.html', 'https://pypi.python.org/pypi/oca/0.2.3', 'http://sourceforge.net/projects/xenman/', 'http://sourceforge.net/projects/openqrm/', 'http://www.qyjohn.net/?p=1263', 'http://download.opensuse.org/repositories/devel:/languages:/ruby:/extensions/openSUSE_12.2/x86_64/', 'http://bundler.io/', 'https://download.suse.com/patch/finder/?keywords=480d98ab926aa6d71214ec344385e860', 'http://redmine.ogf.org/projects/editor/wiki/About_OGF_Documents', 'http://occi-wg.org/', 'https://github.com/gwdg', 'http://occi-wg.org/community/implementations/', '\xd0\xa1\xc4\xbe\xc7\xc5\xc2\xb7\xa3\xba251', '\xba\xc5', '7.30']
>>> cours=dict()
>>> for word in words:
	cours[word]=cours.get(word,0)+1

	
>>> bigcount=None
>>> bigword=None
>>> for word,count in cours.items():
	if bigcount is None or count > bigcount:
		bigword=word
		bigcount=count

		
>>> print bigcount,bigword
1 http://mariosandreou.com/deltacloud/2012/02/15/deltacloud-opennebula.html
>>> for word,count in cours.items():
	if bigcount is None or count > bigcount:
		bigword=word
		bigcount=count

		
>>> 
>>> ccc=dict()
>>> ccc['csen']=1
>>> ccc['cwen']=1
>>> print ccc
{'csen': 1, 'cwen': 1}
>>> ccc['cwen']=ccc['cwen']+1
>>> print ccc
{'csen': 1, 'cwen': 2}
>>> 

>>> 
>>> counts=dict()
>>> names=['java','php','r','java']
>>> for name in names:
	if name not in counts:
		counts[name]=1

		
>>> for name in names:
	if name not in counts:
		counts[name]=1
		else:
			
SyntaxError: invalid syntax
>>> for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1

		
>>> print counts
{'r': 2, 'php': 2, 'java': 3}
>>> print counts
{'r': 2, 'php': 2, 'java': 3}
>>> print counts
{'r': 2, 'php': 2, 'java': 3}
>>> 
>>> 
>>> 
>>> print counts
{'r': 2, 'php': 2, 'java': 3}
>>> if name in counts:
	print counts[names]
	else:
		
SyntaxError: invalid syntax
>>> if name in counts:
	print counts[names]
    else:
	    
  File "<pyshell#88>", line 3
    else:
        ^
IndentationError: unindent does not match any outer indentation level
>>> if name in counts:
	print counts[names]
    else:
	    
  File "<pyshell#89>", line 3
    else:
        ^
IndentationError: unindent does not match any outer indentation level
>>> 
>>> 
>>> 
>>> counts2=dict()
>>> names=['12','1','22','12']
>>> for name in names:
	counts2[name]=counts2.get(name,0)+1

	
>>> print counts2
{'1': 1, '12': 2, '22': 1}
>>> 
