// Copyright 2018 The AITS DNNC Authors.All Rights Reserved.
//
// Licensed to the Apache Software Foundation(ASF) under one
// or more contributor license agreements.See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.See the License for the
// specific language governing permissionsand limitations
// under the License.
//
// This file is part of AITS DNN compiler maintained at
// https://github.com/ai-techsystems/dnnCompiler
//

#pragma once
#include "core/broadcast.h"
#include "operators/baseOperator.h"
#include <string>

using namespace Eigen;

namespace dnnc {

/*! This does element wise binary truedivision operation of two given N D
   tensors of same size. This operator supports multidirectional (i.e.,
   Numpy-style) broadcasting.*/

template <typename To, typename Ti>
class TrueDiv : public baseOperator<To, Ti, Ti> {
  template <typename Scalar>
  inline DNNC_EIGEN_VECTOR_CTOR(float)
      eigenArrayDiv(Map<DNNC_EIGEN_VECTOR_CTOR(Scalar)> &a,
                    Map<DNNC_EIGEN_VECTOR_CTOR(Scalar)> &b) {
    return a.template cast<float>().array() / b.template cast<float>().array();
  }
  // Eigen does not support numeric operator for bool
  // So specialiazation is needed to work around that limitation.
  // Bug Ref: http://eigen.tuxfamily.org/bz/show_bug.cgi?id=426
  inline DNNC_EIGEN_VECTOR_CTOR(float)
      eigenArrayDiv(Map<DNNC_EIGEN_VECTOR_CTOR(bool)> &a,
                    Map<DNNC_EIGEN_VECTOR_CTOR(bool)> &b) {
    throw std::invalid_argument("Division not valid for bool tensor(s)");
    return a.template cast<float>().array() / b.template cast<float>().array();
  }

public:
  TrueDiv(std::string name = "opTrueDiv")
      : baseOperator<To, Ti, Ti>(opTrueDiv, name) {}

  tensor<To> compute(tensor<Ti> a /*!< : N D tensor input*/,
                     tensor<Ti> b /*!< : N D tensor input*/) {

    std::vector<DIMENSION> resultShape = binaryBroadcastReShape(a, b);
    tensor<float> result(resultShape);

    if (!(this->template type_check<float, double, int>(typeid(Ti))))
      throw std::invalid_argument(
          "Constrain input and output types to numeric tensors.");

    if (a.shape() != b.shape())
      throw std::invalid_argument(
          "tensor dimenions not appropriate for TrueDiv operator.");

    DNNC_EIGEN_ARRAY_MAP(eigenVectorA, Ti, a);
    DNNC_EIGEN_ARRAY_MAP(eigenVectorB, Ti, b);

    DNNC_EIGEN_VECTOR_CTOR(float) eResult;

    eResult.array() = eigenArrayDiv(eigenVectorA, eigenVectorB);

    result.load(eResult.data());

    return result;
  }
  /*!<
  \return The output tensor of type float and the same shape as input.
  */
};
} // namespace dnnc
