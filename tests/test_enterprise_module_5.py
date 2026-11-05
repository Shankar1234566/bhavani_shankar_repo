import pytest
from modules.enterprise_module_5 import EnterpriseService5

def test_enterprise_service_5():
    service = EnterpriseService5()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
