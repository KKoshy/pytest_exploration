import pytest
import random


def pytest_addoption(parser):
    parser.addoption("--poles", action="store", type=int, help="Number of poles in induction motor;"
                                                               "even number greater than 2*;"
                                                               "by default 4")


@pytest.fixture(scope='session')
def poles(pytestconfig):
    return pytestconfig.getoption("poles")


@pytest.fixture(scope='session')
def stage():
    return random.choice(['acceleration', 'braking'])


@pytest.fixture(scope='session')
def front_trq():
    return random.randint(300, 450)


@pytest.fixture(scope='session')
def rear_trq():
    return random.randint(250, 550)

# conftest.py
def pytest_generate_tests(metafunc):
    variants = ['40', '60', '60D', '70', '70D', '85', '85D', 'P85+', 'P85D', '90D', 'P90D', '100D', 'P100D']
    if "variant" in metafunc.fixturenames:
        metafunc.parametrize("variant", variants, scope="session")
