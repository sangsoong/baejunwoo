def get_average(marks:dict) -> float:
    sum = 0
    for key in marks:
        sum += marks[key]
    ave = sum / len(marks)
    
    print(f'평균은 {ave}점 입니다')
    
marks = {'국어':90, '영어':80, '수학':85}
get_average(marks)