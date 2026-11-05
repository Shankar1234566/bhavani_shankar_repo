import pytest
from modules.enterprise_module_3 import EnterpriseService3

def test_enterprise_service_3():
    service = EnterpriseService3()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
