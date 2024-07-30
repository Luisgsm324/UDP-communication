test = {"1": "1", "2": "2"}

print("3" in list(test.keys()))

import time
import threading

pretendedtime = 10
global ackreceive
ack_receive = False

def timer():
  for _ in range(pretendedtime):
      time.sleep(1)
      if ack_receive:
          print("CHEGOU")
          break

  if not ack_receive:
      print("nao chegou")
      pass

def nao_sei():
  global ack_receive
  time.sleep(3)
  ack_receive = True


thread_receive = threading.Thread(target=nao_sei)
thread_receive = thread_receive.start()
thread_send = threading.Thread(target=timer)
thread_send.start()

import timeit
pretendedtime = 0.01
def minha_funcao():
    times = 100
    for _ in range(times):
       time.sleep(pretendedtime/times)
       a = 2
       print(a)

# Mede o tempo de execução
tempo_execucao = timeit.timeit(minha_funcao, globals=globals(), number=1)

print(f"Tempo de execução: {tempo_execucao:.4f} segundos")


a =  'teste'
print(a[0:-1])