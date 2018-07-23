# BBC micro:bit data logger
The process involves 2 parts, the script which runs on the micro:bit and the Python script running on the logging computer which reads the serial data from the micro:bit over USB.    

## Micro:bit script Blocks
The script that runs on the BBC micro:bit was written using JavaScript on https://makecode.microbit.org/. Copy the JavaScript code into the editor then click the button to switch to blocks. If you want to log something different other than the temperature and light values, simply change the input block in the ```serial write line``` block. ```Join``` is used to write multiple values on one line. If you use this you need to add a space character between each value so the logging script will read it correctly.

## Micro:bit script Python
This code writes the temperature to the serial port. Unfortunately, micro:python can't currently be used to read the light level. 
    
## Python logging script   
The simple Python 3 micro:bit logging script runs on the logging computer which has the micro:bit plugged into it via USB.   
It sits reading and interpreting each line, converting it across at the end to the ```microbit_data.csv``` file.   
To force the Python script to output the .csv file, simply close/stop the program, or disconnect the micro:bit.  
