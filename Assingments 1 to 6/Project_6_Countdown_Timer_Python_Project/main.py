import time 

def main(times):
    while times:
        mins, secs = divmod(times, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        times -= 1

    
    print("\nTimer Completed!")

times =input("\nEnter the time in seconds: ")
        
    


if __name__ == "__main__":
    main(int(times))
