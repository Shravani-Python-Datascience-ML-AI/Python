



def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *marks = input().split()
        scores = list(map(float,marks))
        student_marks[name] = scores
    query_name = input()
    s = 0
    for i in student_marks[query_name]:
        s = s + i
    print("{0:.2f}".format(s / 3))



if __name__ == "__main__":
    main()


