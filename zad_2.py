import re

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
        " Sed #texting eget mattis sem. Mauris #frasista egestas" \
        " erat #tweetext quam, ut faucibus eros #frasier congue et." \
        " In blandit, mi eu porta lobortis, tortor nisl facilisis leo," \
        " at tristique #frasistas augue risus eu risus."

usuwanie_hashtagow = re.findall(r"#[a-z0-9]+", tekst)
print(usuwanie_hashtagow)