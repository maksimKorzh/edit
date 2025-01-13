#!/bin/python3
i=' if ';e=' elif z==';exec(f"""import curses as u,sys;s=u.initscr()
s.nodelay(1);u.noecho();u.raw();s.keypad(1);b=[];n='o.txt';x,y,r,c=[0]*4
if len(sys.argv)==2:n=sys.argv[1]\ntry:\n with open(sys.argv[1]) as f:
  w=f.read().split('\\n')[:-1]\n  for Y in w:\n   b.append([ord(c) for c in Y])
  r=len(b)-1;c=len(b[r])\nexcept:b.append([])\nwhile True:\n R,C=s.getmaxyx()
 s.move(0,0)\n{i}r<y:y=r\n{i}r>=y+R:y=r-R+1\n{i}c<x:x=c\n{i}c>=x+C:x=c-C+1
 for Y in range(R):\n  for X in range(C):\n   try:s.addch(Y,X,b[Y+y][X+x])
   except:pass\n  s.clrtoeol()\n  try:s.addch('\\n')\n  except:pass
 u.curs_set(0);s.move(r-y,c-x);u.curs_set(1);s.refresh();z=-1\n while z==-1:\
z=s.getch()\n if z!=z&31 and z<128:b[r].insert(c,z);c+=1\n{e}10:l=b[r][c:];b[
r]=b[r][:c];r+=1;c=0;b.insert(r,[]+l)\n{e}263 and c==0 and r:l=b[r][c:];del b[
r];r-=1;c=len(b[r]);b[r]+=l\n{e}263 and c:c-=1;del b[r][c]\n{e}260 and c!=0:\
c-=1\n{e}261 and c<len(b[r]):c+=1\n{e}259 and r!=0:r-=1;c=0\n{e}258 and r<len(
b)-1:r+=1;c=0\n{i}z==17:break\n{e}19:\n  w=''\n  for l in b:w+=''.join([chr(c)\
 for c in l])+'\\n'\n  with open(n,'w') as f:f.write(w)\nu.endwin()""")
