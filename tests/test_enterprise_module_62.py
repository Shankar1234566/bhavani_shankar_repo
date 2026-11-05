import pytest
from modules.enterprise_module_62 import EnterpriseService62

def test_enterprise_service_62():
    service = EnterpriseService62()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
