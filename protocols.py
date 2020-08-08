from operator import add
from functools import partial, reduce

#
# Auxillian Functions
#=============================================================================

in_middle = partial(
        lambda element_a, middle, element_b: element_a + middle + element_b
        )

def first_item(list_a):
    return list(map(lambda l_a: l_a[0], list_a))

def second_item(list_a):
    return list(map(lambda l_a: l_a[1], list_a))

def front_mid_back(region, locale):
    return  [
                [locale, region[0], region[1]],
                [region[0], locale, region[1]],
                [region[0], region[1], locale]
            ]

#
# Work with Lists
#=============================================================================

def to_list(valor1, valor2):
    return [valor1, valor2]

def simplify_list(list_a):
    return reduce(add, list_a)

def apply_to_2list(list_a, list_b, func):
    return list(map(lambda l_a: 
                list(map(lambda l_b: func(l_a, l_b), 
                list_b)), 
            list_a))

def apply_to_3list(list_a, list_b, list_c, func):
    return list(map(lambda l_a: 
                list(map(lambda l_b: 
                    list(map(lambda l_c: func(l_a, l_b, l_c), 
                    list_c)), 
                list_b)), 
            list_a))

def apply_reverse_to_2list(list_a, list_b, func):
    return list(map(lambda l_a: 
                list(map(lambda l_b: func(l_b, l_a), 
                list_b)), 
            list_a))

def apply_reverse_to_3list(list_a, list_b, list_c, func):
    return list(map(lambda l_a: 
                list(map(lambda l_b: 
                    list(map(lambda l_c: func(l_c, l_b, l_a), 
                    list_c)), 
                list_b)), 
            list_a))

def concatenate_2list(list_a, list_b):
    return reduce(add, list(zip(list_a, list_b)))

def concatenate_list_sequence_2item(list_a):
    return first_item(list_a) + second_item(list_a)

#
# Protocols
#=============================================================================

def combine(position_1, position_2):
    return simplify_list(apply_to_2list(position_1, position_2, add))

def wrap(core, hedge):
    return simplify_list(
                apply_to_2list(core, hedge, lambda c, h: h[0] + c + h[1])
                )

def cartesian_product(list_a, list_b):
    return concatenate_2list(
            simplify_list(apply_to_2list(list_a, list_b, add)), 
            simplify_list(apply_reverse_to_2list(list_a, list_b, add))
            )

def intersection(list_a, list_b, inter, method=in_middle):
    return concatenate_list_sequence_2item(concatenate_2list(
            simplify_list(apply_to_3list(list_a, inter, list_b, method)),
            simplify_list(apply_reverse_to_3list(list_a, inter, list_b, method))
            ))

def axis_Z(list_a, list_b, list_c):
    return list(map(lambda l: ''.join(l),
        simplify_list(simplify_list(apply_to_2list(concatenate_2list(
                simplify_list(apply_to_2list(list_a, list_b, to_list)),
                simplify_list(apply_reverse_to_2list(list_a, list_b, to_list))
                ), list_c, front_mid_back)))))

