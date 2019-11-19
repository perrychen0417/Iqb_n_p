# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=no-member,invalid-name,missing-docstring,no-name-in-module
# pylint: disable=attribute-defined-outside-init,unsubscriptable-object

from qiskit.compiler import transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from .backends.fake_melbourne import FakeMelbourne

def phase_oracle(circuit, register):
    circuit.x(register[0])
    circuit.cz(register[0], register[1])
    circuit.x(register[0])

def inversion_about_average(circuit, register):
    """Apply inversion about the average step of Grover's algorithm."""
    circuit.h(register)
    circuit.x(register)
    circuit.h(register[1])
    circuit.cx(register[0], register[1])
    circuit.h(register[1])
    circuit.x(register)
    circuit.h(register)

def get_grover_circuit():
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)

    groverCircuit = QuantumCircuit(qr,cr)
    groverCircuit.h(qr)

    phase_oracle(groverCircuit, qr)
    inversion_about_average(groverCircuit, qr)

    groverCircuit.measure(qr,cr)




class GroverBenchmarks:
    params = ([0, 1, 2, 3])
    param_names = ['op_level']
    #timeout = 600

    def setup(self, op_level):
        #seed = 42
        self.backend = FakeMelbourne()
        self.circuit = get_grover_circuit()

        #random_circuit(n_qubits, depth, measure=True,
                                      #conditional=True)

    def time_optimize_level(self, op_level):
        transpile(self.circuit,backend=self.backend,optimization_level=op_level)
