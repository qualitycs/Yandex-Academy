def simple_map(transformation, values):
    result = []
    for value in values:
        transformed_value = transformation(value)
        result.append(transformed_value)
    return result
