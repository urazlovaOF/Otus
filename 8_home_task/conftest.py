import pytest

@pytest.fixture()
def function_hm_fixture(request):
    print(f"\n {request.scope} fixture starts working")
    yield
    print("function_fixture is finalized")

@pytest.fixture(scope="module")
def module_hm_fixture(request):
    print(f"\n {request.scope} fixture starts working")
    def fin():
        print("module_fixture is finalized")
    request.addfinalizer(fin)

@pytest.fixture(scope="session", params=["Start"])
def session_hm_fixture(request):
    print(f"\n {request.scope} fixture starts working")
    return request.param







