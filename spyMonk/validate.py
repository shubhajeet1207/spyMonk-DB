from .errors import ValidationError


# validate whether variable is the same type as variable_type

def validate(variable, variable_type, error_message):
    if not isinstance(variable, variable_type):
        raise ValidationError(error_message)
