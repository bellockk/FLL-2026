# from hub import light_matrix
# import runloop
# 
# async def main():
#     await light_matrix.write('Hi!')
# 
# runloop.run(main())


from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()
wait(10000)
print('hi!')

hub.speaker.beep()