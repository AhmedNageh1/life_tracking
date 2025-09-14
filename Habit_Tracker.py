import json

#  structure in Python (same as My JSON file)
data = {
"Days" :{
    "Monday":{
        "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    },

    "Tuesday":
    {
        "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    },
   "Wednesday":
    {
       "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    },
    "Thursday":
     {
        "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    },
    "Friday":
        {
         "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    },
    "Saturday":
        {
         "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
        },
    "Sunday":
        {
         "Spiritual" :{} ,
        "Health":{}  ,
        "Education":{} ,
        "Finance":{},
        "Relationships":{}
    }
}

}


def add_activity(data, day, aspect, activity_name, default_value=0):
    """Add a new Activity"""
    if day not in data["Days"]:
        print("Day not found!")
        return
    if aspect not in data["Days"][day]:
        print("Aspect not found!")
        return
    
    data["Days"][day][aspect][activity_name] = default_value

    
def add_values(data,day,aspect):
    if day not in data["Days"]:
        print("Days not Found")
        return
    if aspect not in data["Days"][day]:
        print("Aspect not found!")
        return
    for i in data.items:
        value = input(f["Days"][day][aspect][activity_name])




def delete_activity(data, day, aspect, activity_name):
    """Delete Existing Activity"""
    if day not in data["Days"]:
        print("Day not found!")
        return
    if aspect not in data["Days"][day]:
        print("Aspect not found!")
        return
    if activity_name not in data["Days"][day][aspect]:
        print("Activity not found!")
        return
    
    del data["Days"][day][aspect][activity_name]


def update_activity(data,day , aspect, old_activity_name, new_activity_name, default_value=0):
    """Update Existing Activity"""
    if day not in data["Days"]:
        print("Day not found!")
        return
    if aspect not in data["Days"][day]:
        print("Aspect not found!")
        return
    if old_activity_name not in data["Days"][day][aspect]:
        print("Activity not found!")
        return
    
    # Get old value
    value = data["Days"][day][aspect][old_activity_name]
    
    # Remove old activity
    del data["Days"][day][aspect][old_activity_name]
    
    # Add new activity with same value
    data["Days"][day][aspect][new_activity_name] = value

add_activity(data,"Monday","Spiritual","Fajr")
add_activity(data,"Monday","Spiritual","Dohr")
print(json.dumps(data["Days"]["Monday"]["Spiritual"],indent = 4))

delete_activity(data,"Monday","Spiritual","Dohr")
print(json.dumps(data["Days"]["Monday"]["Spiritual"],indent = 4))

update_activity(data,"Monday","Spiritual","Fajr","Asr")
print(json.dumps(data["Days"]["Monday"]["Spiritual"],indent = 4))

