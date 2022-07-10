import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

# text3.concordance("LIVED")

# text1.similar("monstrous")

# text1.common_contexts(["monstrous","abundant"])



