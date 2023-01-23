from qiskit import QuantumCircuit,execute
from qiskit.providers.aer import AerSimulator 
from qiskit.visualization import plot_histogram 
import math

qc = QuantumCircuit(2,2)
qc.h(0)
qc.h(1)
qc.measure([0,1],[0,1])
print("This is |++>:")
print(qc)
simulator=AerSimulator()
job=execute(qc, backend=simulator, shots=1000) 
result=job.result() 
counts=result.get_counts(qc) 
print("Counts:",counts)
plot_histogram(counts)