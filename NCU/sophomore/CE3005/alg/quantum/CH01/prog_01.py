from qiskit import QuantumCircuit

print("Hello, Qubit!")
qc = QuantumCircuit(1,1)
qc.measure([0], [0])
print("This is the quantum circuit of 1 qubit and 1 bit:")
qc.draw('mpl')