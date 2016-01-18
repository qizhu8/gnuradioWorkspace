This is the install log written by Yu Wang
In is log, I will try my best to explain the whole process of installing gnuradio from source code.


All these steps can be fetched from gnuradio.org

1. download the binary source code for gnuradio
[Link](https://gnuradio.org/redmine/projects/gnuradio/wiki/BuildGuide)
The link above will provide you with the steps you will go through.
The source code can be found at the link below
http://gnuradio.org/releases/gnuradio/
The latest version at present is 3.7.8.1, that is 
http://gnuradio.org/releases/gnuradio/gnuradio-3.7.8.1.tar.gz

use any method you can come up with to download this file. You can use the brower's download tool, or wget command
e.g.
wget http://gnuradio.org/releases/gnuradio/gnuradio-3.7.8.1.tar.gz
will download the fill to the current workpath.

2. install the dependencies
Generally, you have to install nearly 40 kinds of dependencies. They can be found at 
[link](http://gnuradio.org/doc/doxygen/build_guide.html)
the installation command for ubuntu&debian is "apt-get", for fedora is "yum". Mine is based on debian, so I will use "apt-get"
Don't worry if you failed to install all the dependencies. There is a link called "dependencies test", this link will show you whether your system is able to build the gnuradio.
The dependencies needed are:
# general part
git http://git-scm.com/downloads
cmake (>= 2.6.3) http://www.cmake.org/cmake/resources/software.html
boost (>= 1.35) http://www.boost.org/users/download/
cppunit (>= 1.9.14) http://freedesktop.org/wiki/Software/cppunit/
fftw3f (>= 3.0.1) http://www.fftw.org/download.html
# python part
python (>= 2.5) http://www.python.org/download/
swig (>= 1.3.31) http://www.swig.org/download.html
numpy (>= 1.1.0) http://sourceforge.net/projects/numpy/files/NumPy/
# docs part
doxygen (>= 1.5) http://www.stack.nl/~dimitri/doxygen/download.html
latex* (>= 2.0) http://www.latex-project.org/
# GNU Radio Companion part
Cheetah (>= 2.0) http://www.cheetahtemplate.org/
pygtk (>= 2.10) http://www.pygtk.org/downloads.html
# gr-wavelet part
gsl (>= 1.10) http://gnuwin32.sourceforge.net/packages/gsl.htm
# gr-qtgui part
qt4 (>= 4.4.0) http://qt.nokia.com/downloads/
qwt (>= 5.2.0) http://sourceforge.net/projects/qwt/
pyqt (>= 4.10.0) http://www.riverbankcomputing.co.uk/software/pyqt/download
# gr_wxgui part
wxpython (>= 2.8) http://www.wxpython.org/
python-lxml (>= 1.3.6) http://lxml.de/
# gr-audio part
audio-alsa (>= 0.9) http://www.alsa-project.org
audio-jack (>= 0.8) http://jackaudio.org/
portaudio (>= 19) http://www.portaudio.com/
audio-oss (>= 1.0) http://www.opensound.com/oss.html
audio-osx
audio-windows
# uhd part
uhd (>= 3.0.0) http://code.ettus.com/redmine/ettus/projects/uhd/wiki
# gr-video-sdl: PAL and NTSC display
SDL (>= 1.2.0) http://www.libsdl.org/download-1.2.php
# gr-comedi: Comedi hardware interface
comedilib (>= 0.8.1) http://www.comedi.org/
# gr-log: Logging Tools (Optional)
log4cpp (>= 1.0) http://log4cpp.sourceforge.net/

you can do 
```
apt-get -y install [follow one line below]
git git-core
g++
cmake automake autoconf
libboost-all-dev
libcppunit-dev
pkg-config libfftw3-dev
python-dev 
swig
python-numpy
doxygen
python-cheetah
python-gtk2 
libgsl0-dev
libqt4-dev qt4-dev-tools    
python-qwt5-qt4 libqwt5-qt4-dev libqwtplot3d-qt4-dev
pyqt4-dev-tools
python-wxtools 
python-lxml
python-opengl python-tk python-docutils libfontconfig1-dev libxrender-dev libpulse-dev     libtool  libusb-dev libusb-1.0-0-dev fort77 libsdl1.2-dev ccache libxi-dev  gtk2-engines-pixbuf r-base-dev  liborc-0.4-0 liborc-0.4-dev libasound2-dev   
```
% these are special, I did not installed
python-wxgtk2.8 wx2.8-i18n

or 
```
sudo apt-get -y install git git-core g++ cmake automake autoconf libboost-all-dev libcppunit-dev pkg-config libfftw3-dev python-dev swig python-numpy doxygen python-cheetah python-gtk2 libgsl0-dev libqt4-dev qt4-dev-tools python-qwt5-qt4 libqwt5-qt4-dev libqwtplot3d-qt4-dev pyqt4-dev-tools python-wxtools python-lxml python-opengl python-tk python-docutils libfontconfig1-dev libxrender-dev libpulse-dev libtool  libusb-dev libusb-1.0-0-dev fort77 libsdl1.2-dev ccache libxi-dev  gtk2-engines-pixbuf r-base-dev  liborc-0.4-0 liborc-0.4-dev libasound2-dev
```

The whole process may take roughly an hour.
If you find that your terminal is not working forward, press ctrl+c to abort, and redo the command again. The system will automatically determine whether this dependency has been installed.

At this time, I would like to tell you a joke. When I installed these dependency for the first time(maybe one years ago), I input apt-get -y xxxxxxx, and hit the enter. I turned to my partner, who has installed already. I saied "Maybe I can finish all the installation before going back to dorm". My partner fixed his eyes on his TV show and replied "You are going to sleep here tonight?"

3. decompress the source code
Copy or move the downloaded source code file from ~\Download to the place you want.
For me, I mkdir at ~\gnuradio, and put it there
Then decompress the file
```
tar -zxvf gnuradio-3.7.8.1.tar.gz
```

4 build
```
$ cd gnuradio-3.7.8.1
$ mkdir build
$ cd build
$ cmake ../
```
This step is quit fast. If everything goes well, you will see
"
-- Generating done
-- Build files have been written to: /root/gnuradio/gnuradio-3.7.8.1/build
"
```
$ make && make test
```     
this will take some time. maybe 2 hours (because I went to sleep)
have a nap or have meal.
If you failed to install some dependencies, you will not pass the test part.
"100% tests passed, 0 tests failed out of 194

Total Test time (real) = 125.20 sec
```
$ sudo make install
```
5. update the library
Many people can not wait to run "gnuradio-companion", and they failed by seeing an error called "XXX Linux: LD_XXXXXX". This is for the reason that you have to update your library path, or tell the system where the dependencies you installed is. Use the following command
```
# ldconfig
```
6. you have successfully installed the main part of gnuradio



part 2 build UHD
Also we choose to compile this tool from source code.
http://files.ettus.com/manual/page_build_guide.html

for me:
```
$ mkdir USRP_Hardware_Driver
$ cd USRP_Hardware_Driver
$ git clone git://github.com/EttusResearch/uhd.git
$ cd uhd
$ cd host
$ mkdir build
$ cd build
$ cmake ../
```This is [an example](http://example.com/ "Title") inline link.