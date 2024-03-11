from qiskit import QuantumRegister, QuantumCircuit

qrx = QuantumRegister(3, 'x')
qry = QuantumRegister(1, 'y')
qc = QuantumCircuit(qrx, qry)
qc.cx(qrx[0], qry)

qc.draw("mpl")