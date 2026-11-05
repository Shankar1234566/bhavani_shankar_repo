import pytest
from modules.enterprise_module_20 import EnterpriseService20

def test_enterprise_service_20():
    service = EnterpriseService20()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
