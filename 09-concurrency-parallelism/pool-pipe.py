from multiprocessing import Process, Pipe
from time import sleep

def worker(conn):
    print('Worker - started now sleeping for 1 second')
    sleep(1)
    print('Worker - sending data via Pipe')
    conn.send('Hello!')
    print('Worker - closing worker end of connection')
    conn.close()
    
def main():
    print('Main - starting, creating the pipe')
    main_connection, worker_connection = Pipe()
    print('Main - setting up the process')
    p = Process(target=worker, args=[worker_connection])
    print('Main - Starting the process')
    p.start()
    print('Main - Wait for a response from the child process')
    print(main_connection.recv())
    print('Main - Closing parent process end of conenction')
    main_connection.close()
    print('Main - Done')
    
if __name__ == '__main__':
    main()