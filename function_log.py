import logging
import time
import pandas as pd

logging.basicConfig(level=logging.INFO)


def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info(f"start: {func.__name__}.")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time: {elapsed_time}")
        logging.info(f"End: {func.__name__}")
        return result

    return wrapper


def tables_load_info(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, pd.DataFrame):
            logging.info(f"Shape: {func.__name__} : {result.shape}")
        elif isinstance(result, tuple) and all(
            isinstance(df, pd.DataFrame) for df in result
        ):
            for i, df in enumerate(result):
                logging.info(f"Shape {i + 1}: {func.__name__} : {df.shape}")
        else:
            logging.warning(f"Undefined result type: {type(result)}")

        return result

    return wrapper
