import pytest
from modules.enterprise_module_65 import EnterpriseService65

def test_enterprise_service_65():
    service = EnterpriseService65()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
