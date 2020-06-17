# check_network_and_die
This python script checks internet connection every minute and if disconnected, restarts the machine.
Context: I have a windows PC at a remote location that is accessible through VNC Viewer. It is connected to a secure network and can only connect to that network when a certain classified software is running on it. Recently, due to frequent internet outages in that area, the PC loses connection and that classified software stops running. VNC Viewer also stops functioning, and to start the classified software again there is no other option than to physically access the PC.
I came up with this solution, this script runs in the background and checks internet connection every minute. If disconnected, it waits for some time and restarts. On startup, the classified software starts running automatically. Problem solved.
In case of internet disconnection, a log is also maintained.
