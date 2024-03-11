from qiskit import QuantumCircuit, QuantumRegister

qrx = QuantumRegister(3, 'x')
qry = QuantumRegister(1, 'y')
qc = QuantumCircuit(qrx, qry)
qc.x(qry)

qc.draw("mpl")