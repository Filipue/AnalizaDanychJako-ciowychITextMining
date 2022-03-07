import re

emotikony = "Lorem ypsum :) eros congue et. In blandit, mi eu porta;)" \
            " ;( :> :< at tristique #frasistas augue risus" \
            " eu risus ;< :-) ;-)"

wyciaganie_emotikon = re.findall(r"[;|:][-]?\)|\(|<|>", emotikony)
print(wyciaganie_emotikon)
