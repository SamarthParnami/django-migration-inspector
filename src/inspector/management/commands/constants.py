DEFAULT_DB_ALIAS = 'default'



CIRCULAR_DEPENDENCY_ERROR_MESSAGE = '''Circular dependecy between the migrations detected.
Suspected migration discrepancies: {exception}'''

NODE_NOT_FOUND_ERROR_MESSAGE = "{exception}"

MULTIPLE_LEAF_NODE_ERROR_MESSAGE = "Conflicting migration detected; multiple leaf nodes in the"\
                               " migration graph. For the following apps:\n{detail}"
