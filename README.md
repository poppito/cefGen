# cefGen
Python script to generate TCP loads through a text file of CEF events.

To obtain the script run:
git clone https://github.com/poppito/cefGen.git


What it does do:
- reads from a text file and send line by line, events of any format (this should be present in the text file) to a TCP socket.
- let's the user specify the TCP port number.
- requires the text file to be present in the same directory as the script.
- can specify a different target IP to the localhost (however localhost is default if none specified).


What it doesn't do:
- can't tweak EPS (at this stage).
- can't read from a text file outside the directory of the script.


usage:
python cefGen.py

Example: 

python cefGen.py 
path is /home/cefuser/cefGen
Today we'll be generating a 0.33 EPS load of CEF events to a TCP socket on this host!
What port would you like to send this load to? Remember this value can only be between 0-65535, preferably higher than 1024! 513
What is the filename? Remember, the file should be in the same directory as this script! outfile1.cef
about to print event
<Prints event> 
Sending event through to TCP port 513
<Sends event>


