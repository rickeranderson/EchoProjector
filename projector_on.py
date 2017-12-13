from pypjlink import Projector

p = Projector.from_address('192.168.1.4')
p.authenticate('')
p.set_power('on')