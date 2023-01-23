from qiskit import QuantumCircuit 

qc = QuantumCircuit(3)
qc.x(0)
qc.y(1)
qc.z(2)
print(qc)
qc.draw("mpl")