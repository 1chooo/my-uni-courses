from qiskit import QuantumCircuit 

qc = QuantumCircuit(2)
qc.x(1)
qc.draw("mpl")