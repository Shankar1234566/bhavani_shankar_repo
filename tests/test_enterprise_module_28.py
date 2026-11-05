import pytest
from modules.enterprise_module_28 import EnterpriseService28

def test_enterprise_service_28():
    service = EnterpriseService28()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
