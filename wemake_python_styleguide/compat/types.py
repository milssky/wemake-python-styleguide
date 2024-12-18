import ast
from typing import TypeAlias, Union

from wemake_python_styleguide.compat.nodes import TryStar
from wemake_python_styleguide.compat.nodes import TypeAlias as TypeAliasNode

#: When used with `visit_Try` and visit_TryStar`.
AnyTry: TypeAlias = Union[ast.Try, TryStar]

#: Used when named matches are needed.
NamedMatch: TypeAlias = Union[ast.MatchAs, ast.MatchStar]

#: These nodes have `.type_params` on python3.12+:
NodeWithTypeParams: TypeAlias = Union[
    ast.ClassDef,
    ast.FunctionDef,
    ast.AsyncFunctionDef,
    TypeAliasNode,
]
