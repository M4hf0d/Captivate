from django.core.exceptions import ValidationError


from django.core.files.uploadedfile import UploadedFile
from django.db import models
from cloudinary.models import CloudinaryField

# For testing model validation
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb

def file_validation(file):
    if not file:
        raise ValidationError("No file selected.")

    # For regular upload, we get UploadedFile instance, so we can validate it.
    # When using direct upload from the browser, here we get an instance of the CloudinaryResource
    # and file is already uploaded to Cloudinary.
    # Still can perform all kinds on validations and maybe delete file, approve moderation, perform analysis, etc.
    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("File shouldn't be larger than 10MB.")
