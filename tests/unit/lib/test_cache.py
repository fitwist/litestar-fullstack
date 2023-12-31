import pytest
from litestar.config.response_cache import default_cache_key_builder
from litestar.testing import RequestFactory

from app.lib import cache, settings

pytestmark = pytest.mark.anyio


def test_cache_key_builder(monkeypatch: "pytest.MonkeyPatch") -> None:
    monkeypatch.setattr(settings.AppSettings, "slug", "the-slug")
    request = RequestFactory().get("/test")
    default_cache_key = default_cache_key_builder(request)
    assert cache.cache_key_builder(request) == f"the-slug:{default_cache_key}"
