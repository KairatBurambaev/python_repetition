def create_argument_dict(**kwargs):
    argument_dict = {}
    
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, tuple)):
            argument_dict[key] = value
        else:
            argument_dict[str(key)] = value
    
    return argument_dict

arguments = create_argument_dict(a=1, b=2, c='abc')
print(arguments)