from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    import os
    import sys
    import subprocess

    try:
        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # Construct and normalize target file path
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Validate that target_file is within working_directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if target is actually a file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        # Prepare command to run the Python file
        command = ["python3", target_file]
        if args:
            command.extend(args)
        
        # Run the Python file as a subprocess
        result = subprocess.run(command, capture_output=True, text=True, cwd=working_dir_abs)
        
        # Format output with STDOUT and STDERR labels
        output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        
        return output
    
    except Exception as e:
        return f"Error: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file relative to the working directory with optional command-line arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)