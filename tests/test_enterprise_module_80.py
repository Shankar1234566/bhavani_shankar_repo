import pytest
from modules.enterprise_module_80 import EnterpriseService80

def test_enterprise_service_80():
    service = EnterpriseService80()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
