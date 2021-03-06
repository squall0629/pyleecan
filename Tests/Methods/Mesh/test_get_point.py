# -*- coding: utf-8 -*-
import pytest
from unittest import TestCase
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
from pyleecan.Classes.CellMat import CellMat
import numpy as np


@pytest.mark.MeshSol
class unittest_get_point(TestCase):
    """unittest for points getter methods"""

    @classmethod
    def setUp(self):
        self.mesh = MeshMat()
        self.mesh.point = PointMat()
        self.mesh.point.add_point(np.array([0, 0]))
        self.mesh.point.add_point(np.array([1, 0]))
        self.mesh.point.add_point(np.array([1, 2]))
        self.mesh.point.add_point(np.array([2, 3]))
        self.mesh.point.add_point(np.array([3, 3]))

    def test_MeshMat_triangle3(self):
        """unittest with CellMat and PointMat objects, only Triangle3 elements are defined"""

        points = self.mesh.get_point(indices=[1, 2])
        solution = np.array([[1, 0], [1, 2]])

        testA = np.sum(abs(solution - points))
        msg = (
            "Wrong projection: returned " + str(points) + ", expected: " + str(solution)
        )
        DELTA = 1e-10
        self.assertAlmostEqual(testA, 0, msg=msg, delta=DELTA)
