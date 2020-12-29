  # Copyright (C) 2020 William Welna (wwelna@occultusterra.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from itertools import permutations
import stackless
import argparse

def magickSquare(n):
    return int(n*((n**2+1)/2))

def theNumbers(n):
    return [x for x in range(1,n*n+1)]

def get_permutations(n):
    ret = []
    s = magickSquare(n)
    for p in permutations(theNumbers(n), n):
    	if sum(p) == s:
    	    ret.append(p)
    return ret

def checksquare(p, s, n):
    d = []
    for x in range(n):
        t = []
        for y in range(n):
            t.append(p[y][x])
        d.append(t)
    t = theNumbers(n)
    for r in d:
        for y in r:
            if y in t:
                t.remove(y)
            else: return False
    for r in d:
        if sum(r) != s:
            return False
    d2 = sum(p[x][x] for x in range(3))
    d1 = sum(p[x][3-x-1] for x in range(3))
    if d1 == s and d2 == s:
        return p
    else: return False

class Worker:

    def __init__(self):
        self.disbatch = stackless.channel()
        self.results = stackless.channel()
        stackless.tasklet(self.work)()

    def work(self):
        ret = []
        while True:
            recv = self.disbatch.receive()
            if recv == None: break
            t = checksquare(recv['p'], recv['s'], recv['n'])
            if t != False:
                ret.append(t)
        self.results.send(ret)
        return
    
    def finish():
        self.disbatch.close()
        self.results.close()

def do_permutations(n, th):
    ret = []
    s = magickSquare(n)
    r = get_permutations(n)
    threads = []
    for i in range(th): threads.append(Worker())
    stackless.run()
    x = 0
    for p in permutations(r, n):
        if x > (th-1): x = 0
        threads[x].disbatch.send({'p':p, 's':s, 'n':n})
        x += 1
    for z in threads: z.disbatch.send(None)
    for z in threads:
        recv = z.results.receive()
        for y in recv:
            ret.append(y)
        z.disbatch.close()
        z.results.close()
    return ret

def main(size, tasklets):
    p = do_permutations(size, tasklets)
    for x in p:
        print("FOUND ->", x)

parser = argparse.ArgumentParser(description='Stackless Magick Squares Example')
parser.add_argument('--size', help='Size of Magic Square', type=int, default=3, required=False)
parser.add_argument('--tasklets', help='Stackless tasklets', type=int, default=32, required=False)
args = parser.parse_args()

main(args.size, args.tasklets)

