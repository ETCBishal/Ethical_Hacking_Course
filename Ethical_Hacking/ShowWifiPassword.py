import subprocess,platform,time,sys
from colorama import Fore,init

init(autoreset=True)  # autoreset = True => avoiding color to the text in the next line

def show_my_wifi_password():

    wifi = input('Enter the wifi name: ').strip()
    
    os_name = platform.system()  # fetching the os name
    if os_name == 'Windows':
        cmd = 'netsh wlan show profile'
        output = subprocess.check_output(cmd,shell=True,text=True)
        wifi_list = []
        
        for line in output.splitlines():
            if 'All User Profile' in line:
                wifi_name = line.split(':')[1].strip()
                wifi_list.append(wifi_name)
            

        if wifi in wifi_list:
            print('Fetching the password!')
            time.sleep(2)
            
            cmd_fetch_password = f'netsh wlan show profile {wifi} key=clear'

            fetch_password = subprocess.check_output(cmd_fetch_password,shell=True,text=True)

            for line in fetch_password.splitlines():
                if 'Key Content' in line:
                    password_ = line.split(':')[1].strip()
                    return f'\n Your wifi password is:{Fore.GREEN} {password_}'     
        else:
            print(f'{Fore.RED}[-] You are not connected to "{wifi}".\n')
            sys.exit()

    elif os_name == 'Linux':
        
        
        
        # TODO:

        
        
        
        pass

password = show_my_wifi_password()
print(password)