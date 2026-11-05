import pytest
from modules.enterprise_module_30 import EnterpriseService30

def test_enterprise_service_30():
    service = EnterpriseService30()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
