#!/bin/python3
import curses, time, sys
def main(stdscr):
  s = curses.initscr(); s.nodelay(1); curses.noecho(); curses.raw(); s.keypad(1)
  curses.use_default_colors()
  b = []; src = 'noname.txt'; x, y, r, c = [0] * 4
  if len(sys.argv) == 2: src = sys.argv[1]
  try:
    with open(sys.argv[1]) as f:
      cont = f.read().split('\n'); cont = cont[:-1] if len(cont) > 1 else cont
      for rw in cont: b.append([ord(c) for c in rw]); r = len(b)-1; c = len(b[r])
  except: b.append([])
  if len(sys.argv) == 1: b.append([])
  while True:
    R,C = s.getmaxyx()
    s.move(0, 0)
    if r < y: y = r
    if r >= y + R: y = r - R+1
    if c < x: x = c
    if c >= x + C: x = c - C+1
    for rw in range(R):
      brw = rw + y
      for cl in range(C):
        bcl = cl + x
        try: s.addch(rw, cl, b[brw][bcl])
        except: pass
      s.clrtoeol()
      try: s.addch('\n')
      except: pass
    curses.curs_set(0); s.move(r-y, c-x); curses.curs_set(1); s.refresh(); ch = -1
    while (ch == -1): ch = s.getch()
    if ch != ((ch) & 0x1f) and ch < 128: b[r].insert(c, ch); c += 1
    elif ch == ord('\n'): l = b[r][c:]; b[r] = b[r][:c]; r += 1; c = 0; b.insert(r, [] + l)
    elif ch == curses.KEY_BACKSPACE and c: c -= 1; del b[r][c]
    elif ch == curses.KEY_BACKSPACE and c == 0 and r: l = b[r][c:]; del b[r]; r -= 1; c = len(b[r]); b[r] += l
    elif ch == curses.KEY_LEFT and c != 0: c -= 1
    elif ch == curses.KEY_RIGHT and c < len(b[r]): c += 1
    elif ch == curses.KEY_UP and r != 0: r -= 1
    elif ch == curses.KEY_DOWN and r < len(b)-1: r += 1
    elif ch == curses.KEY_END: c = len(b[r])
    elif ch == curses.KEY_HOME: c = 0
    elif ch == curses.KEY_PPAGE: r = r-5 if r-5 > 0 else 0
    elif ch == curses.KEY_NPAGE: r = r+5 if r+5 < len(b)-1 else len(b)-1
    elif ch == curses.KEY_DC and len(b): del b[r]; r = r if r < len(b) else r-1 if r-1 >= 0 else 0
    if not len(b): b = [[]]
    rw = b[r] if r < len(b) else None; rwlen = len(rw) if rw is not None else 0
    if c > rwlen: c = rwlen 
    if ch == (ord('q') & 0x1f): sys.exit()
    elif ch == (ord('s') & 0x1f):
      cont = ''
      for l in b: cont += ''.join([chr(c) for c in l]) + '\n'
      with open(src, 'w') as f: f.write(cont); s.clear(); s.refresh(); time.sleep(0.1)
curses.wrapper(main)
