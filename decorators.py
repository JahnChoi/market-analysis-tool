import exceptions
import time
import os


def timer(func):
    """
    Decorator function to time a function's execution without keyword arguments.
    """
    def time_function(*args):
        start = time.time()
        function_return = func(args)
        end = time.time()

        elapsed_time = end - start
        print('\'{0}\' function took {1}s to execute.'.format(func.__name__, elapsed_time))

        return function_return
    return time_function


def verify_environment(func):
    """
    Decorator function to verify the appropriate IEX Cloud environment variables.
    """
    def validate_environment():
        variables_to_check = ['IEX_API_VERSION', 'IEX_TOKEN']
        for var in variables_to_check:
            if var not in os.environ:
                raise exceptions.EnvironmentNotConfiguredException('Environment does not have the appropriate environment variable set: \'{0}\''.format(var))
        return func()
    return validate_environment