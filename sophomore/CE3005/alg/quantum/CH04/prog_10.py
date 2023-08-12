from qiskit import QuantumCircuit

qc = QuantumCircuit(7)
qc.ccx(0, 1, 4)
qc.ccx(2, 3, 5)
qc.ccx(4, 5, 6)
qc.draw("mpl")