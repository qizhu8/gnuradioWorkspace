Actually, this is not a diary for today only. Because I kept screwing up on installing gnuradio on mac. So here is what I tried and the assumptions I made. Till now, I still have not successfully installed.

I followed the instruction on gnuradio.org, and I planed to install by compiling the source file, because I have already installed it successfully for many times. 
I download the sourcefile, cd it, and "mkdir build", make(I will talk about the CC=xxx XXXX later). Unfortunately, I could not make it, then I find that, for mac, maybe we should change the compiler. The reason is that, the default compiler for mac is clang instead of gcc, and clang++ instead of g++. Also, the executable library for python is also not the same with that on linux. So in the instruction webpage online, there is a command to change the default compiler. I think it is something like modifying the makefile.

the command is something like:
$ CC=/usr/bin/llvm-gcc CXX=/usr/bin/llvm-g++ cmake -DPYTHON_EXECUTABLE=/opt/local/bin/python2.7 -DPYTHON_INCLUDE_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/Headers -DPYTHON_LIBRARY=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/Python -DSPHINX_EXECUTABLE=/opt/local/bin/rst2html-2.7.py -DGR_PYTHON_DIR=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages ..

The compiling process is always smooth, but for the long time. But when I typed "make test", strange things happed. 194 of 195 tests failed! Honestly, it is not the first time I seen this number, but the last time I seen it is for the reason that I have not linked the library to the compiler. I typed "ldconfig" to make the link(not always necessary). But this time, I was at lost. Because this is not linux, there is no command like 'ldconfig'. So I tried several methods.

1. I wanna check whether the problem lies on the compiler. I installed gcc through macport, I also use the "port select" command to change the default gcc compiler. But failed.
2. I turned to pybombs. Because I happed to see someone post a question on gnuradio-discuss that he failed to do something else, but used the pybombs to install gnuradio on mac osx. 
2.1 I tried to set the default pybombs's compiler to be clang and clang++, failed, the error turns to be "failed to install gcc & failed to install make".
2.2 I tried to use the defaul setting for pybombs, still the same errors as above.
Someone from github said that I should use 
$ ./pybombs -v -v -v install gnuradio 2>&1 | tee fail.txt
to store the running records to file "fail.txt"
I find that, 
	(1) pybombs use "wget" to download dependencies; 
	(2) pybombs use make, cmake
so, I tried to solve "wget" first. I install "homwbrew", and successfully install "wget". But the error still keeps the same "failed to install gcc & gailed to install make". I was lost again.
3. I turned to compiling sourcecode again. I searched for "how to use gcc on mac osx". One result is that, I should installed the "command line tool for xcode". This tool will connect or say convey the gcc to clang or livm-gcc automatically. I tried. Failed again. 
4. I turn to suspect the python. I check all the directory the former long command listed (in line 7. CC=XXXXXXXX ), I modified a little, because I found that some of there are different from what I have. I tried again, failed. Then, I looked into the file called "CMakeCatch.txt" in the /build directory. I found that, there are many "NOT FOUND" there. I think this might be the problem. But I haven't find the way to solve them. 
5. Also, I still not sure about the validity of my pythonpath. The reason is that, the last time I instlaled gnuradio on mac, all is well, but when I followed the tuitorial for OOT module, I could not continue. The error was about the python compiler. 

That is the problem I confonted with, and the idea process. I hope some of my guesses are correct.
