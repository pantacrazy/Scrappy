import argparse
from process_command import command
class CLI:
    def __init__(self):
        #Start the parser
        self.parser = argparse.ArgumentParser(description="Task Tracker")
        self.parser.add_argument("comando",help="Command of the aplication", nargs='+')
    
    #Parsing the args
    def parse(self):
        args = self.parser.parse_args()
        answer=args.comando
        orders=command(*answer)
        orders.process_command(*answer)
if __name__ == "__main__":
    cli = CLI()
    cli.parse()