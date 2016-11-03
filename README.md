# OSecurity

OSecurity is a simple home alarm system, run on a Raspberry Pi terminal and remotely controlled by an Android application.

OSecurity requires:
- Python
- Android Studio
- Raspberry Pi run on Raspbian, with connected hardware
- Packages on Raspbian: LSB 3.0 (or above), Hamachi, GPIO, Xdotool

OSeucurity recommendation:
- Intel Haxm if the Android Studio application emulator is run on an Intel CPU

Startup guide:
- Power up the Raspberry Pi
- On our Raspberry, we have automated Hamachi connection and server.py script startup, this needs to be run manually unless configured
- Make sure your client is also connected to the same Hamachi channel as your server
- Run the application through the Android Studio emulator
- The system is now ready for use

This project is licensed under the GNU GPL 3.0, see license.md for more information
      
