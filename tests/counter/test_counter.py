from src.counter import count_ocurrences


def test_counter():
    content = ["Javascript", "Python"]
    number_of_words = [122, 1639]

    for lang in range(len(content)):
        content[lang] = content[lang].lower()
        result = count_ocurrences("src/jobs.csv", content[lang])
        assert result == number_of_words[lang]
