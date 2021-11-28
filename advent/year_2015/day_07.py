"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

To begin, get your puzzle input.

Answer: 
 

You can also [Share] this puzzle.
"""

from advent.tools import *

INT_MAX = 65535
ANSWERS = [None, 956]

def _solve(lines, src):
    def eval_(*tokens):
        if tokens in memo:
            return memo[tokens]
        result = None
        match tokens:
            case [a, 'AND', b]:
                result = eval_(a) & eval_(b)
            case [a, 'OR', b]:
                result = eval_(a) | eval_(b)
            case ['NOT', a]:
                result = INT_MAX - eval_(a)
            case [a, 'LSHIFT', b]:
                result = eval_(a) << eval_(b)
            case [a, 'RSHIFT', b]:
                result = eval_(a) >> eval_(b)
            case [a]:
                if a.isnumeric():
                    result = int(a)
                else:
                    result = eval_(*graph[a])
        memo[tokens] = result
        return result

    graph = cl.defaultdict(list)
    memo = cl.defaultdict(int)

    for expr, wire in lines:
        graph[wire] = expr.split(" ")

    return eval_(src)


def _pt1(lines):
    return _solve(lines, "a")


def _pt2(lines):
    pass


TEST = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


def main():
    return afs.input_lines(
        tests=[TEST], parts=[_pt1], run_input=True, transform_line=_transform_line
    )


def _transform_line(line):
    return line.split(" -> ")
