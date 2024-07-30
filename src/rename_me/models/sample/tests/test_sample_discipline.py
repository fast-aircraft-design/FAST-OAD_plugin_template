"""Test module for sample discipline"""

import shutil
from pathlib import Path

import fastoad.api as oad
import pytest
from fastoad.testing import run_system

from ..sample_discipline import SampleDiscipline

DATA_FOLDER_PATH = Path(__file__).parent / "data"
RESULTS_FOLDER_PATH = Path(__file__).parent / "results" / Path(__file__).stem


@pytest.fixture(scope="module")
def cleanup():
    shutil.rmtree(RESULTS_FOLDER_PATH, ignore_errors=True)
    RESULTS_FOLDER_PATH.mkdir()


def test_sample_discipline():
    """Tests computation of the sample discipline."""

    # Research independent input value in .xml file
    inputs = oad.DataFile(DATA_FOLDER_PATH / "data.xml")

    # Run problem and check obtained value(s) is/(are) correct
    problem = run_system(SampleDiscipline(), inputs)
    sample_output = problem.get_val("sample_output", units="kg")
    assert sample_output == pytest.approx(4.0, abs=1e-3)
