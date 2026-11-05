import pytest
from modules.enterprise_module_61 import EnterpriseService61

def test_enterprise_service_61():
    service = EnterpriseService61()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
