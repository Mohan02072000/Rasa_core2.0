import urllib
slot_data={}
mem_slots=[0,{},{},{},{},{}]
class tracker:
    def get_slot(name):
        try:
             return slot_data[name]['type']
        except Exception as e:
             print("slot not found")
             print("Slots available: "+slot_data)
             return ''
    def update_slot(name, data):
        try:            
            slot_data[name]['type']=data
        except Exception as e:
            print("Update Unseccessful")

def connection_check():
    try:
        st="https://www.google.co.in"
        data=urllib.request.urlopen(st)
        return True
    except Exception as e:
        return False


class Weather:
    def name(self):
        return 'action_weather'

    def run(self):
        if(connection_check()==False):
            return "Error: System offline. Need Internet connection  for this service."
        
        loc=tracker.get_slot('location')
        string=loc

        return (string)

        


class wikipedia:
    def name(self):
        return 'action_wikipedia'


    def run(self):
        if(connection_check()==False):
            return "Error: System offline."
        result=''
        key=tracker.get_slot('keywords')
        result=key
        return (result)
        


class youtube:
    def name(self):
        return 'action_youtube'


    def run(self):
        if(connection_check()==False):
            return "Error: System offline."
        result=''
        key=tracker.get_slot('keywords')
        try:
            
            result=key
            return "That was, "+result
        except:
            print(Exception)
            return "Youtube launch failure: "+key



class browser:
    def name(self):
        return 'action_browser'

    def run(self):
        if(connection_check()==False):
            return "Error: System offline."
        result=''
        key=tracker.get_slot('keywords')
        
        return 'Initiating google search. Keywords input: '+key
        



class software:
    def name(self):
        return 'action_software'

    def run(self):
        result=''
        key=tracker.get_slot('keywords')
        result=key
        return result
        



class video:
    def name(self):
        return 'action_video'

    def run(self):
        
        key=tracker.get_slot('keywords')
        result="Now playing:  "+key
        return result
        


class music:
    def name(self):
        return 'action_music'

    def run(self):
        key=tracker.get_slot('keywords')
        
        result='now playing: '+key
        return result
        



class dateandtime:
    def name(self):
        return 'action_inform'

    def run(self):
        result=""
        key=tracker.get_slot('info')
        print(key)
        e=datetime.datetime.now()
        if(key=='date'):
            return "Todays date is "+str(e.day)+": "+str(e.month)+": "+str(e.year)
        elif(key=='time'):
            if(e.hour<=12):
                return "It is "+str(e.hour)+": "+str(e.minute)+" AM and "+str(e.second)+" seconds right now"
            elif(e.hour>12):
                return "It is "+str(e.hour-12)+": "+str(e.minute)+" PM and "+str(e.second)+" seconds right now"
            
        return "Sorry. Cant tell you that."
         
        
class traceback:
    def name(self):
        return 'action_traceback'

    def run(self):
        i=mem_slots[0]

        print("traceback section")

class repeat:
    def name(self):
        return 'action_repeat'
    def run(self):
        try:
            keywords=tracker.get_slot('keywords')
            return keywords
        except:
            return 'Repeat function failed'


obj_arr=[Weather(),wikipedia(),youtube(),browser(),software(),video(),music(),dateandtime(),repeat()]
