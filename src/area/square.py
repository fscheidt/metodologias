def square_area(lado):
    if isinstance(lado, int) or isinstance(lado,float):
        return lado * lado
    raise ValueError("invalid value of lado")
