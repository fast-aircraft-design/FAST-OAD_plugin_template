# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import os.path as pth
from os import mkdir
from shutil import rmtree

import fastoad.api as oad
import pytest

DATA_FOLDER_PATH = pth.join(pth.dirname(__file__), "data")
RESULTS_FOLDER_PATH = pth.join(
    pth.dirname(__file__), "results", pth.splitext(pth.basename(__file__))[0]
)


@pytest.fixture(scope="module")
def cleanup():
    rmtree(RESULTS_FOLDER_PATH, ignore_errors=True)
    mkdir(RESULTS_FOLDER_PATH)


def test_sample_process():
    configurator = oad.FASTOADProblemConfigurator(pth.join(DATA_FOLDER_PATH, "conf.yml"))
    ref_inputs = pth.join(DATA_FOLDER_PATH, "data.xml")

    oad.DataFile(ref_inputs)

    # Create problem with inputs
    problem = configurator.get_problem()
    problem.write_needed_inputs(ref_inputs)
    problem.read_inputs()

    # Setup problem
    problem.setup()

    # Run problem
    problem.run_model()

    # Writes outputs
    problem.write_outputs()
