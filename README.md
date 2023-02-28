# :musical_note: Vocal/Music separator
### This application takes an mp3 file with music from the user and splits it into vocals and accompaniment, returning a ZIP archive with this content
## Using Spleeter :notes:
This app is using Spleeter, a music separation library, in my project to separate audio tracks into vocals and accompaninment.
You can find MIT Licence of spleeter software at the bottom of this page
![img.png](img.png)

## RUN
```
$ sudo docker build -t vocalapp .
$ sudo docker run -p 5000:5000 vocalapp
```
#### MIT licence
MIT License

Copyright (c) 2019-present, Deezer SA.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.