    # Use the official AWS base image for Python 3.9 Lambda functions
    FROM public.ecr.aws/lambda/python:3.9-arm64

    # Copy the requirements file into the container
    COPY requirements.txt .

    # Install the Python dependencies
    RUN pip install -r requirements.txt

    # Copy the function code into the container
    COPY lambda_function.py .

    # Set the command that Lambda will run when the container starts
    CMD [ "lambda_function.lambda_handler" ]
    