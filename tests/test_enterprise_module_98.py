import pytest
from modules.enterprise_module_98 import EnterpriseService98

def test_enterprise_service_98():
    service = EnterpriseService98()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
