# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for divitional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License") you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at
# https://github.com/ai-techsystems/dnnCompiler


# This file is auto generated by tensor_op_gen.py

import common

import dnnc as dc
import numpy as np
import unittest

class tensorOperatorsTest(unittest.TestCase):

	def setUp(self):

		self.np_bool_0_4 = np.arange(5).astype(np.bool)
		self.np_bool_5_9 = np.arange(5,10).astype(np.bool)

		self.np_int_0_4 = np.arange(5).astype(np.int)
		self.np_int_5_9 = np.arange(5,10).astype(np.int)

		self.np_float_0_4 = np.arange(5).astype(np.float)
		self.np_float_5_9 = np.arange(5,10).astype(np.float)

		self.np_double_0_4 = np.arange(5).astype(np.double)
		self.np_double_5_9 = np.arange(5,10).astype(np.double)

		self.dc_bool_0_4 = dc.arange(5).asTypeBool()
		self.dc_bool_5_9 = dc.arange(5,10).asTypeBool()

		self.dc_int_0_4 = dc.arange(5).asTypeInt()
		self.dc_int_5_9 = dc.arange(5,10).asTypeInt()

		self.dc_float_0_4 = dc.arange(5).asTypeFloat()
		self.dc_float_5_9 = dc.arange(5,10).asTypeFloat()

		self.dc_double_0_4 = dc.arange(5).asTypeDouble()
		self.dc_double_5_9 = dc.arange(5,10).asTypeDouble()


	# Comparison Greater_Than

	# bool_tensor_1 > bool_scalar
	def test_Comparison_Greater_Than_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 > True
		temp_dc = self.dc_bool_0_4 > True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 > bool_tensor_2
	def test_Comparison_Greater_Than_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 > self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 > self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 > float_scalar
	def test_Comparison_Greater_Than_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 > 5.0
		temp_dc = self.dc_bool_0_4 > 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 > float_tensor_2
	def test_Comparison_Greater_Than_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 > self.np_float_5_9
		temp_dc = self.dc_bool_0_4 > self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 > int_scalar
	def test_Comparison_Greater_Than_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 > 5
		temp_dc = self.dc_bool_0_4 > 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 > int_tensor_2
	def test_Comparison_Greater_Than_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 > self.np_int_5_9
		temp_dc = self.dc_bool_0_4 > self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > bool_scalar
	def test_Comparison_Greater_Than_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 > True
		temp_dc = self.dc_int_0_4 > True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > bool_tensor_2
	def test_Comparison_Greater_Than_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 > self.np_bool_5_9
		temp_dc = self.dc_int_0_4 > self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > float_scalar
	def test_Comparison_Greater_Than_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 > 5.0
		temp_dc = self.dc_int_0_4 > 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > float_tensor_2
	def test_Comparison_Greater_Than_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 > self.np_float_5_9
		temp_dc = self.dc_int_0_4 > self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > int_scalar
	def test_Comparison_Greater_Than_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 > 5
		temp_dc = self.dc_int_0_4 > 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 > int_tensor_2
	def test_Comparison_Greater_Than_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 > self.np_int_5_9
		temp_dc = self.dc_int_0_4 > self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > bool_scalar
	def test_Comparison_Greater_Than_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 > True
		temp_dc = self.dc_float_0_4 > True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > bool_tensor_2
	def test_Comparison_Greater_Than_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 > self.np_bool_5_9
		temp_dc = self.dc_float_0_4 > self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > float_scalar
	def test_Comparison_Greater_Than_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 > 5.0
		temp_dc = self.dc_float_0_4 > 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > float_tensor_2
	def test_Comparison_Greater_Than_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 > self.np_float_5_9
		temp_dc = self.dc_float_0_4 > self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > int_scalar
	def test_Comparison_Greater_Than_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 > 5
		temp_dc = self.dc_float_0_4 > 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 > int_tensor_2
	def test_Comparison_Greater_Than_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 > self.np_int_5_9
		temp_dc = self.dc_float_0_4 > self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# Comparison Greater_Equal

	# bool_tensor_1 >= bool_scalar
	def test_Comparison_Greater_Equal_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 >= True
		temp_dc = self.dc_bool_0_4 >= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 >= bool_tensor_2
	def test_Comparison_Greater_Equal_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 >= self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 >= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 >= float_scalar
	def test_Comparison_Greater_Equal_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 >= 5.0
		temp_dc = self.dc_bool_0_4 >= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 >= float_tensor_2
	def test_Comparison_Greater_Equal_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 >= self.np_float_5_9
		temp_dc = self.dc_bool_0_4 >= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 >= int_scalar
	def test_Comparison_Greater_Equal_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 >= 5
		temp_dc = self.dc_bool_0_4 >= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 >= int_tensor_2
	def test_Comparison_Greater_Equal_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 >= self.np_int_5_9
		temp_dc = self.dc_bool_0_4 >= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= bool_scalar
	def test_Comparison_Greater_Equal_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 >= True
		temp_dc = self.dc_int_0_4 >= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= bool_tensor_2
	def test_Comparison_Greater_Equal_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 >= self.np_bool_5_9
		temp_dc = self.dc_int_0_4 >= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= float_scalar
	def test_Comparison_Greater_Equal_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 >= 5.0
		temp_dc = self.dc_int_0_4 >= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= float_tensor_2
	def test_Comparison_Greater_Equal_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 >= self.np_float_5_9
		temp_dc = self.dc_int_0_4 >= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= int_scalar
	def test_Comparison_Greater_Equal_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 >= 5
		temp_dc = self.dc_int_0_4 >= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 >= int_tensor_2
	def test_Comparison_Greater_Equal_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 >= self.np_int_5_9
		temp_dc = self.dc_int_0_4 >= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= bool_scalar
	def test_Comparison_Greater_Equal_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 >= True
		temp_dc = self.dc_float_0_4 >= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= bool_tensor_2
	def test_Comparison_Greater_Equal_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 >= self.np_bool_5_9
		temp_dc = self.dc_float_0_4 >= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= float_scalar
	def test_Comparison_Greater_Equal_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 >= 5.0
		temp_dc = self.dc_float_0_4 >= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= float_tensor_2
	def test_Comparison_Greater_Equal_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 >= self.np_float_5_9
		temp_dc = self.dc_float_0_4 >= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= int_scalar
	def test_Comparison_Greater_Equal_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 >= 5
		temp_dc = self.dc_float_0_4 >= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 >= int_tensor_2
	def test_Comparison_Greater_Equal_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 >= self.np_int_5_9
		temp_dc = self.dc_float_0_4 >= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# Comparison Less_Than

	# bool_tensor_1 < bool_scalar
	def test_Comparison_Less_Than_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 < True
		temp_dc = self.dc_bool_0_4 < True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 < bool_tensor_2
	def test_Comparison_Less_Than_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 < self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 < self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 < float_scalar
	def test_Comparison_Less_Than_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 < 5.0
		temp_dc = self.dc_bool_0_4 < 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 < float_tensor_2
	def test_Comparison_Less_Than_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 < self.np_float_5_9
		temp_dc = self.dc_bool_0_4 < self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 < int_scalar
	def test_Comparison_Less_Than_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 < 5
		temp_dc = self.dc_bool_0_4 < 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 < int_tensor_2
	def test_Comparison_Less_Than_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 < self.np_int_5_9
		temp_dc = self.dc_bool_0_4 < self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < bool_scalar
	def test_Comparison_Less_Than_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 < True
		temp_dc = self.dc_int_0_4 < True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < bool_tensor_2
	def test_Comparison_Less_Than_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 < self.np_bool_5_9
		temp_dc = self.dc_int_0_4 < self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < float_scalar
	def test_Comparison_Less_Than_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 < 5.0
		temp_dc = self.dc_int_0_4 < 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < float_tensor_2
	def test_Comparison_Less_Than_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 < self.np_float_5_9
		temp_dc = self.dc_int_0_4 < self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < int_scalar
	def test_Comparison_Less_Than_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 < 5
		temp_dc = self.dc_int_0_4 < 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 < int_tensor_2
	def test_Comparison_Less_Than_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 < self.np_int_5_9
		temp_dc = self.dc_int_0_4 < self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < bool_scalar
	def test_Comparison_Less_Than_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 < True
		temp_dc = self.dc_float_0_4 < True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < bool_tensor_2
	def test_Comparison_Less_Than_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 < self.np_bool_5_9
		temp_dc = self.dc_float_0_4 < self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < float_scalar
	def test_Comparison_Less_Than_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 < 5.0
		temp_dc = self.dc_float_0_4 < 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < float_tensor_2
	def test_Comparison_Less_Than_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 < self.np_float_5_9
		temp_dc = self.dc_float_0_4 < self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < int_scalar
	def test_Comparison_Less_Than_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 < 5
		temp_dc = self.dc_float_0_4 < 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 < int_tensor_2
	def test_Comparison_Less_Than_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 < self.np_int_5_9
		temp_dc = self.dc_float_0_4 < self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# Comparison Less_Equal

	# bool_tensor_1 <= bool_scalar
	def test_Comparison_Less_Equal_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 <= True
		temp_dc = self.dc_bool_0_4 <= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 <= bool_tensor_2
	def test_Comparison_Less_Equal_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 <= self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 <= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 <= float_scalar
	def test_Comparison_Less_Equal_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 <= 5.0
		temp_dc = self.dc_bool_0_4 <= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 <= float_tensor_2
	def test_Comparison_Less_Equal_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 <= self.np_float_5_9
		temp_dc = self.dc_bool_0_4 <= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 <= int_scalar
	def test_Comparison_Less_Equal_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 <= 5
		temp_dc = self.dc_bool_0_4 <= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 <= int_tensor_2
	def test_Comparison_Less_Equal_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 <= self.np_int_5_9
		temp_dc = self.dc_bool_0_4 <= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= bool_scalar
	def test_Comparison_Less_Equal_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 <= True
		temp_dc = self.dc_int_0_4 <= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= bool_tensor_2
	def test_Comparison_Less_Equal_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 <= self.np_bool_5_9
		temp_dc = self.dc_int_0_4 <= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= float_scalar
	def test_Comparison_Less_Equal_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 <= 5.0
		temp_dc = self.dc_int_0_4 <= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= float_tensor_2
	def test_Comparison_Less_Equal_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 <= self.np_float_5_9
		temp_dc = self.dc_int_0_4 <= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= int_scalar
	def test_Comparison_Less_Equal_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 <= 5
		temp_dc = self.dc_int_0_4 <= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 <= int_tensor_2
	def test_Comparison_Less_Equal_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 <= self.np_int_5_9
		temp_dc = self.dc_int_0_4 <= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= bool_scalar
	def test_Comparison_Less_Equal_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 <= True
		temp_dc = self.dc_float_0_4 <= True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= bool_tensor_2
	def test_Comparison_Less_Equal_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 <= self.np_bool_5_9
		temp_dc = self.dc_float_0_4 <= self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= float_scalar
	def test_Comparison_Less_Equal_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 <= 5.0
		temp_dc = self.dc_float_0_4 <= 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= float_tensor_2
	def test_Comparison_Less_Equal_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 <= self.np_float_5_9
		temp_dc = self.dc_float_0_4 <= self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= int_scalar
	def test_Comparison_Less_Equal_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 <= 5
		temp_dc = self.dc_float_0_4 <= 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 <= int_tensor_2
	def test_Comparison_Less_Equal_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 <= self.np_int_5_9
		temp_dc = self.dc_float_0_4 <= self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# Comparison Equal

	# bool_tensor_1 == bool_scalar
	def test_Comparison_Equal_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 == True
		temp_dc = self.dc_bool_0_4 == True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 == bool_tensor_2
	def test_Comparison_Equal_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 == self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 == self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 == float_scalar
	def test_Comparison_Equal_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 == 5.0
		temp_dc = self.dc_bool_0_4 == 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 == float_tensor_2
	def test_Comparison_Equal_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 == self.np_float_5_9
		temp_dc = self.dc_bool_0_4 == self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 == int_scalar
	def test_Comparison_Equal_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 == 5
		temp_dc = self.dc_bool_0_4 == 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 == int_tensor_2
	def test_Comparison_Equal_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 == self.np_int_5_9
		temp_dc = self.dc_bool_0_4 == self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == bool_scalar
	def test_Comparison_Equal_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 == True
		temp_dc = self.dc_int_0_4 == True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == bool_tensor_2
	def test_Comparison_Equal_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 == self.np_bool_5_9
		temp_dc = self.dc_int_0_4 == self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == float_scalar
	def test_Comparison_Equal_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 == 5.0
		temp_dc = self.dc_int_0_4 == 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == float_tensor_2
	def test_Comparison_Equal_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 == self.np_float_5_9
		temp_dc = self.dc_int_0_4 == self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == int_scalar
	def test_Comparison_Equal_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 == 5
		temp_dc = self.dc_int_0_4 == 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 == int_tensor_2
	def test_Comparison_Equal_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 == self.np_int_5_9
		temp_dc = self.dc_int_0_4 == self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == bool_scalar
	def test_Comparison_Equal_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 == True
		temp_dc = self.dc_float_0_4 == True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == bool_tensor_2
	def test_Comparison_Equal_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 == self.np_bool_5_9
		temp_dc = self.dc_float_0_4 == self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == float_scalar
	def test_Comparison_Equal_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 == 5.0
		temp_dc = self.dc_float_0_4 == 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == float_tensor_2
	def test_Comparison_Equal_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 == self.np_float_5_9
		temp_dc = self.dc_float_0_4 == self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == int_scalar
	def test_Comparison_Equal_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 == 5
		temp_dc = self.dc_float_0_4 == 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 == int_tensor_2
	def test_Comparison_Equal_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 == self.np_int_5_9
		temp_dc = self.dc_float_0_4 == self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# Comparison Not_Equal

	# bool_tensor_1 != bool_scalar
	def test_Comparison_Not_Equal_bool_tensor_1_bool_scalar (self):
		temp_np = self.np_bool_0_4 != True
		temp_dc = self.dc_bool_0_4 != True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 != bool_tensor_2
	def test_Comparison_Not_Equal_bool_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_bool_0_4 != self.np_bool_5_9
		temp_dc = self.dc_bool_0_4 != self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 != float_scalar
	def test_Comparison_Not_Equal_bool_tensor_1_float_scalar (self):
		temp_np = self.np_bool_0_4 != 5.0
		temp_dc = self.dc_bool_0_4 != 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 != float_tensor_2
	def test_Comparison_Not_Equal_bool_tensor_1_float_tensor_2 (self):
		temp_np = self.np_bool_0_4 != self.np_float_5_9
		temp_dc = self.dc_bool_0_4 != self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 != int_scalar
	def test_Comparison_Not_Equal_bool_tensor_1_int_scalar (self):
		temp_np = self.np_bool_0_4 != 5
		temp_dc = self.dc_bool_0_4 != 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# bool_tensor_1 != int_tensor_2
	def test_Comparison_Not_Equal_bool_tensor_1_int_tensor_2 (self):
		temp_np = self.np_bool_0_4 != self.np_int_5_9
		temp_dc = self.dc_bool_0_4 != self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != bool_scalar
	def test_Comparison_Not_Equal_int_tensor_1_bool_scalar (self):
		temp_np = self.np_int_0_4 != True
		temp_dc = self.dc_int_0_4 != True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != bool_tensor_2
	def test_Comparison_Not_Equal_int_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_int_0_4 != self.np_bool_5_9
		temp_dc = self.dc_int_0_4 != self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != float_scalar
	def test_Comparison_Not_Equal_int_tensor_1_float_scalar (self):
		temp_np = self.np_int_0_4 != 5.0
		temp_dc = self.dc_int_0_4 != 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != float_tensor_2
	def test_Comparison_Not_Equal_int_tensor_1_float_tensor_2 (self):
		temp_np = self.np_int_0_4 != self.np_float_5_9
		temp_dc = self.dc_int_0_4 != self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != int_scalar
	def test_Comparison_Not_Equal_int_tensor_1_int_scalar (self):
		temp_np = self.np_int_0_4 != 5
		temp_dc = self.dc_int_0_4 != 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# int_tensor_1 != int_tensor_2
	def test_Comparison_Not_Equal_int_tensor_1_int_tensor_2 (self):
		temp_np = self.np_int_0_4 != self.np_int_5_9
		temp_dc = self.dc_int_0_4 != self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != bool_scalar
	def test_Comparison_Not_Equal_float_tensor_1_bool_scalar (self):
		temp_np = self.np_float_0_4 != True
		temp_dc = self.dc_float_0_4 != True
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != bool_tensor_2
	def test_Comparison_Not_Equal_float_tensor_1_bool_tensor_2 (self):
		temp_np = self.np_float_0_4 != self.np_bool_5_9
		temp_dc = self.dc_float_0_4 != self.dc_bool_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != float_scalar
	def test_Comparison_Not_Equal_float_tensor_1_float_scalar (self):
		temp_np = self.np_float_0_4 != 5.0
		temp_dc = self.dc_float_0_4 != 5.0
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != float_tensor_2
	def test_Comparison_Not_Equal_float_tensor_1_float_tensor_2 (self):
		temp_np = self.np_float_0_4 != self.np_float_5_9
		temp_dc = self.dc_float_0_4 != self.dc_float_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != int_scalar
	def test_Comparison_Not_Equal_float_tensor_1_int_scalar (self):
		temp_np = self.np_float_0_4 != 5
		temp_dc = self.dc_float_0_4 != 5
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))

	# float_tensor_1 != int_tensor_2
	def test_Comparison_Not_Equal_float_tensor_1_int_tensor_2 (self):
		temp_np = self.np_float_0_4 != self.np_int_5_9
		temp_dc = self.dc_float_0_4 != self.dc_int_5_9
		np.testing.assert_array_equal(temp_np, np.array(temp_dc.data()))


	def tearDown(self):
		return "test finished"

if __name__ == '__main__':
	
	unittest.main()
	