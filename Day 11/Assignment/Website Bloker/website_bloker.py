#Code not working correctly - the permission denied error ...
#  ...[Error 13] persists even after the code is running in elivated version

import os, sys, ctypes
ASADMIN = 'asadmin'

def elevate_code():
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def get_sites():
    with open("block_sites.txt", 'r+') as sites:
        site_list = sites.read().split("\n")

    return site_list

def blockIt(site_list):
    host_file_location = "C:\Windows\System32\drivers\etc\hosts"
    with open(host_file_location, "w+") as host_file:
        lines = ["\n127.0.0.1\t"+line for line in site_list]
        host_file.writelines(lines)

def main():
    elevate_code()
    site_list = get_sites()
    
    blockIt(site_list)


if __name__ == "__main__":
    main()