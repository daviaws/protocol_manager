from identifier import get_identifier
from events import Event, Requisition
from protocols import Protocol

identifier = get_identifier()
protocols = []

pSV = Protocol(identifier.generate_uid(), 'SV')
pIPW = Protocol(identifier.generate_uid(), 'IPW')

evACK = Event(identifier.generate_uid(), 'ack', {'id' : int})
evSVSendSST = Event(identifier.generate_uid(), 'send_sensors_status', {'id' : int, 'sensors_stauts' : {'1' : int, '2' : int}})

reqSVGETSST = Requisition(identifier.generate_uid(), 'get_sensors_status', {'id' : int, 'ipwall_id' : int})
reqSVGETSST.add_evt(evACK)
reqSVGETSST.add_evt(evSVSendSST)

reqIPWGETSST = Requisition(identifier.generate_uid(), 'get_sensors_status', {'id' : int})

print(reqSVGETSST)