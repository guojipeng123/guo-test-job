# -*- coding: utf-8 -*-


def hydrate_node_data(node):
    """
    替换当前节点的 data 中的变量
    :param node:
    :return:
    """
    data = node.data
    hydrated = hydrate_data(data.get_inputs())
    data.get_inputs().update(hydrated)


def hydrate_data(data):
    hydrated = {}
    for k, v in data.items():
        from pipeline.core.data import var
        if issubclass(v.__class__, var.Variable):
            hydrated[k] = v.get()
        else:
            hydrated[k] = v
    return hydrated


def hydrate_subprocess_context(subprocess_act):
    # hydrate data
    hydrate_node_data(subprocess_act)

    # context injection
    data = subprocess_act.pipeline.data
    context = subprocess_act.pipeline.context()
    for k, v in data.get_inputs().items():
        context.set_global_var(k, v)

    hydrated = hydrate_data(context.variables)
    context.update_global_var(hydrated)
