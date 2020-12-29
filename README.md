## MagicSquare-Stackless
Magic Square algorithm using Stackless. I wrote this because I wanted to explore the technical aspects of how stackless worked. 

### Interesting Technical Notes
* Multiple tasklets can't share the same stackless.channel(). Doing so results in possibilities of multiple recieve()s of the same data, resulting in deadlocks and multiple tasks performing the same computations.
* Testing the original and the Stackless based version showed identical performance, with decreasing performance when tasklets numbers are increased.

### License
 
Copyright (C) 2020 William Welna (wwelna@occultusterra.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.