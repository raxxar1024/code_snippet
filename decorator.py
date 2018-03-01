import logging


def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is runnging" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def use_logging_2(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is runnging" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@use_logging
def bar():
    print "i am bar"


@use_logging_2(level="warn")
def bar_2(name='foo'):
    print("i am %s" % name)


bar()
bar_2()
