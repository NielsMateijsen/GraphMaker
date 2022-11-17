import graph_creator
import time
import data_getter

if __name__ == '__main__':
    while True:
        graph_creator.create_all_graphs()
        time.sleep(5*60)
