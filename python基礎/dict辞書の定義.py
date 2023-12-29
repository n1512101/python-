my_dict = {"Bob":77, "Jack":88, "Tom":99}

# 空辞書を定義
my_dict2 = {}
my_dict3 = dict()

score = my_dict["Bob"]
print(score)

stu_score_dict = {
    "Bob":{"math":70, "music":60}, 
    "Jack":{"math":40, "music":50}, 
    "Tom":{"math":80, "music":20}
}

print(f"学生たちのスコアは{stu_score_dict}")
print(stu_score_dict["Jack"]["math"])