import builtins

NORMAL_FONT_SIZE = 16

def builtin_children(cls):
    return [s for s in cls.__subclasses__() if s.__module__ == "builtins"]

def format_name(name, highlight_exceptions):
    if name in highlight_exceptions:
        #print(f'{highlight_exceptions=}')
        values = highlight_exceptions[name]
        font_size = ''
        font_color = ''
        if len(values) > 0: font_size = f'POINT-SIZE="{values[0]}"'
        if len(values) > 1: font_color = f'COLOR="{values[1]}"'
        return f'<FONT {font_color} {font_size}><B>{name}</B></FONT>'
    return name

def format_group_label(leaves, highlight_exceptions):
    lines = [format_name(c.__name__, highlight_exceptions) for c in leaves]
    return "<" + "<BR/>".join(lines) + ">"

def add_exception_tree(dot, drop_exceptions, highlight_exceptions, cls=BaseException):
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
        group_label = format_group_label(leaves, highlight_exceptions)
        group_node = f"_leaves_of_{cls.__name__}"
        dot.append(f'    "{group_node}" [label={group_label}];')
        dot.append(f'    "{cls.__name__}" -> "{group_node}";')
    # Non-leaf children get their own node and recurse
    for child in non_leaves:
        if child.__name__ in highlight_exceptions:
            label = format_name(child.__name__, highlight_exceptions)
            dot.append(f'    "{child.__name__}" [label=<{label}>];')
        dot.append(f'    "{cls.__name__}" -> "{child.__name__}";')
        add_exception_tree(dot, drop_exceptions, highlight_exceptions, child)

def create_exception_graph(drop_exceptions=None, highlight_exceptions=None):
    if drop_exceptions is None:
        drop_exceptions = {}
    if highlight_exceptions is None:
        highlight_exceptions = {}
    dot = [
        "digraph ExceptionHierarchy {",
        "    rankdir=TB;",
        "    nodesep=0.1;",
        "    ranksep=0.2;",
        f"    node [shape=box, fontsize={NORMAL_FONT_SIZE}];",
        "    edge [dir=back, arrowtail=empty];",
    ]
    add_exception_tree(dot, drop_exceptions, highlight_exceptions)
    dot.append("}")
    dot_string = "\n".join(dot)
    return dot_string

def render_graph(dot_string, output_filename):
    import subprocess
    subprocess.run(["dot", "-Tpng", "-o", output_filename], input=dot_string, text=True, check=True)

drop_exceptions = {'Warning', 'BaseExceptionGroup'}
highlight_exceptions = {'ZeroDivisionError':(18,), 'AssertionError':(18,), 'NameError':(18,),
                        'IndexError':(24,'red'), 'LookupError':(24,)}
dot_string = create_exception_graph(drop_exceptions, highlight_exceptions)
render_graph(dot_string, "exception_tree.png")
