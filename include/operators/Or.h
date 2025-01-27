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
#include "operators/baseOperator.h"
#include <string>

using namespace Eigen;

namespace dnnc {
template <typename To, typename Ti> class Or : public baseOperator<To, Ti, Ti> {
  //  Or attributes
public:
  Or(std::string name = "opOr") : baseOperator<To, Ti, Ti>(opOr, name) {}

  tensor<To> compute(tensor<Ti> a, tensor<Ti> b) {

    std::vector<DIMENSION> resultShape = binaryBroadcastReShape(a, b);
    tensor<bool> result(resultShape);

    // This check is for ONNX standard
    // if (!(this->template type_check<bool>(typeid(Ti))))
    //   throw std::invalid_argument("Constrain input tensors to bool types.");

    if (a.shape() != b.shape())
      throw std::invalid_argument(
          "tensor dimenions not appropriate for Or operator.");

    DNNC_EIGEN_ARRAY_MAP(eigenVectorA, Ti, a);
    DNNC_EIGEN_ARRAY_MAP(eigenVectorB, Ti, b);

    DNNC_EIGEN_VECTOR_CTOR(bool) eResult;

    eResult.array() = eigenVectorA.template cast<bool>().array() ||
                      eigenVectorB.template cast<bool>().array();
    result.load(eResult.data());

    return result;
  }
};
} // namespace dnnc
