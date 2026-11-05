import pytest
from modules.enterprise_module_36 import EnterpriseService36

def test_enterprise_service_36():
    service = EnterpriseService36()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
