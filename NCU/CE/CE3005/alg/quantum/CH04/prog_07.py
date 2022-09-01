from qiskit import QuantumCircuit

qc = QuantumCircuit(12)
qc.cx(0, 1)
qc.cx(2, 3)
qc.cx(4, 5)
qc.cx(6, 7)
qc.cx(8, 9)
qc.cx(10, 11)
qc.cx(11, 10)
qc.cx(10, 11)

qc.draw("mpl")