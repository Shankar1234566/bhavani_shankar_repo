import pytest
from modules.enterprise_module_64 import EnterpriseService64

def test_enterprise_service_64():
    service = EnterpriseService64()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
