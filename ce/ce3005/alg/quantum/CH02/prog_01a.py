from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4,4)
qc.initialize([1,0],0)
qc.initialize([0,1],1) 
qc.initialize([1/math.sqrt(2), 1/math.sqrt(2)],2) 
qc.initialize([1/math.sqrt(2), -1/math.sqrt(2)],3) 
qc.draw("mpl")