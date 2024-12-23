import pytest


@pytest.mark.unit
class TestString:

    @pytest.mark.happy
    def test_camel(self):
        from stringbender import String

        assert String("abc deF_ghi jKl").camel() == "abcDefGhiJkl"
        assert String("abc.deF_ghi jKl").camel() == "abcDefGhiJkl"
        assert String("abc-deF_ghi jKl").camel() == "abcDefGhiJkl"
        assert String("abc deF\\ghi jKl").camel() == "abcDefGhiJkl"
        assert String("abc deF:ghi jKl").camel() == "abcDefGhiJkl"

    @pytest.mark.happy
    def test_kebob(self):
        from stringbender import String

        assert String("abc deF_ghi jKl").kebob() == "abc-def-ghi-jkl"
        assert String("abc.deF_ghi jKl").kebob() == "abc-def-ghi-jkl"
        assert String("abc d-eF_ghi jKl").kebob() == "abc-d-ef-ghi-jkl"
        assert String("abc deF\\ghi jKl").kebob() == "abc-def-ghi-jkl"
        assert String("abc deF:ghi jKl").kebob() == "abc-def-ghi-jkl"

    @pytest.mark.happy
    def test_pascal(self):
        from stringbender import String

        assert String("abc deF_ghi jKl").pascal() == "AbcDeFGhiJKl"
        assert String("abc.deF_ghi jKl").pascal() == "AbcDeFGhiJKl"
        assert String("abc-deF_ghi jKl").pascal() == "AbcDeFGhiJKl"
        assert String("abc deF\\ghi jKl").pascal() == "AbcDeFGhiJKl"
        assert String("abc deF:ghi jKl").pascal() == "AbcDeFGhiJKl"

    @pytest.mark.happy
    def test_snake(self):
        from stringbender import String

        assert String("abc deF_ghi jKl").snake() == "abc_de_f_ghi_j_kl"
        assert String("abc.deF_ghi jKl").snake() == "abc_de_f_ghi_j_kl"
        assert String("abc d-eF_ghi jKl").snake() == "abc_d_e_f_ghi_j_kl"
        assert String("abc deF\\ghi jKl").snake() == "abc_de_f_ghi_j_kl"
        assert String("abc deF:ghi jKl").snake() == "abc_de_f_ghi_j_kl"

    @pytest.mark.happy
    def test_snake_with_custom_delims(self):
        from stringbender import DEFAULT_DELIMITERS, String

        delims = DEFAULT_DELIMITERS + [",", "’", "!"]
        s = String("Careful man, there’s a beverage here!!")
        assert s.snake(delimiters=delims) == "careful_man_there_s_a_beverage_here"

    @pytest.mark.happy
    def test_toggle(self):
        from stringbender import String

        s = String("abcdefghijklmnopqrstuvwxyz")
        assert s.toggle()

    @pytest.mark.happy
    def test_as_str(self):
        from stringbender import String

        s = String("abc_def")
        s_str = s.as_str()

        assert s_str == "abc_def"
        assert type(s_str) is not String
