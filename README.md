# BBC micro:bit data logger
The process involves 2 parts, the program which runs on the micro:bit and the Python program running on the logging computer which reads the serial data from the micro:bit sent over USB.    

## Micro:bit script Blocks
The program that runs on the BBC micro:bit was written using JavaScript on https://makecode.microbit.org/. Copy the JavaScript code into the editor then click the button to switch to blocks. If you want to log something different other than the temperature and light values, simply change the input block in the ```serial write line``` block. ```Join``` is used to write multiple values on one line. If you use this you need to add a space character between each value so the logging script reads it correctly. 

Note: This program is written in JavaScript as currently MicroPython can’t read the light levels. 
    
## Python logging script   
The Python 3 micro:bit logging program runs on the logging computer which has the micro:bit plugged into it via USB.   
It reads and interprets each line, converting it across at the end to the ```microbit_data.csv``` file.   
To force the Python script to output the .csv file, simply close/stop the program, or disconnect the micro:bit.  

Note: run this program in Linux as you need to install an extra driver to get it to work on Windows.
