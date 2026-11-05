import pytest
from modules.enterprise_module_26 import EnterpriseService26

def test_enterprise_service_26():
    service = EnterpriseService26()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
