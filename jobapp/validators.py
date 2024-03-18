from django.core.exceptions import ValidationError

def validate_file_size(value):
    limit = 4 * 1024 * 1024  # limit to 4MB
    if value.size > limit:
        raise ValidationError("The maximum file size that can be uploaded is 4MB.")