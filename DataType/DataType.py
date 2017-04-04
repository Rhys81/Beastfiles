def data_type(x):
    while True:
        try:
            if isinstance(x, str):
                return str(x.__len__())

                if isinstance(x, bool):
                    return ("the boolean")

                if isinstance(x, int):
                    if x<100:
                        return "less than ", (100)
                    else:
                        return "more than ", (100)

                if isinstance(x, list):
                    return x[3]

                if isinstance(x, None):
                    return "no value"
        except():
            return "Invalid"





