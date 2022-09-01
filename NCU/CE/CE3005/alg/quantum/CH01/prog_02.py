from qiskit import QuantumCircuit

print("This is the quantum circuit of 5 qubits and 2 bits: ")
qc = QuantumCircuit(5, 2)
qc.measure([1, 3], [0, 1])
qc.draw("mpl")