@ECHO OFF

cd %USERPROFILE%\workspace\jobs_mining

ECHO Crawling 'Java' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=java -a l=AC
scrapy crawl indeed -a q=java -a l=AL
scrapy crawl indeed -a q=java -a l=AP
scrapy crawl indeed -a q=java -a l=AM
scrapy crawl indeed -a q=java -a l=BA
scrapy crawl indeed -a q=java -a l=CE
scrapy crawl indeed -a q=java -a l=DF
scrapy crawl indeed -a q=java -a l=ES
scrapy crawl indeed -a q=java -a l=GO
scrapy crawl indeed -a q=java -a l=MA
scrapy crawl indeed -a q=java -a l=MT
scrapy crawl indeed -a q=java -a l=MS
scrapy crawl indeed -a q=java -a l=MG
scrapy crawl indeed -a q=java -a l=PA
scrapy crawl indeed -a q=java -a l=PB
scrapy crawl indeed -a q=java -a l=PR
scrapy crawl indeed -a q=java -a l=PE
scrapy crawl indeed -a q=java -a l=PI
scrapy crawl indeed -a q=java -a l=RJ
scrapy crawl indeed -a q=java -a l=RN
scrapy crawl indeed -a q=java -a l=RS
scrapy crawl indeed -a q=java -a l=RO
scrapy crawl indeed -a q=java -a l=RR
scrapy crawl indeed -a q=java -a l=SC
scrapy crawl indeed -a q=java -a l=SP
scrapy crawl indeed -a q=java -a l=SE
scrapy crawl indeed -a q=java -a l=TO

ECHO Crawling 'Ruby' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=ruby -a l=AC
scrapy crawl indeed -a q=ruby -a l=AL
scrapy crawl indeed -a q=ruby -a l=AP
scrapy crawl indeed -a q=ruby -a l=AM
scrapy crawl indeed -a q=ruby -a l=BA
scrapy crawl indeed -a q=ruby -a l=CE
scrapy crawl indeed -a q=ruby -a l=DF
scrapy crawl indeed -a q=ruby -a l=ES
scrapy crawl indeed -a q=ruby -a l=GO
scrapy crawl indeed -a q=ruby -a l=MA
scrapy crawl indeed -a q=ruby -a l=MT
scrapy crawl indeed -a q=ruby -a l=MS
scrapy crawl indeed -a q=ruby -a l=MG
scrapy crawl indeed -a q=ruby -a l=PA
scrapy crawl indeed -a q=ruby -a l=PB
scrapy crawl indeed -a q=ruby -a l=PR
scrapy crawl indeed -a q=ruby -a l=PE
scrapy crawl indeed -a q=ruby -a l=PI
scrapy crawl indeed -a q=ruby -a l=RJ
scrapy crawl indeed -a q=ruby -a l=RN
scrapy crawl indeed -a q=ruby -a l=RS
scrapy crawl indeed -a q=ruby -a l=RO
scrapy crawl indeed -a q=ruby -a l=RR
scrapy crawl indeed -a q=ruby -a l=SC
scrapy crawl indeed -a q=ruby -a l=SP
scrapy crawl indeed -a q=ruby -a l=SE
scrapy crawl indeed -a q=ruby -a l=TO

ECHO Crawling 'Python' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=python -a l=AC
scrapy crawl indeed -a q=python -a l=AL
scrapy crawl indeed -a q=python -a l=AP
scrapy crawl indeed -a q=python -a l=AM
scrapy crawl indeed -a q=python -a l=BA
scrapy crawl indeed -a q=python -a l=CE
scrapy crawl indeed -a q=python -a l=DF
scrapy crawl indeed -a q=python -a l=ES
scrapy crawl indeed -a q=python -a l=GO
scrapy crawl indeed -a q=python -a l=MA
scrapy crawl indeed -a q=python -a l=MT
scrapy crawl indeed -a q=python -a l=MS
scrapy crawl indeed -a q=python -a l=MG
scrapy crawl indeed -a q=python -a l=PA
scrapy crawl indeed -a q=python -a l=PB
scrapy crawl indeed -a q=python -a l=PR
scrapy crawl indeed -a q=python -a l=PE
scrapy crawl indeed -a q=python -a l=PI
scrapy crawl indeed -a q=python -a l=RJ
scrapy crawl indeed -a q=python -a l=RN
scrapy crawl indeed -a q=python -a l=RS
scrapy crawl indeed -a q=python -a l=RO
scrapy crawl indeed -a q=python -a l=RR
scrapy crawl indeed -a q=python -a l=SC
scrapy crawl indeed -a q=python -a l=SP
scrapy crawl indeed -a q=python -a l=SE
scrapy crawl indeed -a q=python -a l=TO

ECHO Crawling 'PHP' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=php -a l=AC
scrapy crawl indeed -a q=php -a l=AL
scrapy crawl indeed -a q=php -a l=AP
scrapy crawl indeed -a q=php -a l=AM
scrapy crawl indeed -a q=php -a l=BA
scrapy crawl indeed -a q=php -a l=CE
scrapy crawl indeed -a q=php -a l=DF
scrapy crawl indeed -a q=php -a l=ES
scrapy crawl indeed -a q=php -a l=GO
scrapy crawl indeed -a q=php -a l=MA
scrapy crawl indeed -a q=php -a l=MT
scrapy crawl indeed -a q=php -a l=MS
scrapy crawl indeed -a q=php -a l=MG
scrapy crawl indeed -a q=php -a l=PA
scrapy crawl indeed -a q=php -a l=PB
scrapy crawl indeed -a q=php -a l=PR
scrapy crawl indeed -a q=php -a l=PE
scrapy crawl indeed -a q=php -a l=PI
scrapy crawl indeed -a q=php -a l=RJ
scrapy crawl indeed -a q=php -a l=RN
scrapy crawl indeed -a q=php -a l=RS
scrapy crawl indeed -a q=php -a l=RO
scrapy crawl indeed -a q=php -a l=RR
scrapy crawl indeed -a q=php -a l=SC
scrapy crawl indeed -a q=php -a l=SP
scrapy crawl indeed -a q=php -a l=SE
scrapy crawl indeed -a q=php -a l=TO

ECHO Crawling '.NET' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=.net -a l=AC
scrapy crawl indeed -a q=.net -a l=AL
scrapy crawl indeed -a q=.net -a l=AP
scrapy crawl indeed -a q=.net -a l=AM
scrapy crawl indeed -a q=.net -a l=BA
scrapy crawl indeed -a q=.net -a l=CE
scrapy crawl indeed -a q=.net -a l=DF
scrapy crawl indeed -a q=.net -a l=ES
scrapy crawl indeed -a q=.net -a l=GO
scrapy crawl indeed -a q=.net -a l=MA
scrapy crawl indeed -a q=.net -a l=MT
scrapy crawl indeed -a q=.net -a l=MS
scrapy crawl indeed -a q=.net -a l=MG
scrapy crawl indeed -a q=.net -a l=PA
scrapy crawl indeed -a q=.net -a l=PB
scrapy crawl indeed -a q=.net -a l=PR
scrapy crawl indeed -a q=.net -a l=PE
scrapy crawl indeed -a q=.net -a l=PI
scrapy crawl indeed -a q=.net -a l=RJ
scrapy crawl indeed -a q=.net -a l=RN
scrapy crawl indeed -a q=.net -a l=RS
scrapy crawl indeed -a q=.net -a l=RO
scrapy crawl indeed -a q=.net -a l=RR
scrapy crawl indeed -a q=.net -a l=SC
scrapy crawl indeed -a q=.net -a l=SP
scrapy crawl indeed -a q=.net -a l=SE
scrapy crawl indeed -a q=.net -a l=TO

ECHO Crawling 'Javascript' jobs in all Brazilian states on Indeed.com.br

scrapy crawl indeed -a q=javascript -a l=AC
scrapy crawl indeed -a q=javascript -a l=AL
scrapy crawl indeed -a q=javascript -a l=AP
scrapy crawl indeed -a q=javascript -a l=AM
scrapy crawl indeed -a q=javascript -a l=BA
scrapy crawl indeed -a q=javascript -a l=CE
scrapy crawl indeed -a q=javascript -a l=DF
scrapy crawl indeed -a q=javascript -a l=ES
scrapy crawl indeed -a q=javascript -a l=GO
scrapy crawl indeed -a q=javascript -a l=MA
scrapy crawl indeed -a q=javascript -a l=MT
scrapy crawl indeed -a q=javascript -a l=MS
scrapy crawl indeed -a q=javascript -a l=MG
scrapy crawl indeed -a q=javascript -a l=PA
scrapy crawl indeed -a q=javascript -a l=PB
scrapy crawl indeed -a q=javascript -a l=PR
scrapy crawl indeed -a q=javascript -a l=PE
scrapy crawl indeed -a q=javascript -a l=PI
scrapy crawl indeed -a q=javascript -a l=RJ
scrapy crawl indeed -a q=javascript -a l=RN
scrapy crawl indeed -a q=javascript -a l=RS
scrapy crawl indeed -a q=javascript -a l=RO
scrapy crawl indeed -a q=javascript -a l=RR
scrapy crawl indeed -a q=javascript -a l=SC
scrapy crawl indeed -a q=javascript -a l=SP
scrapy crawl indeed -a q=javascript -a l=SE
scrapy crawl indeed -a q=javascript -a l=TO