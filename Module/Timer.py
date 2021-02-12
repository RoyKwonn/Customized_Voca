from threading import Timer
timeout = 5
t = Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt = "You have %d seconds to choose the correct answer ...\n" % timeout
answer = input(prompt)
t.cancel()