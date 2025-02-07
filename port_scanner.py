import socket                 # this is for network connections
import sys                    # this is to access command-line arguments
from datetime import datetime # to measure scan duration

#To target the host
if len(sys.argv) == 2:
    # Convert the hostname to an IP address
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Usage: python3 port_scanner <hostname>')
    sys.exit(1)    


#Scanning and Banner UI
print('=' * 50)
print('Scanning Target: ' + target)
print('Scanning started at: ' + str(datetime.now()))
print('=' * 50)

# Scanning a Range of Ports
def scan_port(port):
    #Creating a new socket for each port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # timeout for the connection
    s.settimeout(1)
    try:
        # Attempting to connect to the target
        result = s.connect_ex((target, port))
        # If result is 0, the port is open
        if result == 0:
            print ('Port{}: Open'.format(port))
    except KeyboardInterrupt:
        print('\nScan interrupted by user')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server") 
        sys.exit()
    finally:
        s.close()

# Loop through the ports

# Timing for calculation of the total of scan duration
start_time = datetime.now()

# Scanning ports 1 to 1023 (this can be adjusted as needed)
for port in range(1, 600):
    scan_port(port)

# Calculating and displaying total scan time
end_time = datetime.now()
total_time = end_time - start_time
print('=' * 50)
print('Scanning completed in: {}'.format(total_time))

