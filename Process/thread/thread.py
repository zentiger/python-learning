import _thread
import time

loops = [4, 2]

def loop(nloop, nsec, lock):
    print(f'Start loop: {nloop}, at: {time.ctime()}')
    time.sleep(nsec)
    print(f'End loop: {nloop}, at: {time.ctime()}')
    lock.release()

def main():
    print(f'Starting at: {time.ctime()}')
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i, loops[i], locks[i]))
	
    for i in nloops:
        while locks[i].locked(): pass
    
    print(f'All done at: {time.ctime()}')

if __name__ == "__main__":
    main()