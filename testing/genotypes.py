from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'conv_7x1_1x7',
    'sep_conv_7x7',
     'dil_conv_5x5'
]



NASNet = Genotype(
  normal = [
     ('sep_conv_5x5', 1),
    ('sep_conv_3x3', 0),
     ('sep_conv_5x5', 0),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 1),
     ('skip_connect', 0),
    ('avg_pool_3x3', 0),
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
     ('skip_connect', 1),
  ],
  normal_concat = [2, 3, 4, 5, 6],
  reduce = [
     ('sep_conv_5x5', 1),
     ('sep_conv_7x7', 0),
    ('max_pool_3x3', 1),
     ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
     ('sep_conv_5x5', 0),
     ('skip_connect', 3),
    ('avg_pool_3x3', 2),
    ('sep_conv_3x3', 2),
    ('max_pool_3x3', 1),
  ],
  reduce_concat = [4, 5, 6],
)
    
AmoebaNet = Genotype(
  normal = [
    ('avg_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 2),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 3),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 1),
    ],
  normal_concat = [4, 5, 6],
  reduce = [
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('max_pool_3x3', 0),
    ('sep_conv_7x7', 2),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('max_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('conv_7x1_1x7', 0),
    ('sep_conv_3x3', 5),
  ],
  reduce_concat = [3, 4, 6]
)



acc_final=Genotype(normal=[('avg_pool_3x3', 1), ('conv_7x1_1x7', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 2), ('avg_pool_3x3', 1), ('dil_conv_3x3', 2), ('sep_conv_7x7', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_7x7', 1), ('conv_7x1_1x7', 0), ('sep_conv_7x7', 2), ('conv_7x1_1x7', 0), ('sep_conv_7x7', 3), ('sep_conv_3x3', 2), ('sep_conv_7x7', 4), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
don_final=Genotype(normal=[('dil_conv_5x5', 1), ('dil_conv_5x5', 0), ('conv_7x1_1x7', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('conv_7x1_1x7', 1), ('max_pool_3x3', 0), ('max_pool_3x3', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_7x7', 1), ('avg_pool_3x3', 0), ('sep_conv_7x7', 2), ('dil_conv_5x5', 1), ('dil_conv_3x3', 3), ('avg_pool_3x3', 1), ('sep_conv_7x7', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
