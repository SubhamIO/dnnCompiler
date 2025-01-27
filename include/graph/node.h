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

#include "core/tensor.h"
#include "operators/baseOperator.h"
#include <any>
#include <vector>

namespace dnnc {
typedef std::tuple<DNNC_DataType, DNNC_DataType, DNNC_DataType> OP_DTYPES;

/*! Graph node
 * */
/*! Compute Graph Node.
 *       It represents basic computational unit (like adder/multiplier)
 * available in underlying hardware.
 * */
class node {
protected:
  // TODO: add node attributes like level, graph-input, graph-output,
  //       placeholder, const, variable etc.
  std::string _name = "";
  baseOperator<float, float, float> *_op = 0x0; /*!< operator aka symbol */
  std::vector<tensor<std::any>>
      _ins; /*!< inputs, i.e. tensors coming to   this node */
  std::vector<tensor<std::any>>
      _outs; /*!< outputs, i.e tensors going  from this node */
public:
  node(baseOperator<float, float, float> *op) : _op(op) { assert(op); }
  ~node() { delete _op; }
  /*
  template <typename DTYPE> baseOperator<DTYPE> op() {
    return std::any_cast<DTYPE>(_op);
  }
  inline baseOperator<T> op() { return _op; }
  inline bool hasInput(tensor<Ti> &in) {
    return std::find(_ins.begin(), _ins.end(), in);
  }
  inline bool hasOutput(tensor<To> &out) {
    return std::find(_outs.begin(), _outs.end(), out);
  }
  bool addInput(tensor<Ti> &in) {
    if (hasInput(in))
      return false;
    _ins.push_back(in);
    return true;
  }
  bool addOutput(tensor<To> &out) {
    if (hasOutput(out))
      return false;
    _outs.push_back(out);
    return true;
  }
};

template <class T, class Ti, class To> struct nodeCmp {
  bool operator()(const node<T, Ti, To> &lhs,
                  const node<T, Ti, To> &rhs) {
      //TODO: enhance this to compare in/out edges
    return opCmp<T>()(*lhs.op(), *rhs.op());
  }
};

template <class T, class Tf, class Tt> class edge {
protected:
  const node<T, std::any, Tf> _from;
  const node<T, Tt, std::any> _to;

public:
  edge(const node<T, std::any, Tf> f, const node<T, Tt, std::any> t)
      : _from(f), _to(t) {}
  const node<T, std::any, Tf> from() { return _from; }
  const node<T, Tt, std::any> to()   { return _to; }
};

template <class T, class Tf, class Tt> struct edgeCmp {
  bool operator()(const edge<T, Tf, Tt> &lhs,
                  const edge<T, Tf, Tt> &rhs) {
      return nodeCmp<T, std::any, Tf>()(lhs.from(), rhs.from()) &&
             nodeCmp<T, Tt, std::any>()(lhs.to(), rhs.to()) ;
  }
  */
};

} // namespace dnnc
