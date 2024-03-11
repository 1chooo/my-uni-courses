from qiskit import QuantumCircuit,execute
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
import math

qc = QuantumCircuit(1,1)
qc.x(0)
qc.h(0)
qc.measure([0],[0])
print("This is |->:")
print(qc)
simulator=AerSimulator()
job=execute(qc, backend=simulator, shots=1000)
result=job.result()
counts=result.get_counts(qc)
print("Counts:",counts)
plot_histogram(counts)