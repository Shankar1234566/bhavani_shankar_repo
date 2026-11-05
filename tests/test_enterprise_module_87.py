import pytest
from modules.enterprise_module_87 import EnterpriseService87

def test_enterprise_service_87():
    service = EnterpriseService87()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
