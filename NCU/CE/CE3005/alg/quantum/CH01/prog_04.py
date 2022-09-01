from qiskit import QuantumCircuit, transpile, execute 
from qiskit.providers.aer import AerSimulator

sim = AerSimulator()
qc = QuantumCircuit(1, 1)
qc.measure([0], [0])
print(qc)
cqc = transpile(qc, sim)
job=execute(cqc, backend = sim, shots = 1000) 
result = job.result()
counts = result.get_counts(qc)
print("Total counts for qubit states are:", counts)