import pytest
from modules.enterprise_module_66 import EnterpriseService66

def test_enterprise_service_66():
    service = EnterpriseService66()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
