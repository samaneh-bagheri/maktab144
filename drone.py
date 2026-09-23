from abc import ABC, abstractmethod

# status_list =[  AVAILABLE , CHARGING ,MAINTENANCE ,IN_MISSION ]
# area_type_list= [SMALL ,MEDIUM ,LARGE ]
# # medical_shipment = [blood,medicine,emergency_kit]
# # sensitivity_level = [NORMAL,SENSITIVE,CRITICAL]
  
class Drone(ABC):
    def __init__(self,id,name,battery_level,current_status=None,complete_missions_count =0):
        self.id = id
        self.name = name
        self.battery_level = battery_level
        self.current_status = current_status
        self.complete_missions_count = complete_missions_count
    def check_battery(self,required_battery):
        if self.battery_level >= required_battery:
            return True
        self.current_status = "CHARGHING"
        return False
    def change_status(self,new_status):
        self.current_status = new_status

    def New_mission(self):
        if self.current_status == "AVAILABLE":
            print ("mission recived")

class EquipmentDrone(Drone):
    def __init__(self,id,name,battery_level,current_status=None,complete_missions_count=0,capacity,aid_package):
        super().__init__(id,name,battery_level,current_status=None,complete_missions_count=0)
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self.capacity = capacity
        self.aid_package = Aid_package() #composition
    def success_mission(self,weight,capacity,battery_level):
        complete_missions_count =0
        if  self.aid_package.weight <= self.EquipmentDrone.capacity and self.battery_level == 20:
            self.complete_missions_count +=1
        else:
            raise ValueError("mission not completed")
            
class Aid_package:
    def __init__(self,title,weight,category):
        self.title =title
        self.weight = weight
        self.category = category

class SearchDrone(Drone):
    def __init__(self,id,name,battery_level,current_status=None,complete_missions_count = 0,area_type):
        super().__init__(self,id,name,battery_level,current_status=None,complete_missions_count=0)
        self.area_type = area_type
        self.result=0
    def search(self):
        if self.area_type == "SMALL":
            if self.battery_level >= 10:
                print ("search completed , Area:SMALL ,Result :",self.result,"people found.")
            else:
                print("battery is not enough")
        if self.area_type == "MEDIUM":
            if self.battery_level >= 20:
                print ("search completed , Area:MEDIUM ,Result :",self.result,"people found.")
            else:
                print("battery is not enough")

        if self.status == "LARGE":
            if self.battery_level >= 30:
                print ("search completed , Area:LARGE ,Result :",self.result,"people found.")
            else:
                print("battery is not enough")

class MedicalDrone(Drone):
    def __init__(self,id,name,battery_level,current_status=None,complete_missions_count =0,medical_shipment,can_carry_critical):
    super().def__init__(self.id,name,battery_level,current_status=None,complete_missions_count =0)
        
    def success_medical_mission(self):
        if self.battery_level>=25:
            print("successful mission")
        else:
            print("the mission is not successful")

class Charging:
    def __init__(self):
        self.battery_level = Drone()
    if battery_level<20:
        print("no new mission")
        self.current_status = Charging

class Fix:
    def __init__(self):
        self.current_status = MAINTENANCE
        print("can not be charghing or has mission")
    
class Users:
    def __init__(self,user_id,name,username,_password):
        self.user_id = user_id
        self.name = name
        self.user_name = {}
        self._password = password
    # def validate_user(user_name):
    #     if user_name in user_name:
    #         raise ValueError ("this user name is duplicated")
    def validate_password(password):
        if not len(password)==8:
            raise ValueError ("password must have 8 characters")
            
class Operator(Users):
    def __init__(self,user_id,name,username,_password,):
    super().def __init__(self,user_id,name,username,_password):
    def show_drone(self):
    def register_new_mission(self):
    def assigned_drone(self):
    def 
    
class Admin(Users):
class AccessLevels(ABC):
class Missions(ABC):
    def __init__(self,mission_id,title,priority,creator,assigned_drone,status = pending):
        self.mission_id = mission_id
        self.title = title
        self.priority = [1,2,3,4,5]
        self.creator = creator
        self.assigned_drone = assigned_drone
        self.status = [pending,assigned,in_progress,completed,failed,cancelled]

class Activity_Reports:
assigned_drone

class ControlCenter:
    def __init__(self):
    def Drone_search(id):
    def Users_search():
    def Mission_search():
    def Register_events():



    


