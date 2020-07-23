n = 0
while True:
    n += 1
    percent = n/34867844
    percent = percent*100
    print(n,"%.5f" % percent, '%', 'of 34,867,844')
    if(n == 34867844):
        break
print('Finished,\nPress return to exit')
exit = input()
