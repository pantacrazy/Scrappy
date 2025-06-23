from json_layer import file_json
jsonfile='task.json'
errorMessage='Invalid Command'
class command:
    choices=['add','update','delete','list','mark-in-progress','mark-done']
    def __init__(self, *args):
        if args[0] not in self.choices:
            print(errorMessage)
            exit()
        else:
            self.command=args[0]
    def process_command(self, *args):
        if self.command=='add':
            if len(args)<2:
                print(errorMessage)
            else:
                self.command_add_task(args[1])
        elif self.command=='update':
            if len(args)<3:
                print(errorMessage)
            else:
                self.command_update_task(args[1],args[2])
        elif self.command=='delete':
            if len(args)<2:
                print(errorMessage)
            else:
                self.command_delete_task(args[1])
        elif self.command=='list':
            self.command_list_tasks(*args)
        elif self.command=='mark-in-progress':
            if len(args)<2:
                print(errorMessage)
            else:
                self.command_mark_in_progress(args[1])
        elif self.command=='mark-done':
            if len(args)<2:
                print(errorMessage)
            else:
                self.command_mark_done(args[1])
            
    def command_add_task(self,task):
        if type(task) != str:
            print(errorMessage)
        else:
            file=file_json(jsonfile)
            file.add_task(task)
    def command_update_task(self,target,change):
        if ((not target.isnumeric()) or (type(change) != str)):
            print(errorMessage)
        else:
            file=file_json(jsonfile)
            file.update_id(target,change)
    def command_delete_task(self,target):
        if not target.isnumeric():
            print(errorMessage)
        else:
            file=file_json(jsonfile)
            file.delete(target)
    def command_list_tasks(self,*args):
        if len(args)>1:
            total=False
        else:
            total=True
        file=file_json(jsonfile)
        if total:
            file.list()
        else:
            file.list_by_status(args[1])
    def command_mark_in_progress(self,target):
        if not target.isnumeric():
            print(errorMessage)
        else:
            file=file_json(jsonfile)
            file.mark_in_progress(target)
    def command_mark_done(self,target):
        if not target.isnumeric():
            print(errorMessage)
        else:
            file=file_json(jsonfile)
            file.mark_done(target)