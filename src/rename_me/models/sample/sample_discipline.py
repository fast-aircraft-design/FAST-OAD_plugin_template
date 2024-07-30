"""Sample module to provide a simple basis for FAST-OAD model."""

import fastoad.api as oad
import numpy as np
import openmdao.api as om
from fastoad.module_management.constants import ModelDomain


@oad.RegisterOpenMDAOSystem("fastoad.sample_plugin.sample_discipline", domain=ModelDomain.OTHER)
class SampleDiscipline(om.ExplicitComponent):
    """
    Sample discipline to give an example of how to register a custom module.
    """

    def setup(self):
        self.add_input("sample_input", val=np.nan, units="kg")

        self.add_output("sample_output", units="kg")

    def setup_partials(self):
        # self.declare_partials("*", "*", method="fd")  # The brutal and easy way
        self.declare_partials("sample_output", "sample_input", method="exact")

    def compute(self, inputs, outputs, discrete_inputs=None, discrete_outputs=None):
        outputs["sample_output"] = 2.0 * inputs["sample_input"]

    def compute_partials(self, inputs, partials, discrete_inputs=None):
        partials["sample_output"] = 2.0
