"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    list_of_wagons = []
    for arg in args:
        list_of_wagons.append(arg)
    return list_of_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_two = each_wagons_id[:2]
    first = each_wagons_id[2]
    rest_wagons_id = each_wagons_id[3:]
    fixed_wagons = [first] + missing_wagons + rest_wagons_id + first_two
    return fixed_wagons


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = []
    for kwarg in kwargs.values():
        stops.append(kwarg)
    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    for key in more_route_information:
        route[key] = more_route_information[key]
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    transposed_tuples = list(zip(*wagons_rows))
    transposed = [list(sublist) for sublist in transposed_tuples]
    return transposed
