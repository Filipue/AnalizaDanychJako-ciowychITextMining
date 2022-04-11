import re


def cleaning_text(text: str) -> str:

    without_emoticons = re.sub(r"[:|:][-]/(<>)", " ", text.lower())
    without_digits = re.sub(r"\d", " ", without_emoticons)
    html_remove = re.sub(r"<.*?>", " ", without_digits)
    punctional_marks_remove = re.sub(r"[,.;]", " ", html_remove)
    multiple_spaces_remove = re.sub(' +', " ", punctional_marks_remove)
    instert_emoticons = ' '.join([str(i) for i in re.findall(r"[:|:][-]/(<>)", text)])
    result = multiple_spaces_remove + instert_emoticons
    return result
