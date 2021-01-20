import pytest


@pytest.mark.unit
class TestConvenienceMethods:

    @pytest.mark.happy
    def test_camel(self):
        from stringbender import camel
        assert camel("Abc DEF") == "abcDef"

    @pytest.mark.happy
    def test_kebob(self):
        from stringbender import kebob
        assert kebob("ABC DEF") == "abc-def"

    @pytest.mark.happy
    def test_pascal(self):
        from stringbender import pascal
        assert pascal("ABC DEF GHI") == "AbcDefGhi"

    @pytest.mark.happy
    def test_snake(self):
        from stringbender import snake
        assert snake("aBC Def GHI") == "abc_def_ghi"
