import yaml
import actions
import random
import old_modules
domain_file_address='./domain.yml'
mapping_file_address='./data/mapping.yml'


def intent_extractor(data):
    intent=data['intent']['name']
    arr=[str(intent)]
    if len(data['entities'])!=0:
        for i in range(0,len(data['entities'])):
            entity_name=data['entities'][i]['entity']
            entity_value=data['entities'][i]['value']
            arr.append({"name":entity_name,"value":entity_value})           
    return arr

def yml_parse(address):
    with open(address,'r') as file_descriptor:
        domain=yaml.load(file_descriptor, Loader=yaml.FullLoader)    
    return domain



domain=yml_parse(domain_file_address)
actions.slot_data=domain['slots']
map=yml_parse(mapping_file_address)


def get_response(parsed_message):
    try:
        data=intent_extractor(parsed_message)
    except:
        return ' '
    intent=data[0]
    print(intent)
    i=actions.mem_slots[0]
    if(i>=5):
        i=1
       
    actions.mem_slots[i+1]={"intent":intent}
    
    if i<5:
        actions.mem_slots[0]=i+1
    elif i>5:
        actions.mem_slots[0]=1
    if len(data)!=1 :       
        actions.tracker.update_slot(data[1]["name"],data[1]["value"])
    for i in range(1,len(map[intent])+1):
        if(len(map[intent]['case '+str(i)][0])==len(data)):
            if(intent=='data'):
                intent=actions.mem_slots[actions.mem_slots[0]]
            
            action=map[intent]['case '+str(i)][1]
            print(action)
            try:
                
               if(action in domain['actions'] and str(map[intent]['case '+str(i)][0][1]['intent']==intent)):
                   for j in actions.obj_arr:
                      if(action==j.name()):
                         return j.run()
            except:
                print("no entities found")
            list=domain['templates'][action]                   
            return list[int(random.random()*(len(list)-1))]
    return 'reached the end of the function'



    
def get_prefix(parsed_message):
    message=""
    print()
    return message

def get_sufix(parsed_message):
    message=""
    print()
    return message

def respond(message):
    response=get_response(message) 
    if(response!=' '):
        print("Lara >> "+str(response))
        old_modules.speaker(response)
