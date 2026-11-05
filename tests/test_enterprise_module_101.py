import pytest
from modules.enterprise_module_101 import EnterpriseService101

def test_enterprise_service_101():
    service = EnterpriseService101()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
