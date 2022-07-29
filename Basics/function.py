def div(a,b):
    try:
        return a/b
    except:
        print("error")

    finally:
        print("wrap up") # it will also execute
        return 10 # always will give this answer and discard the previous return
if __name__ == "__main__":
    print(div(10, 2))
    
