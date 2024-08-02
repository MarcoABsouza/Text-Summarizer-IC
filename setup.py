import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer-IC"
AUTHOR_USER_NAME = "MarcoABsouza"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mabdsouza@outlook.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    description="Research project on summarizing multiple legal texts",
    url="https://github.com/MarcoABsouza/Text-Summarizer-IC",
    long_description=long_description,
    long_description_content = "text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)