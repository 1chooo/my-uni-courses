from qiskit import QuantumCircuit, Aer
from qiskit.visualization import array_to_latex

sim = Aer.get_backend("aer_simulator")
qc1 = QuantumCircuit(3)
qc1.ccx(0, 1, 2)
display(qc1.draw("mpl"))
qc1.save_unitary()
unitary = sim.run(qc1).result().get_unitary()
display(array_to_latex(unitary, prefix="\\text{CNOT (MSB as Target) = }"))
print('=' * 80)
qc2 = QuantumCircuit(3)
qc2.ccx(2, 1, 0)
display(qc2.draw("mpl"))
qc2.save_unitary()
unitary = sim.run(qc2).result().get_unitary()
display(array_to_latex(unitary, prefix="\\text{CNOT (LSB as Target) = }"))