import shutil
from os import mkdir
from pathlib import Path

import fastoad.api as oad
import pytest

DATA_FOLDER_PATH = Path(__file__).parent / "data"
RESULTS_FOLDER_PATH = Path(__file__).parent / "results" / Path(__file__).stem


@pytest.fixture(scope="module")
def cleanup():
    shutil.rmtree(RESULTS_FOLDER_PATH, ignore_errors=True)
    mkdir(RESULTS_FOLDER_PATH)


def test_sample_process():
    configurator = oad.FASTOADProblemConfigurator((DATA_FOLDER_PATH / "conf.yml").as_posix())
    ref_inputs = (DATA_FOLDER_PATH / "data.xml").as_posix()

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
