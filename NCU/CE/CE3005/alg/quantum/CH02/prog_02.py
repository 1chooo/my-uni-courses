from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(4, 4)
qc.initialize([1, 0], 0)
qc.initialize([1, 0], 1)
qc.initialize([0, 1], 2)
qc.initialize([0, 1], 3)

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
print(qc)
simulator=AerSimulator()
job=execute(qc, backend=simulator, shots=1000)
result=job.result()
counts=result.get_counts(qc)
print("Counts:",counts)
plot_histogram(counts)