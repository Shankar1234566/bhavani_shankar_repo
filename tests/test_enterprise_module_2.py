import pytest
from modules.enterprise_module_2 import EnterpriseService2

def test_enterprise_service_2():
    service = EnterpriseService2()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
