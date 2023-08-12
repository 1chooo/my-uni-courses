from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

qrx = QuantumRegister(3, 'x')
qry = QuantumRegister(2, 'y')
qrz = QuantumRegister(1, 'z')
cr = ClassicalRegister(4, 'c')
qc = QuantumCircuit(qrx,qry,qrz,cr) 
qc.measure([qrx[1], qrx[2]], [cr[0], cr[1]]) 
qc.measure([4, 5], [2, 3])
qc.draw()