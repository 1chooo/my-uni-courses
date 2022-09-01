from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector 

qc = QuantumCircuit(3)
qc.x(0)
qc.y(1)
qc.z(2)
print(qc)
qc.draw("mpl")


state = Statevector.from_instruction(qc) 
state.draw('bloch')