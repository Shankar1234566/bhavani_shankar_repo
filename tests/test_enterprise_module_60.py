import pytest
from modules.enterprise_module_60 import EnterpriseService60

def test_enterprise_service_60():
    service = EnterpriseService60()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
