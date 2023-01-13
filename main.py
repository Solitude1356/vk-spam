from src import session, utils
from loguru import logger
from threading import Thread, Barrier

# THREADS = 5

import concurrent.futures


def do_job(sessions):
   logger.warning('Session loaded!')
   for s in sessions:
      s.start()

def main():
   with open('links.txt', encoding="utf-8") as lnk, open('messages.txt', encoding="utf-8") as msg, open('accounts.txt') as accounts:
      lnk, msg, accounts = lnk.read().split('\n'), msg.read().split('\n'), [ac.split(':') for ac in accounts.read().split('\n')]
      links = utils.check_links(lnk)

      sessions = []
      for ac in accounts:
         login, password = ac[0], ac[1]
         a = session.Session(login, password)
         sessions.append(Thread(target=a.comment_posts, args=(links, msg)))
      
      do_job(sessions)


if __name__ == '__main__':
   main()


'''
import concurrent.futures
import time
import requests

urls = [
    'http://example.com/1',
    'http://example.com/2',
    'http://example.com/3',
    # ...
]


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(requests.get, urls))
    for response in results:
        print(response.status_code)
'''



'''
import concurrent.futures

class MyObject:
    def __init__(self, value):
        self.value = value

    def multiply(self, factor):
        return self.value * factor


objects_args = [(10, 2), (20, 3), (30, 4)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(lambda args: MyObject(*args).multiply(), objects_args))
    print(results)  # prints [20, 60, 120]
'''