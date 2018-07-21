# BBC micro:bit data logger
The process involves 2 parts, the script which runs on the micro:bit and the Python script running on the logging computer which reads the serial data from the micro:bit over USB.    

## Micro:bit script Blocks
The script that runs on the BBC micro:bit was written using JavaScript on https://makecode.microbit.org/. Copy the JavaScript code into the editor then click the button to switch to blocks. If you want to log something different other than the accelerometer values, simply change the input block in the ```send value``` block.

## Micro:bit script Python
TODO
    
## Python logging script   
The simple Python (3) micro:bit logging script runs on the logging computer which has the receiver micro:bit plugged into it via USB.   
It sits reading and interpreting each line, converting it across at the end to the ```microbit_data.csv``` file.   
To force the Python script to output the .csv file, simply close/stop the program, or disconnect the micro:bit.  

To use this part, you need to make sure your operating system has the required USB serial driver. 

#### Windows
You need to make sure you have the [mbed USB serial driver](https://developer.mbed.org/handbook/Windows-serial-configuration) installed.   

#### Mac/Linux   
All you need is already built in to Mac OS / Linux. There is no need to install any additional drivers.
