acc1 = 0
pre1 = 0
rec1 = 0
f1 = 0
for num in range(5):

    predict_file = open('predict' + str(num) + '.txt', 'r').readlines()

    all_count = 0
    concord_count = 0
    correct_count = 0
    correct_match_count = 0
    pre = 0
    for line in predict_file:
        all_count += 1
        correct, predict, prob = line.split('\t')
        if correct == predict:
            concord_count += 1
        if correct == '1':
            correct_count += 1
            if correct == predict:
                correct_match_count += 1
        if predict == '1':
            pre += 1
    print 'roop:', num
    acc1 += concord_count / float(all_count)
    print 'rate of concordance:', concord_count / float(all_count)
    pre1 += correct_match_count / float(pre)
    pre = correct_match_count / float(pre)
    rec1 += correct_match_count / float( correct_count)
    rec = correct_match_count / float(correct_count)

    print 'Precision:', pre
    print 'Recall:', rec
    f1 += 2 * rec*pre/(rec+ pre)
    print 'F-measure:', 2 * rec * pre / (rec + pre)
    print ''

print 'result:'
print 'rate of concordance:', acc1 / 5

print 'Precision:', pre1 / 5
print 'Recall:', rec1 / 5
print 'F-measure:', f1 / 5
