# Custom GnuRadio Blocks

This repo is intended to host some GnuRadio blocks that I have been developing as part of my research. They are various utilitary blocks that you may find useful.
All blocks are foundable under the "Custom category"

# List of provided blocks
## Gain Sweeper
This block applies subsequently each gain of the provided gain list to the input signal, changing the gain value every "Segment length" samples

## Test Interp
Simple test of an interpolation block that you can use as an example

#Installation
```
mkdir build
cd build
cmake ../
make
make install (you may need sudo for this one)
ldconfig
```

