import json,datetime, os
class file_json:
    def __init__(self,file):
        self.file = file
        if (not os.path.exists(self.file)):
            file=open(self.file, "w")
            file.close()
        file_json = open(self.file, "r", encoding='utf-8-sig')
        if file_json.read()=="":
            self.json=[]
        else:
            file_json.seek(0)
            self.json = json.load(file_json)
            file_json.close()
    def add_task(self,description):
        date=datetime.datetime.now().isoformat()
        id=self.get_last_task()
        self.json.append({'id':id,"description":description,'status':'todo','createdAt':date,'updatedAt':date})
        self.save()
        print(f"Output: Task added successfully (ID: {id})")
    def get_last_task(self):
        return len(self.json)
    def update_id(self,id,description):
        id_test=int(id)
        find=False
        for element in self.json:
            if element['id']==id_test:
                element['description']=description
                element['updatedAt']=datetime.datetime.now().isoformat()
                find=True
                break
        if find==False:
            print("That task dont exists")
        else:
            self.save()
            print(f"Task {id_test} updated")
    def delete(self,id):
        id_test=int(id)
        find=False
        for i,element in enumerate(self.json):
            if element['id']==id_test:
                del self.json[i]   
                find=True
                break
        if find==False:
            print("That task dont exists")
        else:
            self.save()
            print(f"Task {id_test} deleted")
    def mark_in_progress(self,id):
        id_test=int(id)
        find=False
        for element in self.json:
            if element['id']==id_test:
                element['status']='in-progress'
                element['updatedAt']=datetime.datetime.now().isoformat()  
                find=True
                break
        if find==False:
            print("That task dont exists")
        else:
            self.save()
            print(f"Mark task {id_test} as in-progress")
    def mark_done(self,id):
        id_test=int(id)
        find=False
        for element in self.json:
            if element['id']==id_test:
                element['status']='done'
                element['updatedAt']=datetime.datetime.now().isoformat()
                find=True
                break
        if find==False:
            print("That task dont exists")
        else:
            self.save()
            print(f"Mark task {id_test} as done")
    def save(self):
        file_json = open(self.file,'w')
        json.dump(self.json,file_json,indent=4)
        file_json.close()
    def list(self):
        print("Listing all tasks")
        for element in self.json:
            print(element)
    def list_by_status(self,status):
        print("Listing tasks by status")
        for element in self.json:
            if element['status']==status:
                print(element)
