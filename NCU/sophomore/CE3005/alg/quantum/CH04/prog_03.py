from qiskit import QuantumCircuit, Aer
from qiskit.visualization import array_to_latex

sim = Aer.get_backend("aer_simulator")
qc = QuantumCircuit(2)
qc.cx(0, 1)
display(qc.draw("mpl"))
qc.save_unitary()
unitary = sim.run(qc).result().get_unitary()
display(array_to_latex(unitary, prefix="\\text{CNOT (LSB as Target) = }"))