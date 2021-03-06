"""
 Copyright (C) 2018-2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.common.partial_infer.elemental import copy_shape_infer
from mo.graph.graph import Graph
from mo.ops.op import Op


class AttributedClamp(Op):
    op = 'AttributedClamp'

    def __init__(self, graph: Graph, attrs: dict):
        super().__init__(graph, {
            'type': 'Clamp',
            'op': self.op,
            'version': 'opset1',
            'infer': copy_shape_infer,
            'in_ports_count': 1,
            'out_ports_count': 1,
        }, attrs)

    def supported_attrs(self):
        return [
            'max',
            'min'
        ]


class Clamp(Op):
    op = 'Clamp'

    def __init__(self, graph: Graph, attrs: dict):
        super().__init__(graph, {
            'type': None,
            'op': self.op,
            'infer': copy_shape_infer,
            'in_ports_count': 3,
            'out_ports_count': 1,
        }, attrs)
