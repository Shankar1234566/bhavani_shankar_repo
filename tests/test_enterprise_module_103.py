import pytest
from modules.enterprise_module_103 import EnterpriseService103

def test_enterprise_service_103():
    service = EnterpriseService103()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
