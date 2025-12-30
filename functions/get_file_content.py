import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # Construct and normalize target file path
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Validate that target_file is within working_directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if target is actually a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read file content with character limit
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            # Check if file was truncated
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)