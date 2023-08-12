from qiskit import QuantumCircuit, Aer
from qiskit.visualization import array_to_latex

qc = QuantumCircuit(2)
qc.cx(0, 1)
display(qc.draw("mpl"))
sim = Aer.get_backend("aer_simulator")
qc.save_unitary()
unitary = sim.run(qc).result().get_unitary()
display(array_to_latex(unitary, prefix="\\text{CNOT (MSB as Target) = }"))