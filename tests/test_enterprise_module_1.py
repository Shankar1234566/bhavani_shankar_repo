import pytest
from modules.enterprise_module_1 import EnterpriseService1

def test_enterprise_service_1():
    service = EnterpriseService1()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
