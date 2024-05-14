#/usr/bin/python3

#1. Display the OS version – if Windows, display the Windows details; if executed on Linux, display the Linux details.
#2. Display the private IP address, public IP address, and the default gateway.
#3. Display the hard disk size; free and used space.
#4. Display the top five (5) directories and their size.
#5. Display the CPU usage; refresh every 10 seconds.



#1. Display the OS version – if Windows, display the Windows details; if executed on Linux, display the Linux details.


#Importing all necessary modules for this script

import platform
import os
import time
import requests
import socket
import netifaces
import shutil
import psutil
import operator


print('\nWelcome, currently gathering information about your OS...\n')						#Message to user on current process


OSInfo = (platform.uname()) 																#Using the os.platform, this command returns six attributes of your device, system, node, release, version, machine, and processor.


a=(OSInfo[0])																				#Assigning variables to easily print the OSInfo variable and it's index
b=(OSInfo[1])
c=(OSInfo[2])
d=(OSInfo[4])


time.sleep(5)																				#Time delay (5secs) to let user read the previous message instead of showing all output at once



print('This is your operating system:', a)													#Printing out the variables in readable format to user
print('This is the distro of the OS:', b)
print('This is your OS version:', c)
print('Bit processor information:', d)


#2. Display the private IP address, public IP address, and the default gateway.


print('\nGathering information about your IP Address...\n')									#Message to user on current process



time.sleep(5)																				#Time delay (5secs) to let user read the previous message instead of showing all output at once



#Getting the public IP through ipify.org API by calling the function as shown below.


def get_ip_address(): 																		#This is the function get_ip_address
	url = 'https://api.ipify.org' 															#This the domain that will give us our information, Public IP
	response = requests.get(url) 															#Sending a HTTP get request and storing information in variable
	ip_address = response.text 																#response variable information input into text, then store as ip_address variable
	return ip_address 																		#return ip_address variable to the function
	
ip = get_ip_address() 																		#Storing our function in a variable
print("This is your Public IP Address:", ip)												#Printing out the ip variable which contain our function


#Getting the default gateway through the netiface module


gateways = netifaces.gateways()																#Calls out the netifaces gateway function and store it to the variable 'gateways', the functions return all available gateway on our device
default_gateway = gateways['default'][netifaces.AF_INET][0]									#Access gateway information for default network interface and AF_INET(Address Family) then store the first element into the variable

print('This is your Default Gateway IP Address:', default_gateway)							#Prints the variable, default_gateway which contain our default gateway IP


#Getting our internal ip address


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)										#Using socket.socket() function, we place a AF_INET parameter in it to indicate that what we looking for is a IPv4 address. SOCK_DGRAM indicates socket uses UDP
s.connect(("8.8.8.8", 80))																	#This establish a connection to the ip 8.8.8.8, which is Google DNS server, port 80

print('Your Internal IP Address is:', s.getsockname()[0])									#Socket will retrieve IP and port number but will only display IP because of [0], we then print the results


#3. Display the hard disk size; free and used space.

print('\nCalculating disk usage...\n')														#Message to user on current process

																							
time.sleep(5)																				#Time delay for user to have some time to read the message

total, used, free = shutil.disk_usage("/")													#Using shutil module, we can retrieve disk usage from root path folder, return values assign for disk_usage()

print("Total: %d GiB" % (total // (2**30)))													# (2**30) round down the information from btyes to Gigabytes for easy reading
print("Used: %d GiB" % (used // (2**30)))													# total, used, free variables are respectively print out
print("Free: %d GiB" % (free // (2**30)))

#4. Display the top five (5) directories and their size.

print('\nCalculating the top 5 directories and their size...\n')							#Message to user on current process


time.sleep(5)																				#Time delay (5secs) to let user read the previous message instead of showing all output at once

os.chdir("/")																				#Change current directory to root (/)
														
dir_name = os.getcwd()																		#Get the current directory

file_sizes = {}																				#Dictionary stores file name as keys, sizes as values

for filename in os.listdir(dir_name):														#for loop to loop through the (/) directory, os.listdir(dir_name) list all files in the mentioned directory	
    if os.path.isdir(os.path.join(dir_name, filename)):										#os.path.isfile, checks if the given input is a file in this case >> os.path.join >> combines dir_name and filename into a single directory path
        file_sizes[filename] = os.path.getsize(os.path.join(dir_name, filename))			#Store the key and value from filename into file_sizes. Then get the size of the files

sorted_file_sizes = sorted(file_sizes.items(), key=operator.itemgetter(1), reverse=True) 	#sorted function to sort files in size. reverse=True arrange the data in decending order.
																							#opeartor.itemgetter(1) tells the sort function to use 2nd item (index) as the key for sorting, in this case our file size
																							
for i in range(5):																			#repeat 5 times, this will show top 5 files, in this case 5 largest file as we sorted the files in descending order
	
    filename, size = sorted_file_sizes[i]													#Assign filename and size from sort_file_sizes
    
    print(f"{i+1}. {filename} - {size} bytes")												#Uses f-string to format, i+1 to rank the files and output the filename and size
    
    
    
#5. Display the CPU usage; refresh every 10 seconds.

print('\nDisplaying your CPU Usage in percentage % ...\n')									#Message to user on current process

while True:																					#Infinite loop using while function. Always true, unless condition met
    try:
        print('The CPU usage is: ', psutil.cpu_percent(10), 								#Using psutil module. we can extract the CPU usage %, then print is out every 10 secs by adjusting the value in the bracket
        '%, information will refresh infinitely every 10 secs')
        print('Ctrl + C to exit program\n')
        
    except KeyboardInterrupt:																#except if KeyboardInterrupt, it will trigger the condition to exit
        print('\nUser exited through keyboard input')
        break
