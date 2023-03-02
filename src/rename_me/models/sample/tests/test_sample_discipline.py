"""
Test module for sample discipline
"""
#  This file is part of FAST : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2020  ONERA & ISAE-SUPAERO
#  FAST is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os.path as pth
from os import mkdir
from shutil import rmtree

import fastoad.api as oad
import pytest
from fastoad._utils.testing import run_system

from ..sample_discipline import SampleDiscipline

DATA_FOLDER_PATH = pth.join(pth.dirname(__file__), "data")
RESULTS_FOLDER_PATH = pth.join(
    pth.dirname(__file__), "results", pth.splitext(pth.basename(__file__))[0]
)


@pytest.fixture(scope="module")
def cleanup():
    rmtree(RESULTS_FOLDER_PATH, ignore_errors=True)
    mkdir(RESULTS_FOLDER_PATH)


def test_sample_discipline():
    """Tests computation of the sample discipline."""

    # Research independent input value in .xml file
    ivc = oad.DataFile(pth.join(DATA_FOLDER_PATH, "data.xml")).to_ivc()

    # Run problem and check obtained value(s) is/(are) correct
    problem = run_system(SampleDiscipline(), ivc)
    sample_output = problem.get_val("sample_output", units="kg")
    assert sample_output == pytest.approx(4.0, abs=1e-3)
