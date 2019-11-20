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
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, BasicAer
from .backends.fake_melbourne import FakeMelbourne


import copy
import numpy as np
from qiskit.chemistry import QiskitChemistry
#import warnings
#warnings.filterwarnings('ignore')
# setup qiskit.chemistry logging
#import logging
from qiskit.chemistry import set_qiskit_chemistry_logging
#set_qiskit_chemistry_logging(logging.ERROR) # choose among DEBUG, INFO, WARNING, ERROR, CRITICAL and NOTSET


def VQE_circuit(depth_level):
    qiskit_chemistry_dict = {
    'driver': {'name': 'HDF5'},
    'HDF5': {'hdf5_input': 'H2/H2_equilibrium_0.735_sto-3g.hdf5'},
    'operator': {'name':'hamiltonian', 
                 'qubit_mapping': 'parity', 
                 'two_qubit_reduction': True},
    'algorithm': {'name': 'ExactEigensolver'}
    }
    qiskit_chemistry_dict['algorithm']['name'] = 'VQE'
    qiskit_chemistry_dict['optimizer'] = {'name': 'SPSA', 'max_trials': 350}
    qiskit_chemistry_dict['variational_form'] = {'name': 'RYRZ', 'depth': depth_level, 'entanglement':'full'}
    return qiskit_chemistry_dict

class VQEBenchmarks:
    params = ([0, 1, 2, 3])
    param_names = ['op_level']
    
    depth_level=4
    
    def setup(self, depth_level):
        #seed = 42
        self.backend = BasicAer.get_backend('statevector_simulator')
        self.circuit = VQE_circuit(depth_level)
    def time_optimize_level(self,op_level):
        transpile(self.circuit,self.backend,optimization_level=op_level)
# solver = QiskitChemistry()
# result = solver.run(qiskit_chemistry_dict, backend=backend)
