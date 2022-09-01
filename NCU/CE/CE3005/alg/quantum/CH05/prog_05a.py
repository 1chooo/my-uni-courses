from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

qrx = QuantumRegister(3, 'x')
qry = QuantumRegister(1, 'y')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qrx, qry, cr)
qc.h(qrx)
qc.x(qry)       
# qc.h(qry) 機率會不同
qc.h(qry)
qc.barrier()
qc.cx(qrx[0], qry)
qc.barrier()
qc.h(qrx)
qc.h(qry)
qc.measure(qrx, cr)

qc.draw("mpl")