# jlpt_flashcard

http://doc.scrapy.org/en/latest/intro/tutorial.html

```
# to avoid system python
# it is required since system python has module "six"
# which cannot be upgraded because of OSX's rootless policy.
brew install python
pip install scrapy

git clone https://github.com/azrle/jlpt_flashcard.git
cd jlpt_flashcard
scrapy crawl grammar -o /tmp/result
```
