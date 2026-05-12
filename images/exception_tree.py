import builtins

def builtin_children(cls):
    return [s for s in cls.__subclasses__() if s.__module__ == "builtins"]

def add_exception_tree(dot, cls=BaseException, drop_exceptions=None):
    if drop_exceptions is None:
        drop_exceptions = []
    children = sorted(
        [c for c in builtin_children(cls) if c.__name__ not in drop_exceptions],
        key=lambda c: c.__name__
    )
    if not children:
        return
    leaves = [c for c in children if not builtin_children(c) or
              all(gc.__name__ in drop_exceptions for gc in builtin_children(c))]
    non_leaves = [c for c in children if c not in leaves]
    # Group leaf children into a single box (skip if empty after filtering)
    if leaves:
        group_label = "\\n".join(c.__name__ for c in leaves)
        group_node = f"_leaves_of_{cls.__name__}"
        dot.append(f'    "{group_node}" [label="{group_label}"];')
        dot.append(f'    "{cls.__name__}" -> "{group_node}";')
    # Non-leaf children get their own node and recurse
    for child in non_leaves:
        dot.append(f'    "{cls.__name__}" -> "{child.__name__}";')
        add_exception_tree(dot, child, drop_exceptions)

def create_exception_graph(drop_exceptions=None):
    if drop_exceptions is None:
        drop_exceptions = []
    dot = [
        "digraph ExceptionHierarchy {",
        "    rankdir=TB;",
        "    nodesep=0.1;",
        "    ranksep=0.2;",
        "    node [shape=box, fontsize=16];",
        "    edge [dir=back, arrowtail=empty];",
    ]
    add_exception_tree(dot, drop_exceptions=drop_exceptions)
    dot.append("}")
    dot_string = "\n".join(dot)
    return dot_string

def render_graph(dot_string, output_filename):
    import subprocess
    subprocess.run(["dot", "-Tpng", "-o", output_filename], input=dot_string, text=True, check=True)

drop_exceptions = ['Warning', 'BaseExceptionGroup']
dot_string = create_exception_graph(drop_exceptions)
render_graph(dot_string, "exception_tree.png")
