def handler(event, context):
    print("Event:", event)
    print("Function name:", context.function_name)
    print("Function version:", context.function_version)
    print("Function ARN:", context.invoked_function_arn)
    print("AWS request id:", context.aws_request_id)
    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)
    return "hello world!"
