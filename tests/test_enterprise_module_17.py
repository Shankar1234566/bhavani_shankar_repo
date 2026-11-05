import pytest
from modules.enterprise_module_17 import EnterpriseService17

def test_enterprise_service_17():
    service = EnterpriseService17()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
