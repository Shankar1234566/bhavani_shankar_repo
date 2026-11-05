import pytest
from modules.enterprise_module_71 import EnterpriseService71

def test_enterprise_service_71():
    service = EnterpriseService71()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
