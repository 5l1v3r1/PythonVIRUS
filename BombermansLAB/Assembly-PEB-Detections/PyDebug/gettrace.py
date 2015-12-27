"""
    Get the trace function as set by settrace().
    CPython implementation detail: 
    The gettrace() function is intended only for implementing debuggers, profilers, coverage tools and the like. 
    Its behavior is part of the implementation platform, rather than part of the language definition, 
    and thus may not be available in all Python implementations.
  #So as you can see we can use that function easly for our purpose.

While searching more about that function I saw little comment on stackoverflow ;
- "Though it seems to be a cleaner way, it does not work in pdb if there is no breakpoint set"
Well after more research, I found public techniques for that.
"""

from sys import gettrace
from inspect import stack

def pydbg():
  if gettrace() != None:
    return True
  else:
    for frame in stack():
	    if frame[1].endswith("pydevd.py") or frame[1].endswith("pdb.py"):
	        return True
"""
Well now you must think "how working that"  ? .. Lets open that stack() function in pdb and see what's happen.

        (Pdb) import inspect
        (Pdb) for frame in inspect.stack():
        *** SyntaxError: unexpected EOF while parsing (<stdin>, line 1)
        (Pdb) print inspect.stack()
        [(<frame object at 0xb741241c>, '<stdin>', 1, '<module>', None, None), (<frame object at 0xb73f41b4>, '/usr/lib/python2.7/pdb.py', 234, 'default', ['                exec code in globals, locals\n'], 0), (<frame object at 0xb74065ec>, '/usr/lib/python2.7/cmd.py', 220, 'onecmd', ['                return self.default(line)\n'], 0), (<frame object at 0xb7413c8c>, '/usr/lib/python2.7/pdb.py', 279, 'onecmd', ['            return cmd.Cmd.onecmd(self, line)\n'], 0), (<frame object at 0xb72d902c>, '/usr/lib/python2.7/cmd.py', 142, 'cmdloop', ['                stop = self.onecmd(line)\n'], 0), (<frame object at 0xb741370c>, '/usr/lib/python2.7/pdb.py', 210, 'interaction', ['        self.cmdloop()\n'], 0), (<frame object at 0xb741344c>, '/usr/lib/python2.7/pdb.py', 158, 'user_line', ['            self.interaction(frame, None)\n'], 0), (<frame object at 0xb7416434>, '/usr/lib/python2.7/bdb.py', 67, 'dispatch_line', ['            self.user_line(frame)\n'], 0), (<frame object at 0xb745889c>, '/usr/lib/python2.7/bdb.py', 49, 'trace_dispatch', ['            return self.dispatch_line(frame)\n'], 0), (<frame object at 0xb74166e4>, 'punk3.py', 3, '<module>', ['from struct import pack\n'], 0), (<frame object at 0xb741217c>, '<string>', 1, '<module>', None, None), (<frame object at 0xb740602c>, '/usr/lib/python2.7/bdb.py', 400, 'run', ['            exec cmd in globals, locals\n'], 0), (<frame object at 0xb74585cc>, '/usr/lib/python2.7/pdb.py', 1233, '_runscript', ['        self.run(statement)\n'], 0), (<frame object at 0xb74582fc>, '/usr/lib/python2.7/pdb.py', 1314, 'main', ['            pdb._runscript(mainpyfile)\n'], 0), (<frame object at 0xb744e75c>, '/usr/bin/pdb', 1338, '<module>', ['    pdb.main()\n'], 0)]

As you can see,when open any python script on pdb or pydevd that libraries loading their own scripts to stack.
So that inspect module has stack() function and can detect stack informations !
Freaking simple also working ! 
"""
    



