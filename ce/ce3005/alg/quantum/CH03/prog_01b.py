from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector 

qc = QuantumCircuit(2)
qc.x(1)
qc.draw("mpl")


state = Statevector.from_instruction(qc) 
state.draw('bloch')