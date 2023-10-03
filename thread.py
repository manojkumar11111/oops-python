import threading

def hello(name):
    print(f"hi {name}")
def bye(name):
    print(f" bye {name}")
if __name__ == "__main__":
    t1=threading.Thread(target=hello,args=("manoj",))

    t2=threading.Thread(target=bye,args=("manoj",))


    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("donr!")