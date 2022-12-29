#
#this program is used to study the runtimes of other programs using c_profile module 

#another way to start the time your program consume is to use the time mo
import time 
import cProfile
from palingram import palingram

start_time = time.time()
cProfile.run("palingram()")
end_time = time.time()

print(start_time-end_time)