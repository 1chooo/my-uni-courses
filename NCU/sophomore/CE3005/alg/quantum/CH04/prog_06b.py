from qiskit import execute 
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit 
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2, 2)
sv = Statevector.from_label("10")
qc.initialize(sv, range(2))
qc.h(0)
qc.cx(0, 1)
qc.measure(range(2), range(2))
qc.draw("mpl")


sim = AerSimulator()
job = execute(qc, backend = sim, shots = 1000)
result = job.result()
counts = result.get_counts(qc)
print("Counts: ", counts)
plot_histogram(counts)