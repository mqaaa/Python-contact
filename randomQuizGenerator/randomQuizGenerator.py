#! python3
import random
capitals = {'山西':'太原',
'河北':'石家庄',
'辽宁':'沈阳',
'吉林':'长春',
'黑龙江':'哈尔滨',
'江苏':'南京',
'安徽':'合肥',
'山东':'济南',
'浙江':'杭州',
'江西':'南昌',
'福建':'福州',
'湖南':'长沙',
'湖北':'武汉',
'河南':'郑州',
'广东':'广州',
'广西壮族自治区':'南宁',
'海南':'海口',
'贵州':'贵阳',
'云南':'昆明',
'四川':'成都',
'陕西':'西安',
'甘肃':'兰州',
'宁夏回族自治区':'银川',
'青海':'西宁',
'新疆维吾尔自治区':'乌鲁木齐',
'西藏自治区':'拉萨',
'台湾省':'台北',
'北京':'北京',
'上海':'上海',
'天津':'天津',
'重庆':'重庆',
'香港':'香港',
'澳门':'澳门'}

#随机出3份试卷
for quizNum in range(3):
    #创建文件
    quizFile = open('试卷%s.txt'%(quizNum+1),'w')
    answerFile = open('答案%s.txt'%(quizNum+1),'w')
    #文件表头
    quizFile.write('Name:\nData:\nPeriod:\n\n')
    quizFile.write((' '*20)+'试卷%s'%(quizNum+1))
    quizFile.write('\n\n')

    answerFile.write((' '*20)+'试卷%s'%(quizNum+1))
    answerFile.write('\n\n')
    #生成试题
    states = list(capitals.keys())
    random.shuffle(states)

    #创建选择答案选项
    for questionNum in range(33):
        Answer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(Answer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOption = wrongAnswer + [Answer]
        random.shuffle(answerOption)

        quizFile.write('%s.What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n'%('ABCD'[i],answerOption[i]))
        quizFile.write('\n')


        answerFile.write(' %s.%s\t'%(questionNum+1,'ABCD'[answerOption.index(Answer)]))
        if((questionNum+1) % 5 == 0):
            answerFile.write('\n')
    quizFile.close()
    answerFile.close()
    print('试卷'+str(quizNum+1)+'生成')
    
    
