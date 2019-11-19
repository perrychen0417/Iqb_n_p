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

from qiskit.compiler import assemble

import ../grover.py


class GroverBenchmarks:
    params = ([0, 1, 2, 3])
    param_names = ['op_level']
    #timeout = 600

    def setup(self, op_level):
        #seed = 42
        self.circuit = grover_curcuit(op_level)
        #random_circuit(n_qubits, depth, measure=True,
                                      conditional=True)

    def time_optimize_level(self, _, __):
        #assemble(self.circuit)
