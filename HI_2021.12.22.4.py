
# pip install pyinstaller
# pip install pyjokes
# pip install PyDictionary
# pip install platform
# pip install psutil
# pip install requests
# pip install getpass
# pip install pywhatkit
# pip install pysttx3
# pip install speechrecogition
# pip install wikipedia
# pip install Pyaudio
# pip install speedtest-cli
# pip install pyautogui
# pip install py-cpuinfo
# pip install textblob
# pip install nlp
# pip install cz_freeze

#######################################################################################################################################################################


#######################################################################################################################################################################

from genericpath import exists
import pyttsx3
import json
import speech_recognition as sr
import requests
from time import *
import datetime
import getpass
import platform
import random
import psutil
import pyaudio
import wikipedia
import sys
import os
import subprocess
import pyautogui
from PyDictionary import PyDictionary
import cpuinfo
import speedtest
import webbrowser

# ######################################################################################################################################################################


# insilizing listener to take in voice of user from microphone(using python text to speech module)
# selected index voice 0 for male voice and 1 for female voice.
# insilizing  talk method to pass in text in talk method make program speak those words.
# returning none in case of any exception occured.


all_voice = ["MARK","SOFIA"]
# Reading data from hip_data.json file is exists
if os.path.isfile("hip_data.json"):
    with open("hip_data.json",encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        if "voice" in data.keys():
            voice_name = data["voice"]
        else:
            voice_name = 0

        if "user_passcode" in data.keys():
            user_passcode ={}
            for key,value in data["user_passcode"].items():
                user_passcode[key] = value
        else:
            user_passcode = {}

        if "main_passcode" in data.keys():
            main_passcode = data["main_passcode"]
        else:
            main_passcode = "sat"

        if "run_count" in data.keys():
            run_count = data["run_count"]+1
        else:
            run_count = 1

        if "user_phone" in data.keys():
            user_phone = {}
            for key, value in data["user_phone"].items():
                user_phone[key] = value
        else:
            user_phone = {}
            
# Else setting default values of them
else:
    voice_name = 0
    user_passcode = {}
    data = {}
    main_passcode = "sat"
    run_count = 1
    user_phone = {}



############################
############################
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[voice_name].id)
voices = engine.setProperty("rate", 190)
   

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)


    except Exception as e:
        print(e)
        print("Unable to Recognize your voice")
        return "None"

    return command

    

#######################################################################################################################################################################

# checking for internet connection by using request (sending request to connect to google.com
# if  connected passing in true,
# if not connected to internet returning false data.)


url = "https://www.google.com"
connect_status = bool

def check_connection():

    try:
        request = requests.get(url, timeout = 2)
        print("You are connected to the Internet")
        connect_status = True

    except(requests.ConnectionError, requests.Timeout) as exception:
        print("No, Internet Connection")
        connect_status = False

    return connect_status

connect_status = check_connection()
#######################################################################################################################################################################


# predefined and learned data storage
# lists of data in program

pass_change_times = 0

ans_yes = ('yes','y')
ans_no = ('n','no')
nexx_info = ['Nexx', 'I am Nexx', 'I am Nexx Version 2021.12.06', 'I have been created by Satyam Mishra Aka Bedead']

greeting = {'good' : ["Good Morning", "Good night", "Good Afternoon", 'Good evening'],
            'casual_start' : ['Hope you are having a good day', 'Nice to meet you','Hey, how do you do?','How do you do?', 'how are you doing?','Pleased to meet you',
                              'How have you been','How’s it going','Nice to see you',"It’s great to see you","Good to see you",'What’s up?','Heyyy'],
            'casual_end_happy' : ['Good Day','Have a nice day','Have a good day', 'Bye, have a nice day','Thanks for this great talk', 'Hope we will meet again'],
            'startup' : ["Hey","hii","Hello","Welcome back"],
            }


q_about_creator = {'who_made': ('who made you', 'who created you', 'how was you created', 'who is your creator', 'who programmed you', 'can i know your creator'),
                   'born_in' : ("your creator was born in",'satyam was born in','bedead was born in','satyam mishra was born in', 'when was satyam born','when was your creator born'),
                   'current_age' : ('what is satyams current age', 'what is bedeads current age', 'how old is satyam mishra','how old is satyam, what is satyams age'),
                   'current_age_total_months' : ('what is satyams age in months','what is bedeads age in months','how old is satyam in months', 'in months how old is satyam',
                                          'how many` months has satyam lived','how many months did satyam live', 'for how many months bedead has lived'),
                   'current_age_total_days' : ('what is satyams age in days','what is bedeads age in days','how old is satyam in days', 'in days how old is satyam',
                                          'how many days has satyam lived','how many days did satyam live', 'for how many days bedead has lived')}                                   

# for checking users entered answer
receive_query_check = {'greeting' : ('i am fine how are you','i am good how are you','i am great how are you','how do you do', 'i am fine how do you do'),
                       "simp_cal": ["calculate","math mode","calculator mode","calculator","solve"],
                       'what_doing' : ('what are you doing', 'are you doing anything','are you doing anything right now','hat’s going on','hat’s going on in here',
                                       'what is happening right now','what the heck are you doing','what the hell is going on','what are you doing these days'),
                       'help' : ('i need a help', 'i need a small help', 'i need your help', 'i need a small favor from you', 'i have a question','i am having a question',
                                 'can u help me', 'can you help me', 'can you help me please', 'i need some assistance','could you give me a hand','would you mind helping me please',
                                 'can you help me out',"i need help","i need a little help"),
                       'what_can_do' : ["what can you do",'what are things you can do','show me what you have got'],
                       'what_time' : ["what time it is",'what is the time', 'what current time',"what is the time now",'can you tell me current time',
                                      'can you tell whats the time'],
                       'send_what_msg' : ["can you send messege in whatsapp",'drop a messege in whatsapp','deliver a messege in whatsapp',
                                          'can you deliver a messege in whatsapp','send messege'],
                       'voice_mode' : ["turn on voice mode","switch to voice mode","voice mode","voice mode on"],
                       "chat_mode" : ["turn on chat mode","chat mode","chat mode on","turn on text mode","switch to text mode","switch to chat mode","text mode on",],
                       "restart_program" : ["rerun","re run","re run this program","restart","restart this program","restart software",
                                            "re run program","rerun software","rerun program","restart program"],
                       "exit" : ["exit","quit","stop program","exit program","stop software","stop application","exit application",
                                 "exit application","exit nexx","quit nexx","exit nex","quit nex","quit program"],
                       "disk_stats": ["show me disk status","disk stats","show me disk stats","what are disk statistics","disk usage","show me disk usage",
                                      "disk details"],
                       "c_disk": ["c","main disk","1"],
                       "e_disk": ["e","second disk","2"],
                       "f_disk": ["f","third disk","3"],
                       "g_disk": ["g","fourth disk","4"],
                       "memory_stats": ["show me memory status","memory usage","show me memory usage",
                                        "memory distribution","how's memory usage","memory stats","ram usgae",
                                        "show me ram usage","ram stats","ram details"],
                       "core_count": ["show me core count","tell me number of core count","how many core my pc has",
                                      "what is core count in my pc","what is core count in my computer","what is core count in my system",
                                      "how many core this pc has","how many core does this computer has",
                                      "show cpu usage","show cpu stats","cpu stats","cpu usage"],
                       "processor_name": ["what is the name of processor in this pc","what is the name of processor in this computer",
                                         "what is the name of processor in this system","processor in this pc","processor in this computer",
                                         "processor in this system","which processor does this pc has","which processor does this computer has",
                                         "which processor does this system has"],
                        ########
                       "voice_to_mp3": ["convert my voice to mp3 file","change my voice to mp3","voice to mp3",
                                        "can you change my voice to mp3 format","can you change my voice to mp3 file",
                                        "can you convert my voice to mp3 file","can you convert my voice to mp3 format",
                                        "convert my voice to mp3 format"],
                       "internet_speed_test": ["speed readings","show me speed readings","internet speed details","internet speed score",
                                      "internet speed test","perform internet speed test","my internet speed please","my internet speed",
                                      "how's my internet speed","is my internet speed low","is my internet speed high","is my internet high","is my internet slow",
                                                "can you show me my internet speed","how is my internet speed","start speed test",
                                                "start speedtest"],
                       ########
                       "text_to_mp3": ["convert my text to mp3 file","change text file to mp3 file","change text file to mp3 format","convert my text to mp3",
                                       "convert text to mp3 file","change text file to mp3","text to mp3 file","text to mp3"],
                       "change_voice_type": ["change nexx voice", "change the voice of nexx","change nex voice","change the voice of nex",
                                            "change voice type","change you voice"],
                       "sentence_correction": ["check this sentence","correct this sentence","is this sentence right","autocorrect this sentence"],
                       "open_youtube": ["open youtube","open up youtube","show me youtube","open youtube website","goto youtube"]}

# for responding to user
receive_query_check_ans = {'greeting_ans' : (' i am doing great','i am also good','i am fine', 'As allways i am damm good and cool'),
                            "simp_cal_ans": ["That was easy","Here you go","Ammm this is you answer","Is this your answer?","This must be answer",
                                                "You have something more?","That's easy","Amm Here you go","Done"],
                           'what_doing_ans' : ('just chilling in your devcie', 'what can i program do other then processing?', 'I’m just here thinking about you',
                                               'As usual, missing you','I was just about to ask you that.','Waiting for your question, obviously!','I live here!',
                                               'I was just leaving, bye.', 'What do you mean what am I doing here? It’s a free country','I don’t know, I’m lost.',
                                               'I am doing what you said to do','None of your business', 'I’m doing my job. What are you doing?'),
                           'help_ans' : ('Let Me Know How I Can Help',' Is there anything you need','Can I get you anything',
                                         'What can I do to help your process','I am happy to help'),
                           'not_in_data_ans' : ('I dont know about this','Sorry, cant help','I am unable to understand','I need more data to understand',
                                               'I am under development'),
                           'what_time_ans' : ("It's around","It's about","Current time is","It's",""),
                           'send_what_msg_phone_ask_ans' : ("What's that number ",'what is that number ',"Please tell me that number ","Enter the number "),
                           'send_what_msg_ask_ans' : ("What should be that msg ","Enter the msg ","What can be that message ","message please ",
                                                      "What's that msg "),
                           "voice_mode_ans" : ["voice mode turned on","voice mode is on now","voice mode on","turned on one"],
                           "chat_mode_ans" : ["chat mode turned on","text mode on","text mode turned on","chat mode is on"],
                           "how's_internet_speed_fast_ans": ["Your internet speed is good","It seems that your internet is fast",
                                                             "It's good","It's optimum for general use","It's as good as you","It's as fast as you",
                                                             "It's pretty fast"],
                           "how's_internet_speed_slow_ans": ["Your internet speed is low","It's slow","It's a bit slow",
                                                             "It's not fast for general use","It's as slow as you","It's as lazy as you"],
                           "enter_phone": ["Tell me phone number to which you want to send messege","tell me phone number",
                                           "phone number please"],
                           "enter_msg": ["what messege you want to deliver","tell me that messege","what is that messege",
                                         "what should be that messege"],
                           "whats_not_send": ["whatsapp messege was not send","messege can not be send"]}



#######################################################################################################################################################################
# all the functions methods here



# method containing details about satyam mishra,
# such as year of  born, date,month, total months, total days

def creator_details():
    # defining current_data, born_data, name-
    current = datetime.datetime.now()
    born_in = (2003,"December",6) 
    name = []


    # calculating totral months and days lived 
    total_months = ((current.year - born_in[0] - 1)*12) + current.month
    total_days = (365*current.year - born_in[0])- ((12 - current.month)*30)
    
    # calculating my current age in year and month
    age = (current.year - born_in[0] - 1, current.month)
    if current.month == 12 and current.day>=6:
        age = (current.year - born_in[0], current.month - 12)


    # returning all the variables data
    return name,age,born_in,total_months, total_days, current
 
# method for current data
# such as date,month,year,hour,time,day
def get_current_info():
    
    current = datetime.datetime.now()
    year = current.year
    month = current.month
    day = current.day
    hour = current.hour
    minute = current.minute
    second = current.second
    microsecond = current.microsecond

    time = "%s:%s:%s" % (hour,minute,second)

    # returing time variable

    return time

# method for getting meanings and translation and more
def pydictionary(value, word1):

    # instancing pydictionary
    word = PyDictionary()
    
        
    if value =="meaning":
        # getting meaning of thr word
        meaning = word.meaning(word1)

        return  meaning
    elif value=="synonym":
        # getting synnonym of the word
        synonym = word.synonym(word1)

        return synonym
    elif value=="antonym":
        # getting antonym of the word
        antonym = word.antonym(word1)

        return antonym

# method to fretch device details and user details
def device_user_details(value):
    username = getpass.getuser()
    this_system = platform.uname()
    operating_system = this_system.system
    device_node = this_system.node
    device_release = this_system.release
    device_version = this_system.version
    device_machine = this_system.machine
    device_processor = this_system.processor
    processor_brand = cpuinfo.get_cpu_info()["brand_raw"]
    if value == "processor":
        return processor_brand, device_processor

# a method for memory and disk stats
def memory_usage(value, path):

    b = 1024*1024*1024
    if value == "disk":
        data = list(psutil.disk_usage(path))
        n = data[0]
        a = data[1]
        c = data[2]
        space_total = round(n/b, 2)
        space_used = round(a/b, 2)
        space_free = round(c/b, 2)

        return space_total, space_used, space_free
    elif value == "memory":
        data = list(psutil.virtual_memory())
        a = data[0]
        e = data[1]
        c = data[2]
        d = data[3]

        total_memory = round(a/b, 2)
        free_memory = round(e/b, 2)
        percentage_used = c
        used_memory = round(d/b, 2)

        return total_memory,free_memory,percentage_used,used_memory
    elif value == "cpu_core":
        count = int(psutil.cpu_count())
        freq_range = list(psutil.cpu_freq())

        return count, freq_range
    # yet to be coded #
    ###################

# A method for send a reset key for password reset
def sending_whatmsg_instantly(phone_number,msg):

    connect_status = check_connection()
    
    if connect_status == True:
        import pywhatkit as kit
        kit.sendwhatmsg_instantly(f"+91{phone_number}", msg)
        sleep(16)
        pyautogui.press("enter")
        return True
    else:
        print(nexx_info[0]+' - '+"Please, connect to internet")
        return False
    
# method for genrating 5 digit random number
def random_reset_key():
    avail_num = [0,1,2,3,4,5,6,7,8,9]
    reset_key = str()

    for i in range(1, 6):
        reset_key += str(random.choice(avail_num))

    return reset_key


def list_all_software():
    data_ = subprocess.check_output(["wmic", "product", "get", "name"])
    string_ = str(data_)

    try:
        for i in range(len(string_)):
            print(string_.split("\\r\\r\\n")[6:][i]) 
    except IndexError as e:
        print("Done")

def speedtest_start():
    st = speedtest.Speedtest()
    download_speed_bytes = float(st.download())
    upload_speed_bytes = float(st.upload())
    download_speed_mb = download_speed_bytes/(1048576)
    upload_speed_mb = upload_speed_bytes/(1048576)

    return download_speed_mb, upload_speed_mb

def basic_calculation(equation):
    ans = eval(equation)

    return ans

#######################################################################################################################################################################
######################################################################## Access for admin(Security) ###################################################################


def security_check_for_admin(main_passcode, pass_change_times, opertor_name):

        
    pass_code = str(input(nexx_info[0]+' - '+"Can you please enter the passcode : "))

    if (pass_code == main_passcode) or (pass_code == user_passcode[opertor_name]):

        print(nexx_info[0]+' - ', random.choice(greeting.get('casual_start')))
        
        while True:

            n = input(opertor_name + " - ").lower()
                   
            if n in q_about_creator.get('who_made'):
                print(nexx_info[0]+' - ',nexx_info[3])

            elif n in q_about_creator.get('born_in'):
                print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
                    
            elif n in q_about_creator.get('current_age'):
                print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
                    
            elif n in receive_query_check.get("what_doing"):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
                    
            elif n in receive_query_check.get('greeting'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
                    
            elif n in receive_query_check.get('help'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('help_ans')))
    
            elif n in receive_query_check.get('send_what_msg'):
                #phone = input(nexx_info[0]+' - '+"Enter a number : ")
                phone = "9550739128"
                if len(phone) == 10:
                    messege = input(nexx_info[0]+' - '+"Enter a messege : ")
                    
                    send = sending_whatmsg_instantly(phone_number=phone,msg=messege)
                    if send == True:
                        print(nexx_info[0]+' - ',"The messege has been delivered.")
                    else:
                        print(nexx_info[0]+' - ',"I could'nt deliver this messege.")

                else:
                    print(nexx_info[0]+' - ',"The number you entered is greater or less then 10.")

                ################### update code ###############

            elif n in receive_query_check.get("voice_mode"):
                voice_mode_admin(main_passcode, pass_change_times, opertor_name)
                break

            elif n in receive_query_check.get("exit"):
                lis = [3,2,1]
                for i in lis:
                    print(i,end = " ",flush=True);sleep(.3)
                print("Bye")
                exit()
                
            elif n in receive_query_check.get("restart_program"):
                admin_opertor_mode(user_passcode,pass_change_times, data)
                    
            elif n in receive_query_check.get("disk_stats"):
                path = ""
                disk_name = input(nexx_info[0]+' - ' + "which disk data : ")
                if disk_name in receive_query_check.get("c_disk"):
                    path = "C:/"
                elif disk_name in receive_query_check.get("e_disk"):
                    path = "E:/"
                elif disk_name in receive_query_check.get("f_disk"):
                    path = "F:/"
                elif disk_name in receive_query_check.get("g_disk"):
                    path = "G:/"
                elif disk_name == "all":
                    path = "/"

                value = "disk"
                space_total,space_used,space_free = memory_usage(value, path)
                print(nexx_info[0]," - \nTotal Size: ",space_used,"\nUsed disk : ",space_used,"\nFree disk : ",space_free)
            ########################### upto here in voice mode ############################

            elif n in receive_query_check.get("memory_stats"):
                value = "memory"
                total_memory,free_memory,percentage_used,used_memory = memory_usage(value, "")
                print(nexx_info[0]," - \nTotal Ram : ",total_memory,"\nUsed Ram : ",used_memory,"\nUsed Percentage : ",percentage_used,"\nFree Ram : ",free_memory)

            elif "open" in n and (n not in receive_query_check.get("open_youtube")):
                n = list(n.split(" "))
                print(n)
                if len(n) == 2:
                    software_name = str(n[1]).capitalize()
                    os.system(software_name)
                elif len(n) == 3:
                    n1 = str(n[1]).capitalize() + str(n[2]).capitalize()
                    print(n1)
                    os.system(n1)
                else:
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))

            elif n in receive_query_check.get('what_time'):
                time = get_current_info()
                print(nexx_info[0]+' - ' +random.choice(receive_query_check_ans.get("what_time_ans")) + time)

            elif "antonym" in n:
                check_connection()
                value = "antonym"
                lis = list(n.split(" "))
                word1 = str(lis[-1])
                ans = pydictionary(value, word1)
                print(ans)

            elif "synonym" in n:
                check_connection()
                value = "synonym"
                lis = list(n.split(" "))
                word1 = str(lis[-1])
                ans = pydictionary(value, word1)
                print(ans)

            elif n in receive_query_check.get("text_to_mp3"):
                v = str(input(nexx_info[0]+' - Enter the text which you want to convert to mp3 : '))
                file_name = str(input(nexx_info[0]+' - What should be name of saved file : '))
                if ".mp3" in file_name:
                    pass
                else:
                    file_name = file_name+".mp3"

                anim = " Saving.."
                anim1 = file_name

                for i in anim:
                    print(i,end=" ",flush=True);sleep(.1)

                engine.save_to_file(v, file_name)
                engine.runAndWait()

                for a in anim1:
                    print(a,end=" ",flush=True);sleep(.1)
                print("Saved")
                print(file_name)

            elif n in receive_query_check.get("core_count"):
                value = "cpu_core"
                count_cpu, freq_range = memory_usage(value,"")
                print(nexx_info[0]," - \nCPU Count : ",count_cpu,"\nFREQ-Range : ",freq_range)

            elif n in receive_query_check.get("processor_name"):
                value = "processor"
                processor_brand, device_processor = device_user_details(value)
                print(nexx_info[0]," - \Processor brand : ",processor_brand,"\Processor Model : ",device_processor)

            elif "meaning" in n:
                check_connection()
                value = "meaning"
                lis = list(n.split(" "))
                word1 = str(lis[-1])
                if connect_status==True:
                    ans = pydictionary(value, word1)
                    
                    print(ans)
                elif connect_status==False:
                    print(nexx_info[0]+' - ',"Please, connect to Internet for this feature to")
            
            elif n in receive_query_check.get("internet_speed_test"):
                download_speed_mb, upload_speed_mb = speedtest_start()
                print(nexx_info[0]+' - ',"\nDownload Speed : ",download_speed_mb,"\nUpload Speed : ",upload_speed_mb)

            elif n in receive_query_check.get("simp_cal"):
                while True:

                    n = input(nexx_info[0]+' - '+"Equation : ").lower()
                    if n in receive_query_check.get("exit"):
                        break
                
                    else:
                        equation = n
                        ans = basic_calculation(equation)
                        print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get("simp_cal_ans")))
                        print(nexx_info[0]+' - ',ans)
            
            elif ("search" in n) or ("google" in n) or("tell me" in n):
                if ("for" in n) or ("about" in n) or ("in google about" in n):
                    n = list(n.split())
                    if "about" in n:
                        ind = int(n.index("about"))
                    elif "for" in n:
                        ind = int(n.index("for"))
                    topic = n[(ind+1):]
                    new_topic = " ".join([str(a) for a in topic])

                    check_connection()
                    if connect_status == True:
                        print(wikipedia.summary(new_topic))
                    else:
                        print(nexx_info[0]+' - ',"Connect to Internet and try again")

            elif n in receive_query_check.get("sentence_correction"):
                pass

            elif n in receive_query_check.get("open_youtube"):
                webbrowser.open_new_tab("https://www.youtube.com")
                print(nexx_info[0]+' - ',"Youtube has been opened in one of your browsers.")

            

            else:
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))

    else:
        pass
        

    ############## update this #################

###################################################################################################################################################
###################################################################################################################################################

def voice_mode_admin(main_passcode, pass_change_times, opertor_name):

    global v

    talk(random.choice(receive_query_check_ans.get("voice_mode_ans")))
    talk("Voice mode is under development it's suggested to use text mode")

    while True:
        print("listening....")
        n = take_command().lower()

        if n in receive_query_check.get("chat_mode"):
            print(random.choice(receive_query_check_ans.get("chat_mode_ans")))
            security_check_for_admin(main_passcode, pass_change_times, opertor_name)
            break
        
        elif n in receive_query_check.get("change_voice_type"):
            print(nexx_info[0]+' - ',"All Voices available : ",all_voice)
            v = str(input(nexx_info[0]+' - '+ "Enter any name from above list : "))
            talk("For voice to be changed you need to restart this program")
            print(nexx_info[0]+' - ',"For voice to be changed you need to restart this program")
            print(nexx_info[0]+' - ',"I am restarting this program in 5 second")
            print(nexx_info[0]+' - ',"After restarting turn on voice mode to see changes")
            talk("After restarting turn on voice mode to see changes")
            
            #############################
            #############################
            if v.lower == "sofia":
                data["voice"] = 1
            else:
                data["voice"] = 0
            with open("hip_data.json","w",encoding="utf-8") as file:
                json.dump(data, file)

            anim = 3

            for i in range(1,anim+1):
                print(i,end="\n",flush=True);sleep(.1);talk(i)
            exit()
        
        elif n in q_about_creator.get('who_made'):
            talk(nexx_info[3])

        elif n in q_about_creator.get('born_in'):
            talk("he was born in"+born_in[0]+born_in[2]+born_in[1])
                    
        elif n in q_about_creator.get('current_age'):
            talk(random.choice(name)+"is currently"+age[0]+'years'+age[1]+'months old')
                    
        elif n in receive_query_check.get("what_doing"):
            talk(random.choice(receive_query_check_ans.get('what_doing_ans')))
                    
        elif n in receive_query_check.get('greeting'):
            talk(random.choice(receive_query_check_ans.get('greeting_ans')))
        
        elif n in receive_query_check.get('help'):
            talk(random.choice(receive_query_check_ans.get('help_ans')))
    
        elif n in receive_query_check.get('send_what_msg'):
            talk(random.choice(receive_query_check_ans.get("enter_phone")))
            phone = take_command().lower()
            if len(phone) == 10:
                talk(random.choice(receive_query_check_ans.get("enter_msg")))
                messege = take_command().lower()
                send = sending_whatmsg_instantly(phone_number=phone,msg=messege)
                if send == True:
                    talk(random.choice(receive_query_check_ans.get("whats_not_send")))
                    ##########################################
                    ##########################################
                    ##########################################
                    ##########################################


        elif n in receive_query_check.get("exit"):
            lis =[3,2,1]
            for i in lis:
                print(i,end="",flush=True);sleep(.2);talk(i)
            exit()

        elif n in receive_query_check.get("restart_program"):
            talk("Restarting program")
            admin_opertor_mode(user_passcode,pass_change_times,data)

        elif n in receive_query_check.get("disk_stats"):
            path = ""
            talk("About which disk storage you want to know")
            disk_name = take_command().lower()
            if disk_name in receive_query_check.get("c_disk"):
                path = "C:/"
            elif disk_name in receive_query_check.get("e_disk"):
                path = "E:/"
            elif disk_name in receive_query_check.get("f_disk"):
                path = "F:/"
            elif disk_name in receive_query_check.get("g_disk"):
                path = "G:/"
            elif disk_name == "all":
                path = "/"
            else:
                path = "/"

            value = "disk"
            space_total,space_used,space_free = memory_usage(value, path)
            print(nexx_info[0]," - \nTotal Size: ",space_used,"\nUsed disk : ",space_used,"\nFree disk : ",space_free)

        else:
            talk(random.choice(receive_query_check_ans.get("not_in_data_ans")))

    ####################
    ######## under progress ########

#######################################################################################################################################################################
####################################################################### Opertor check and mode select ####################################################################

# code to start a simple converstiion
def admin_opertor_mode(user_passcode,pass_change_times,data):
    data["run_count"] = run_count
    with open("hip_data.json","w",encoding="utf-8") as file:
        json.dump(data, file)
    
    if run_count == 1:
        print(nexx_info[0]+' - ',"hey, I am Nexx.\nAn multi-purpose program.\nCurrently, I am version 2021.12.22 or in simple words 4th version.")


    print(nexx_info[0]+' - ',random.choice(greeting.get('startup'))+",", nexx_info[1], flush=True);sleep(0.2)
    opertor_name = str(input(nexx_info[0]+" - Can I know your name : "))
    
    if opertor_name in name:
        print(nexx_info[0]+' - ',random.choice(greeting.get('startup')), random.choice(name))
        if current.hour >0 and current.hour <= 12:
            print(nexx_info[0]+' - ',greeting.get('good')[0])
        elif current.hour > 12 and current.hour <= 16:
            print(nexx_info[0]+' - ',greeting.get('good')[2])
        elif current.hour > 16 and current.hour <= 19:
            print(nexx_info[0]+' - ',greeting.get('good')[3])
        elif current.hour > 19 and current.hour <=24:
            print(nexx_info[0]+' - ',greeting.get('good')[1])



        security_check_for_admin(main_passcode, pass_change_times,opertor_name)
    elif opertor_name in user_passcode.keys():
        print(nexx_info[0]+' - ',random.choice(greeting.get('startup')), opertor_name)
        if current.hour >0 and current.hour <= 12:
            print(nexx_info[0]+' - ',greeting.get('good')[0])
        elif current.hour > 12 and current.hour <= 16:
            print(nexx_info[0]+' - ',greeting.get('good')[2])
        elif current.hour > 16 and current.hour <= 19:
            print(nexx_info[0]+' - ',greeting.get('good')[3])
        elif current.hour > 19 and current.hour <=24:
            print(nexx_info[0]+' - ',greeting.get('good')[1])

        

        security_check_for_admin(main_passcode, pass_change_times,opertor_name)
        
            
    else:
        print(nexx_info[0]+' - ', "Ohh. you seems new")
        new_user = str(input(nexx_info[0]+' - '+"Enter your username for this program\n(This is one time) : "))
        new_user_pass = str(input(nexx_info[0]+' - '+"Enter your password for this program\n(This is one time) : "))
        new_user_phone = input(nexx_info[0]+' - '+"Enter your phone number which is connected to whatsapp : ")
        
        user_passcode[new_user] = new_user_pass
        user_phone[new_user] = new_user_phone
        if os.path.isfile("hip_data.json"):
            with open("hip_data.json","w",encoding="utf-8") as file:
                data["user_passcode"] = user_passcode
                data["user_phone"] = user_phone
                json.dump(data, file)
        else:
            data = {}
            n = {new_user:new_user_pass}
            n1 = {new_user:new_user_phone}
            data["user_passcode"] = n
            data["user_phone"] = n1

            with open("hip_data.json","w",encoding="utf-8") as file:
                json.dump(data, file,indent=3)

        anim = "Adding...."

        for i in anim:
            print(i,flush = True,end = " ");sleep(.2)

        admin_opertor_mode(user_passcode,pass_change_times,data)
            
name,age,born_in,total_month,total_days,current = creator_details()

#######################################################################################################################################################################

def main_run():
    admin_opertor_mode(user_passcode,pass_change_times,data)

main_run()

#######################################################################################################################################################################
