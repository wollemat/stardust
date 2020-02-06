from multiprocessing import Process
from multiprocessing import Pipe

from planet import cut_out_planet

from config import NUMBER_OF_WORKERS
from config import _GRID_SIZE


def worker_function(conn):
    msg = conn.recv()

    if isinstance(msg, int):
        conn.send(cut_out_planet(msg))
        worker_function(conn)
        return

    if isinstance(msg, str):
        if msg == "stop":
            return

    print("Something went wrong")


def initialize_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        parent_connection, child_connection = Pipe()
        process = Process(target=worker_function, args=(child_connection,))
        processes.append(process)
        conns.append(parent_connection)
    print("Workers are initialized")


def start_workers(processes):
    for i in range(NUMBER_OF_WORKERS):
        processes[i].start()
    print("Workers have started")


def delegate_workers(conns, counter):
    for i in range(NUMBER_OF_WORKERS):
        if counter == _GRID_SIZE:
            break
        conns[i].send(counter)
        counter += 1


def collect_from_workers(conns, counter, video):
    for i in range(NUMBER_OF_WORKERS):
        if counter == _GRID_SIZE:
            break
        video.write(conns[i].recv())
        counter += 1


def stop_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        conns[i].send("stop")
    for i in range(NUMBER_OF_WORKERS):
        processes[i].join()
    print("Workers have been stopped")
