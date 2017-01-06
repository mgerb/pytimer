import time, sys, os

sys.argv.pop(0)
variables = " ".join(str(x) for x in sys.argv)

start = time.time()
os.system(variables)
end = time.time()

print "Time elapsed " + str(end - start)