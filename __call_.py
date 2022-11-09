class GiveName():
    def __init__(self):
        print("this is class ")
    
    # this function is used to call the instance as the function   
    def __call__(self):
        print("This is called")
        
if __name__=="__main__":
    name1 = GiveName()
    name1()
