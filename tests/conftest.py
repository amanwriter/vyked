from vyked.registry import Registry, Repository
import pytest
from .factories import ServiceFactory, EndpointFactory


@pytest.fixture
def registry():
    r = Registry(ip='192.168.1.1', port=4001, repository=Repository())
    return r


@pytest.fixture
def service(*args, **kwargs):
    return ServiceFactory(*args, **kwargs)


# @pytest.fixture
# def services():
#     """
#     returns a dict of services where

#     a1, a2 are independent
#     b1, b2 depend on a1 and a2 respectively
#     c1 depends on both a1 and b1
#     c2 and c3 depend on both a2 and b2

#     more services to be added for different testcases
#     """
#     a1 = ServiceFactory()
#     a2 = ServiceFactory(service=a1['service'], version='1.0.1')

#     b1 = ServiceFactory(dependencies=dependencies_from_services(a1))
#     b2 = ServiceFactory(
# service=b1['service'], version='1.0.1',
# dependencies=dependencies_from_services(a2))

#     c1 = ServiceFactory(dependencies=dependencies_from_services(a1, b1))
#     c2 = ServiceFactory(service=c1[
#                         'service'], version='1.0.1', dependencies=dependencies_from_services(a2, b2))

#     c3 = ServiceFactory(service=c1[
#                         'service'], version='1.0.1', dependencies=dependencies_from_services(a2, b2))

#     return locals()


@pytest.fixture
def dependencies_from_services(*services):
    return [{'service': service['service'], 'version': service['version']} for service in services]


def endpoints_for_service(service, n):
    endpoints = []
    for _ in range(n):
        endpoint = EndpointFactory()
        endpoint['service'] = service['service']
        endpoint['version'] = service['version']
        endpoints.append(endpoint)
    return endpoints


@pytest.fixture
def service_a1():
    return ServiceFactory()


@pytest.fixture
def service_a2(service_a1):
    return ServiceFactory(service=service_a1['service'], version='1.0.1')


@pytest.fixture
def service_b1(service_a1):
    return ServiceFactory(dependencies=dependencies_from_services(service_a1))


@pytest.fixture
def service_b2(service_b1):
    return ServiceFactory(
        service=service_b1['service'], version='1.0.1', dependencies=dependencies_from_services(service_b1))


@pytest.fixture
def service_c1(service_a1, service_b1):
    return ServiceFactory(dependencies=dependencies_from_services(service_a1, service_b1))


@pytest.fixture
def service_c2(service_a2, service_b2, service_c1):
    return ServiceFactory(service=service_c1['service'], version='1.0.1',
                          dependencies=dependencies_from_services(service_a2, service_b2))


@pytest.fixture
def service_c3(service_a2, service_b2, service_c2):
    return ServiceFactory(service=service_c2['service'], version='1.0.1',
                          dependencies=dependencies_from_services(service_a2, service_b2))


@pytest.fixture
def service_d1(service_a1):
    return ServiceFactory(events=endpoints_for_service(service_a1, 1))
