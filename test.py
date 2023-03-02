import src.owl01 as owl

m: owl.AirplaneManager = owl.get_airplane_manager()
m.flush()
a: owl.AirplaneController = m.get_airplane("127.0.0.1")
b: owl.AirplaneController = m.get_airplane("127.0.0.2")
c: owl.AirplaneController = m.get_airplane("127.0.0.3")
planes = [a, b, c]
m.start()
# a.mode()
for i in planes:
    i.takeoff(100)
m.sleep(1)
for i in planes:
    i.forward(100)
m.sleep(1)
for i in planes:
    i.left(100)
m.sleep(1)
for i in planes:
    i.back(100)
m.sleep(1)
for i in planes:
    i.right(100)
m.sleep(1)
for i in planes:
    i.land()
m.sleep(1)
