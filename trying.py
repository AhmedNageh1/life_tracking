def enter_activities(Act:list):
    list_lenth =len(Act)
    values = [0 for val in Act]
    return dict(zip(Act ,values))
  
act = ["that", "is" , "cool"]
print(enter_activities(act))