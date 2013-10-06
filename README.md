# Glassface

_"Ok glass, meet this person."_

_Glassface_ is an opt-in utility that lets you add friends on social networks by taking a picture of their face with [Google Glass](https://glass.google.com). 

This hack was developed by @derek-schultz, @daniel-bulger, @alexkau, and @theopak for HackMIT October 2013.


## Building OpenCV From Source

This project uses OpenCV for facial recognition. It is required that you build OpenCV from source. Here's how to do it:

1. Download the [source code](http://opencv.org/downloads.html) to your local development machine.
2. From inside the folder, build the source:

    cd opencv-2.4.6.1 # Change to the downloaded (unzipped) directory
    mkdir build
    cd build
    cmake -D BUILD_PYTHON_SUPPORT=ON  # We're building from source just for this feature
    make
    sudo make install 


## Screen Mirroring Glass on Your Development Machine

This [helpful guide](http://neatocode.tumblr.com/post/49566072064/mirroring-google-glass) describes how to use [asm.jar](asm.jar) to screen mirror.

