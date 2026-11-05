import pytest
from modules.enterprise_module_21 import EnterpriseService21

def test_enterprise_service_21():
    service = EnterpriseService21()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
