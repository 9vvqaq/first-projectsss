#GOVworkreport.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w =wordcloud.WordCloud( font_path = "msyh.ttc", width = 1000, height = 700, background_color ="black",)
w.generate(txt)
w.to_file("grordcloud.png")

