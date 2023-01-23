from qiskit import QuantumCircuit
import math
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
qc.rx(math.pi/2, 0)
qc.ry(math.pi/2, 1)
qc.rz(math.pi/2, 2)
qc.draw("mpl")


state = Statevector.from_instruction(qc) 
state.draw('bloch')