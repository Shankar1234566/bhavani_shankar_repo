import pytest
from modules.enterprise_module_25 import EnterpriseService25

def test_enterprise_service_25():
    service = EnterpriseService25()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
