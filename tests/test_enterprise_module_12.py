import pytest
from modules.enterprise_module_12 import EnterpriseService12

def test_enterprise_service_12():
    service = EnterpriseService12()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
