# web_controll_LED
use webpage controll LED

Bascially you should install the pyfirmata for python library, a raspberry pi and arduino.
Initially you should install the LANMP in your raspberry pi.
But now. it just little bit simple and lots of function are not developmented.

It contains three documents:
  the config.txt is for your IP address and your port.
  the listen.py is for your back-end program what is responsible for receving datas.
  the index.php is web pages that sends your data to listen.py
  
Something just like this:
Flow:
    index.php => listen.py => arduino  => LED
      |___raspbery pi___|

Potocal:
    html => tcp => firmata





