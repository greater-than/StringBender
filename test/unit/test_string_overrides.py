import pytest
from stringbender import String


@pytest.mark.unit
class TestStringOverrides:
    @pytest.mark.happy
    def test_capitalize(self):
        s = String("i LOVE the Smell of Napalm in the mOrning.")
        assert s.capitalize() == "I love the smell of napalm in the morning."

    @pytest.mark.happy
    def test_casefold(self):
        s = String("gENTLEMEN, YOU CaN'T FigHT IN HErE! tHIS IS ThE wAR rOOM!")
        assert s.casefold() == "gentlemen, you can't fight in here! this is the war room!"

    @pytest.mark.happy
    def test_center(self):
        s = String("I'll be back")
        assert s.center(20, "*") == "****I'll be back****"

    @pytest.mark.happy
    def test_expandtabs(self):
        s = String("Bond.\tJames Bond.")
        assert s.expandtabs(10) == "Bond.     James Bond."

    @pytest.mark.happy
    def test_format(self):
        s = String("I want my {price} dollars!")
        assert s.format(price=2) == "I want my 2 dollars!"

    @pytest.mark.happy
    def test_format_map(self):
        map = {"stooge1": "Larry", "stooge2": "Moe", "stooge3": "Curly"}
        s = String("{stooge1} {stooge2} {stooge3}")
        assert "Larry Moe Curly" == s.format_map(map)

    @pytest.mark.happy
    def test_join(self):
        s = String(" ")
        s_joined = s.join(("No", "matter", "where", "you", "go,", "there", "you", "are."))
        assert s_joined == "No matter where you go, there you are."

    @pytest.mark.happy
    def test_ljust(self):
        s = String("There's no crying in baseball!")
        assert s.ljust(50, "*") == f"{s}********************"

    @pytest.mark.happy
    def test_lower(self):
        s = String("May the Force be with you.")
        assert s.lower() == "may the force be with you."

    @pytest.mark.happy
    def test_lstrip(self):
        s = String("          You talking to me?")
        assert s.lstrip() == "You talking to me?"

    @pytest.mark.happy
    def test_partition(self):
        s = String("You've gotta ask yourself a question: 'Do I feel lucky?'")
        s_1, s_2, s_3 = s.partition(": ")
        assert s_1 == "You've gotta ask yourself a question"
        assert s_2 == ": "
        assert s_3 == "'Do I feel lucky?'"

    @pytest.mark.happy
    def test_removeprefix(self):
        # TODO Install Python 3.9 and test
        import sys
        if sys.version_info >= (3, 9):
            s = String("Scarface: Say 'hello' to mhy little friend!")
            assert s.removeprefix("Scarface:") == "Say 'hello' to my little friend!"
        else:
            assert True

    @pytest.mark.happy
    def test_removesuffix(self):
        # TODO Install Python 3.9 and test
        import sys
        if sys.version_info >= (3, 9):
            s = String("Say 'hello' to mhy little friend! --Scarface")
            assert s.removeprefix(" --Scarface") == "Say 'hello' to my little friend!"
        else:
            assert True

    @pytest.mark.happy
    def test_replace(self):
        s = String("What*we've*got*here*is*a*failure*to*communicate.")
        assert s.replace("*", " ") == "What we've got here is a failure to communicate."

    @pytest.mark.happy
    def test_rjust(self):
        s = String("Here's Johnny!")
        assert s.rjust(30, "*") == f"****************{s}"

    @pytest.mark.happy
    def test_rpartition(self):
        s = String("Mrs Robinson, you're trying to seduce me. Aren't you?")
        s_1, s_2, s_3 = s.rpartition(". ")
        assert s_1 == "Mrs Robinson, you're trying to seduce me"
        assert s_2 == ". "
        assert s_3 == "Aren't you?"

    @pytest.mark.happy
    def test_rsplit(self):
        s = String("Carpe diem. Sieze the day, boys. Make your lives extraordinary")
        s_rsplit = s.rsplit(". ", 1)
        assert s_rsplit[0] == "Carpe diem. Sieze the day, boys"
        assert s_rsplit[1] == "Make your lives extraordinary"

    @pytest.mark.happy
    def test_rstrip(self):
        s = String("Nobody puts baby in a corner.          ")
        assert s.rstrip() == "Nobody puts baby in a corner."

    @pytest.mark.happy
    def test_split(self):
        s = String("I feel the need--the need for speed!")
        s_split = s.split("--")
        assert s_split[0] == "I feel the need"
        assert s_split[1] == "the need for speed!"

    @pytest.mark.happy
    def test_splitlines(self):
        s = String(("Cinderella story. Outta nowhere. A former greenskeeper, now,\n"
                    "about to become the Masters champion. It looks like a mirac...\n"
                    "It's in the hole! It's in the hole! It's in the hole!"))
        s_splitlines = s.splitlines()
        assert s_splitlines[0] == "Cinderella story. Outta nowhere. A former greenskeeper, now,"
        assert s_splitlines[1] == "about to become the Masters champion. It looks like a mirac..."
        assert s_splitlines[2] == "It's in the hole! It's in the hole! It's in the hole!"

    @pytest.mark.happy
    def test_strip(self):
        s = String("   I'll get you, my pretty, and your little dog, too!          ")
        assert s.strip() == "I'll get you, my pretty, and your little dog, too!"

    @pytest.mark.happy
    def test_swapcase(self):
        s = String("You're gonna need a bigger boat.")
        assert s.swapcase() == "yOU'RE GONNA NEED A BIGGER BOAT."

    @pytest.mark.happy
    def test_title(self):
        s = String("Is it safe?")
        assert s.title() == "Is It Safe?"

    @pytest.mark.happy
    def test_translate(self):
        s = String("God is my copilot")
        assert s.translate({71: 68, 100: 103}) == "Dog is my copilot"

    @pytest.mark.happy
    def test_upper(self):
        s = String("They're here!")
        assert s.upper() == "THEY'RE HERE!"

    @pytest.mark.happy
    def test_zfill(self):
        s = String("3.1417")
        assert s.zfill(10) == "00003.1417"

    # Magic Methods

    @pytest.mark.happy
    def test__add__(self):
        s = String("One plus one")
        assert s.__add__(" does not always equal two.") == "One plus one does not always equal two."

    @pytest.mark.happy
    def test__mul__(self):
        s = String("*")
        s_1 = s * 10
        assert s_1 == "**********"

    @pytest.mark.happy
    def test__rmul__(self):
        s = String("*")
        s_1 = 10 * s
        assert s_1 == "**********"
