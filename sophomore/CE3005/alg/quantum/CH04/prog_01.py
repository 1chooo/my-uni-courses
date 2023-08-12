from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.cx(0, 1)
qc.draw("mpl")